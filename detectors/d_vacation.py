#! /usr/bin/python
# -*- coding: iso-8859-1 -*-
# Copyright (C) 2014 Dr. Ralf Schlatterbeck Open Source Consulting.
# Reichergasse 131, A-3411 Weidling.
# Web: http://www.runtux.com Email: office@runtux.com
# All rights reserved
# ****************************************************************************
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
# ****************************************************************************

from roundup.exceptions             import Reject
from roundup.date                   import Date, Interval
from roundup.cgi.TranslationService import get_translation
from roundup                        import roundupdb

import common
import vacation

def check_range (db, nodeid, uid, first_day, last_day) :
    """ Check length of range and if there are any records in the given
        time-range for this user. This means either the first day of an
        existing record is inside the new range or the last day is
        inside the new range or the first day is lower than the first
        day *and* the last day is larger (new interval is contained in
        existing interval).
    """
    if (last_day - first_day) > Interval ('30d') :
        raise Reject (_ ("Max. 30 days for single vacation submission"))
    range = common.pretty_range (first_day, last_day)
    both  = (first_day.pretty (';%Y-%m-%d'), last_day.pretty ('%Y-%m-%d;'))
    for f, l in ((range, None), (None, range), both) :
        d = dict (user = uid)
        if f :
            d ['first_day'] = f
        if l :
            d ['last_day'] = l
        r = [x for x in db.vacation_submission.filter (None, d) if x != nodeid]
        if r :
            raise Reject \
                (_ ("You already have vacation requests in this time range"))
# end def check_range

def check_wp (db, wp_id) :
    wp = db.time_wp.getnode (wp_id)
    tp = db.time_project.getnode (wp.project)
    if not tp.approval_required :
        raise Reject (_ ("No approval required for work package"))
# end def check_wp

def new_submission (db, cl, nodeid, new_values) :
    """ Check that new vacation submission is allowed and has sensible
        parameters
    """
    uid = db.getuid ()
    st_open = db.vacation_status.lookup ('open')
    common.require_attributes \
        (_, cl, nodeid, new_values, 'first_day', 'last_day', 'time_wp')
    if 'user' not in new_values :
        user = new_values ['user'] = uid
    else :
        user = new_values ['user']
    first_day = new_values ['first_day']
    last_day  = new_values ['last_day']
    check_range (db, None, user, first_day, last_day)
    check_wp    (db, new_values ['time_wp'])
    if 'status' in new_values and new_values ['status'] != st_open :
        raise Reject (_ ('Initial status must be "open"'))
    if 'status' not in new_values :
        new_values ['status'] = st_open
    if user != uid and not common.user_has_role (db, uid, 'HR-vacation') :
        raise Reject \
            (_ ("Only special role may create submission for other user"))
# end def new_submission

def check_submission (db, cl, nodeid, new_values) :
    """ Check that changes to a vacation submission are ok.
        We basically allow changes of first_day, last_day, and time_wp
        in status 'open'. The user must never change. The status
        transitions are bound to certain roles. Note that this auditor
        is called *after* it has been verified that a requested state
        change is at least possible (although we still have to check the
        role).
    """
    common.reject_attributes (_, new_values, 'user')
    old = cl.getnode (nodeid)
    uid = db.getuid ()
    old_status = db.vacation_status.get (old.status, 'name')
    new_status = db.vacation_status.get \
        (new_values.get ('status', old.status), 'name')
    if old_status != new_status or old_status != 'open' :
        common.reject_attributes \
            (_, new_values, 'first_day', 'last_day', 'time_wp')
    first_day = new_values.get ('first_day', cl.get (nodeid, 'first_day'))
    last_day  = new_values.get ('last_day',  cl.get (nodeid, 'last_day'))
    time_wp   = new_values.get ('time_wp',   cl.get (nodeid, 'time_wp'))
    check_range (db, nodeid, old.user, first_day, last_day)
    check_wp    (db, time_wp)
    if old_status != new_status :
        # Allow special HR role to do any (possible) state changes
        if common.user_has_role (db, uid, 'HR-vacation') :
            ok = True
        else :
            ok = False
            tp = db.time_project.getnode \
                (db.time_wp.get (old.time_wp, 'project'))
            if not ok and uid == old.user :
                if old_status == 'open' and new_status == 'submitted' :
                    ok = True
                if old_status == 'accepted' :
                    ok = True
                if old_status == 'submitted' and new_status == 'open' :
                    ok = True
            clearer = common.clearance_by (db, old.user)
            if  (  not ok
                and (   (uid in clearer and not tp.approval_hr)
                    or  common.user_has_role (db, uid, 'HR-leave-approval')
                    )
                ) :
                if  (   old_status == 'submitted'
                    and new_status in ('accepted', 'declined')
                    ) :
                    ok = True
                if old_status == 'cancel requested' :
                    ok = True
            if not ok :
                raise Reject (_ ("Permission denied"))
