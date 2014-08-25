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
#
#++
# Name
#    vacation
#
# Purpose
#    Vacation-related routines
#--
#

import roundup.date
import common
import user_dynamic

def try_create_public_holiday (db, daily_record, date, user) :
    dyn = user_dynamic.get_user_dynamic (db, user, date)
    wh  = user_dynamic.day_work_hours   (dyn, date)
    if wh :
        # Check if there already is a public-holiday time_record
        trs = db.time_record.filter (None, dict (daily_record = daily_record))
        for tr in trs :
            wp = db.time_record.get (tr, 'wp')
            if wp is None :
                continue
            tp = db.time_project.getnode (db.time_wp.get (wp, 'project'))
            if tp.is_public_holiday :
                return
        loc = db.org_location.get (dyn.org_location, 'location')
        hol = db.public_holiday.filter \
            ( None
            , {'date' : common.pretty_range (date, date), 'locations' : loc}
            )
        if hol and wh :
            wp  = None
            try :
                ok  = db.time_project_status.lookup ('Open')
                prj = db.time_project.filter \
                    (None, dict (is_public_holiday = True, status = ok))
                wps = db.time_wp.filter \
                    (None, dict (project = prj, bookers = user))
                for wpid in wps :
                    w = db.time_wp.getnode (wpid)
                    if  (   w.time_start <= date
                        and (not w.time_end or date < w.time_end)
                        ) :
                        wp = wpid
                        break
            except (IndexError, KeyError) :
                pass
            holiday = db.public_holiday.getnode (hol [0])
            comment = holiday.name
            if holiday.description :
                comment = '\n'.join ((holiday.name, holiday.description))
            if holiday.is_half :
                wh = wh / 2.
            wh = user_dynamic.round_daily_work_hours (wh)
            db.time_record.create \
                ( daily_record  = daily_record
                , duration      = wh
                , wp            = wp
                , comment       = comment
                , work_location = db.work_location.lookup ('off')
                )
# end def try_create_public_holiday

def create_daily_recs (db, user, first_day, last_day) :
    d = first_day
    while d <= last_day :
        pr = common.pretty_range (d, d)
        x = db.daily_record.filter (None, dict (user = user, date = pr))
        if x :
            assert len (x) == 1
            x = x [0]
        else :
            x = db.daily_record.create \
                ( user              = user
                , date              = d
                , weekend_allowed   = False
                , required_overtime = False
                )
        try_create_public_holiday (db, x, d, user)
        d += common.day
# end def create_daily_recs

def leave_submissions_on_date (db, user, date) :
    """ Return all vacation records that overlap with the given date
    """
    dts = ';%s' % date.pretty (common.ymd)
    dte = '%s;' % date.pretty (common.ymd)
    vs = db.leave_submission.filter \
        (None, dict (user = user, first_day = dts, last_day = dte))
    return [db.leave_submission.getnode (v) for v in vs]
# end def leave_submissions_on_date

def leave_days (db, user, first_day, last_day) :
    d = first_day
    s = 0.0
    while d <= last_day :
        dyn = user_dynamic.get_user_dynamic (db, user, d)
        if not dyn :
            continue
        wh = user_dynamic.day_work_hours (dyn, d)
        ld = leave_duration (db, user, d)
        if ld != 0 :
            s += (ld / wh * 2 + 1) / 2
        d += common.day
    return s
# end def leave_days

def leave_duration (db, user, date) :
    """ Duration of leave on a single day to be booked. """
    dyn = user_dynamic.get_user_dynamic (db, user, date)
    wh  = user_dynamic.day_work_hours (dyn, date)
    if not wh :
        return 0.0
    dt  = common.pretty_range (date, date)
    dr  = db.daily_record.filter (None, dict (user = user, date = dt))
    assert len (dr) == 1
    trs = db.time_record.filter (None, dict (daily_record = dr [0]))
    bk  = 0.0
    for trid in trs :
        tr = db.time_record.getnode (trid)
        if not tr.wp :
            continue
        wp = db.time_wp.getnode (tr.wp)
        tp = db.time_project.getnode (wp.project)
        if tp.is_public_holiday :
            bk += tr.duration
    assert bk <= wh
    return wh - bk
# end def leave_duration

def next_yearly_vacation_date (db, user, date) :
    d = date + common.day
    dyn = user_dynamic.get_user_dynamic (db, user, d)
    if not dyn :
        dyn = user_dynamic.find_user_dynamic (db, user, d, '-')
    if not dyn :
        dyn = user_dynamic.find_user_dynamic (db, user, d, '+')
    if not dyn :
        return None
    y = int (d.get_tuple () [0])
    next_date = roundup.date.Date \
        ('%04d-%02d-%02d' % (y, dyn.vacation_month, dyn.vacation_day))
    if next_date < d :
        next_date = roundup.date.Date \
            ('%04d-%02d-%02d' % (y + 1, dyn.vacation_month, dyn.vacation_day))
    # Found a dyn user record too far in the future, can't determine
    # next yearly vacation date
    if dyn.valid_from > next_date :
        return None
    while dyn.valid_from <= next_date :
        if dyn.valid_to > next_date :
            # valid dyn record
            return next_date
        ndyn = user_dynamic.next_user_dynamic (db, dyn)
        if not ndyn or ndyn.valid_from > next_date :
            # use last dyn record, no next or too far in the future
            return next_date
        dyn = ndyn