# end def check_submission

def vac_report (db, cl, nodeid, new_values) :
    raise Reject (_ ("Creation of vacation report is not allowed"))
# end def vac_report

def daily_recs (db, cl, nodeid, old_values) :
    vs = cl.getnode (nodeid)
    vacation.create_daily_recs (db, vs.user, vs.first_day, vs.last_day)
# end def daily_recs

def state_change_reactor (db, cl, nodeid, old_values) :
    vs         = cl.getnode (nodeid)
    old_status = old_values.get ('status')
    new_status = vs.status
    accepted   = db.vacation_status.lookup ('accepted')
    declined   = db.vacation_status.lookup ('declined')
    submitted  = db.vacation_status.lookup ('submitted')
    cancelled  = db.vacation_status.lookup ('cancelled')
    if old_status == new_status :
        return
    dt  = common.pretty_range (vs.first_day, vs.last_day)
    drs = db.daily_record.filter (None, dict (user = vs.user, date = dt))
    trs = db.time_record.filter (None, dict (daily_record = drs))
    tp  = db.time_project.getnode (db.time_wp.get (vs.time_wp, 'project'))
    if new_status == accepted :
        handle_accept  (db, vs, trs, old_status)
    elif new_status == declined :
        handle_decline (db, vs)
    elif new_status == submitted :
        # FIXME: also check if wp over yearly vacation
        hr_only = tp.approval_hr
        handle_submit  (db, vs, hr_only)
    elif new_status == cancelled :
        handle_cancel  (db, vs, trs)
# end def state_change_reactor

def handle_accept (db, vs, trs, old_status) :
    cancr = db.vacation_status.lookup ('cancel requested')
    warn  = []
    for trid in trs :
        tr  = db.time_record.getnode (trid)
        wp  = tp = None
        if tr.wp is not None :
            wp  = db.time_wp.getnode (tr.wp)
            tp  = db.time_project.getnode (wp.project)
        trd = db.daily_record.get (tr.daily_record, 'date')
        if tp is None or not tp.is_public_holiday :
            if wp is None or wp.id != vs.time_wp :
                dt = trd.pretty (common.ymd)
                st = tr.start or ''
                en = tr.end   or ''
                wn = (wp and wp.name) or ''
                tn = (tp and tp.name) or ''
                warn.append ((dt, tn, wn, st, en, tr.duration))
            db.time_record.retire (trid)
    d = vs.first_day
    off = db.work_location.lookup ('off')
    while (d <= vs.last_day) :
        vd = vacation.vacation_duration (db, vs.user, d)
        if vd :
            dt = common.pretty_range (d, d)
            dr = db.daily_record.filter (None, dict (user = vs.user, date = dt))
            assert len (dr) == 1
            db.time_record.create \
                ( daily_record  = dr [0]
                , duration      = vd
                , work_location = off
                , wp            = vs.time_wp
                )
        d += common.day
    mailer  = roundupdb.Mailer (db.config)
    now     = Date ('.')
    wp      = db.time_wp.getnode (vs.time_wp)
    email   = db.user.get (vs.user, 'address')
    wpn     = wp.name
    tpn     = db.time_project.get (wp.project, 'name')
    fday    = vs.first_day.pretty (common.ymd)
    lday    = vs.last_day.pretty  (common.ymd)
    if old_status == cancr :
        subject = 'Leave "%(wpn)s" %(fday)s-%(lday)s not cancelled' % locals ()
        content = 'Your cancel request "%(tpn)s/%(wpn)s" was not granted.\n' \
                % locals ()
        content += "Please contact your supervisor.\n"
    else :
        subject = 'Leave "%(wpn)s" %(fday)s-%(lday)s accepted' % locals ()
        content = ('Your absence request "%(tpn)s/%(wpn)s" '
                   'has been accepted.\n'
                  % locals ()
                  )
    if warn :
        content = [content]
        content.append \
            ("The following existing time records have been deleted:")
        tdl = wdl = 0
        for w in warn :
            tdl = max (tdl, len (w [1]))
            wdl = max (wdl, len (w [2]))
        fmt = "%%s: %%%ds / %%%ds %%5s-%%5s duration: %%s" % (tdl, wdl)
        for w in warn :
            content.append (fmt % w)
        content = '\n'.join (content)
    try :
        mailer.standard_message ((email,), subject, content)
    except roundupdb.MessageSendError, message :
        raise roundupdb.DetectorError, message