# end def next_yearly_vacation_date

def interval_days (iv) :
    """ Compute number of days in a roundup.date Interval. The
        difference should be computed from two dates (without time)
        >>> D = roundup.date.Date
        >>> I = roundup.date.Interval
        >>> interval_days (D ('2014-01-07') - D ('2013-01-07'))
        365
        >>> interval_days (D ('2014-01-07') - D ('2012-01-07'))
        731
        >>> interval_days (I ('23d'))
        23
        >>> interval_days (I ('-23d'))
        -23
        >>> interval_days (D ('2012-01-07') - D ('2014-01-07'))
        -731
    """
    t = iv.get_tuple ()
    assert abs (t [0]) == 1
    assert t [1] == 0
    assert t [2] == 0
    assert t [4] == 0
    return t [3] * t [0]
# end def interval_days

def get_vacation_correction (db, user, date) :
    """ Get latest absolute vacation_correction.
    """
    dt = ";%s" % date.pretty (common.ymd)
    vc = db.vacation_correction.filter \
        ( None
        , dict (user = user, absolute = True, date = dt)
        , sort = [('-', 'date')]
        )
    if not vc :
        return
    return db.vacation_correction.getnode (vc [0])
# end def get_vacation_correction

def remaining_vacation (db, user, date, consolidated = None) :
    """ Compute remaining vacation on the given date
    """
    vc = get_vacation_correction (db, user, date)
    if not vc :
        return
    dt = common.pretty_range (vc.date, date)
    if consolidated is None :
        consolidated = consolidated_vacation (db, user, date, vc)
    vac = consolidated
    # All time recs with vacation wp up to date
    ds  = [('+', 'date')]
    vtp = db.time_project.filter (None, dict (is_public_holiday = True))
    assert vtp
    vwp = db.time_wp.filter (None, dict (project = vtp))
    dr  = db.daily_record.filter (None, dict (user = user, date = dt))
    dtt = [('+', 'daily_record.date')]
    trs = db.time_record.filter \
        (None, dict (daily_record = dr, wp = vwp), sort = dtt)
    for tid in trs :
        tr  = db.time_record.getnode  (tid)
        dr  = db.daily_record.getnode (tr.daily_record)
        dyn = user_dynamic.get_user_dynamic (db, user, dr.date)
        wh  = user_dynamic.day_work_hours (dyn, dr.date)
        assert wh
        vac -= (tr.duration / wh * 2 + 1) / 2.
    # All vacation_correction records up to date but starting with one
    # day later (otherwise we'll find the absolute correction)
    dt  = common.pretty_range (vc.date + common.day, date)
    vcs = db.vacation_correction.filter \
        (None, dict (user = user, date = dt), sort = ds)
    for vcid in vcs :
        vc = db.vacation_correction.getnode (vcid)
        assert not vc.absolute
        vac += vc.days
    return vac
# end def remaining_vacation

def consolidated_vacation (db, user, date, vc = None) :
    """ Compute remaining vacation on the given date
    """
    vc  = vc or get_vacation_correction (db, user, date)
    if not vc :
        return None
    dt  = common.pretty_range (vc.date, date)
    ed  = next_yearly_vacation_date (db, user, date)
    d   = vc.date
    dyn = user_dynamic.get_user_dynamic (db, user, d)
    if not dyn :
        dyn = user_dynamic.find_user_dynamic (db, user, d)
    vac = float (vc.days)
    while dyn and d < ed :
        if dyn.valid_from > d :
            d = dyn.valid_from
            continue
        assert not dyn.valid_to or dyn.valid_to > d
        if dyn.valid_to and dyn.valid_to <= ed :
            vac += interval_days (dyn.valid_to - d) * dyn.vacation_yearly / 365.
            dyn = user_dynamic.next_user_dynamic (db, dyn)
        else :
            vac += interval_days (ed - d) * dyn.vacation_yearly / 365.
            d = ed
    return vac
# end def consolidated_vacation

def valid_wps (db, filter, username = None, date = None, srt = None) :
    # FIXME: One day we want to refactore 'work_packages' in
    # extensions/interfaces to use this.
    srt  = srt or [('+', 'id')]
    wps  = {}
    date = date or roundup.date.Date ('.')
    d    = dict (time_start = ';%s' % date.pretty (common.ymd))
    d.update (filter)
    wps = []
    if username :
        for bookers in ['-1', db.user.lookup (username)] :
            d ['bookers'] = bookers
            wps.extend (db.time_wp.filter (None, d, srt))
    else :
        wps.extend (db.time_wp.filter (None, d, srt))
    wps = [db.time_wp.getnode (w) for w in wps]
    wps = [w for w in wps if not w.time_end or w.time_end > date]
    return [w.id for w in wps]
# end def valid_wps

def valid_leave_wps (db, username = None, date = None, srt = None) :
    d = {'project.approval_required' : True}
    return valid_wps (db, d, username, date, srt)
# end def valid_leave_wps

### __END__