# end def handle_accept

def handle_cancel (db, vs, trs) :
    for trid in trs :
        tr  = db.time_record.getnode (trid)
        wp  = db.time_wp.getnode (tr.wp)
        tp  = db.time_project.getnode (wp.project)
        trd = db.daily_record.get (tr.daily_record, 'date')
        if not tp.is_public_holiday :
            assert tp.approval_required
            db.time_record.retire (trid)
# end def handle_cancel

def handle_decline (db, vs) :
    mailer  = roundupdb.Mailer (db.config)
    now     = Date ('.')
    wp      = db.time_wp.getnode (vs.time_wp)
    email   = db.user.get (vs.user, 'address')
    wpn     = wp.name
    tpn     = db.time_project.get (wp.project, 'name')
    fday    = vs.first_day.pretty (common.ymd)
    lday    = vs.last_day.pretty  (common.ymd)
    subject = 'Leave "%(wpn)s" %(fday)s-%(lday)s declined' % locals ()
    content = 'Your absence request "%(tpn)s/%(wpn)s" has been declined.\n' \
            % locals ()
    content += "Please contact your supervisor.\n"
    try :
        mailer.standard_message ((email,), subject, content)
    except roundupdb.MessageSendError, message :
        raise roundupdb.DetectorError, message
# end def handle_decline

def handle_submit (db, vs, hr_only) :
    mailer  = roundupdb.Mailer (db.config)
    now     = Date ('.')
    wp      = db.time_wp.getnode (vs.time_wp)
    user    = db.user.getnode (vs.user)
    # always send to supervisor (and/or substitute), too.
    emails  = [db.user.get (x, 'address')
               for x in common.clearance_by (db, vs.user)
              ]
    if hr_only :
        emails.extend \
            (db.user.get (u, 'address')
             for u in common.get_uids_with_role (db, 'HR-leave-approval')
            )
    wpn     = wp.name
    tpn     = db.time_project.get (wp.project, 'name')
    fday    = vs.first_day.pretty (common.ymd)
    lday    = vs.last_day.pretty  (common.ymd)
    realnm  = user.realname
    nick    = user.nickname.upper ()
    url     = 'FIXME'
    subject = 'Leave request "%(wpn)s" from %(nick)s' % locals ()
    content = '%(realnm)s has submitted a leave request "%(wpn)s".' % locals ()
    if hr_only :
        content += "\nNeeds approval by HR."
    content += '\n' + url
    try :
        mailer.standard_message (emails, subject, content)
    except roundupdb.MessageSendError, message :
        raise roundupdb.DetectorError, message
# end def handle_decline

def init (db) :
    global _
    _   = get_translation \
        (db.config.TRACKER_LANGUAGE, db.config.TRACKER_HOME).gettext

    if 'vacation_submission' not in db.classes :
        return
    # Status is checked with prio 200, we come later.
    db.vacation_submission.audit ("set",    check_submission, priority = 300)
    db.vacation_submission.audit ("create", new_submission)
    db.vacation_submission.react ("create", daily_recs, priority = 80)
    db.vacation_submission.react ("set",    daily_recs, priority = 80)
    db.vacation_submission.react ("set",    state_change_reactor)
    db.vacation_report.audit     ("create", vac_report)
# end def init
