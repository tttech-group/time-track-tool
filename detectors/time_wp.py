#! /usr/bin/python
# -*- coding: iso-8859-1 -*-
# Copyright (C) 2006-18 Dr. Ralf Schlatterbeck Open Source Consulting.
# Reichergasse 131, A-3411 Weidling.
# Web: http://www.runtux.com Email: office@runtux.com
# All rights reserved
# ****************************************************************************
# 
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
#    time_wp
#
# Purpose
#    Detectors for 'time_wp'
#

from roundup.exceptions             import Reject
from roundup.date                   import Date
from roundup.cgi.TranslationService import get_translation
from freeze                         import freeze_date

import re
import common
import user_dynamic
import lib_auto_wp

def check_duplicate_field_value (cl, project, field, value) :
    ids     = cl.filter (None, {field : value, 'project' : project})
    # filter for exact match!
    ids     = [i for i in ids if cl.get (i, field) == value]
    if ids :
        assert (len (ids) == 1)
        raise Reject, _ ('Duplicate %(field)s "%(value)s"') % locals ()
# end def check_duplicate_field_value

def check_time_wp (db, cl, nodeid, new_values) :
    common.require_attributes \
        ( _
        , cl
        , nodeid
        , new_values
        , 'name'
        , 'project'
        , 'is_public'
        )
    common.check_prop_len (_, new_values.get ('name', cl.get (nodeid, 'name')))
    opr  = cl.get (nodeid, 'project')
    oprj = db.time_project.getnode (opr)
    prid = new_values.get ('project', opr)
    prj  = db.time_project.getnode (prid)
    act  = db.time_project_status.get (prj.status,  'active')
    acto = db.time_project_status.get (oprj.status, 'active')
    if (not act or not acto) and opr != prid :
        raise Reject \
            (_ ("No change of %(tp)s from/to closed %(tp)s")
            % dict (tp = _ ('time_project'))
            )
    if not act and 'time_end' in new_values :
        end = new_values ['time_end']
        now = Date ('.')
        od  = cl.get (nodeid, 'time_end')
        if (od and od < now) or end > now :
            raise Reject \
                (_ ("No change of %(te)s for %(wp)s of inactive %(tp)s")
                % dict ( te = _ ('time_end')
                       , wp = _ ('time_wp')
                       , tp = _ ('time_project')
                       )
                )
    for i in 'name', 'wp_no' :
        if i in new_values and new_values [i] is not None :
            check_duplicate_field_value (cl, prid, i, new_values [i])
    if 'project' in new_values :
        new_values ['cost_center'] = prj.cost_center
# end def check_time_wp

def new_time_wp (db, cl, nodeid, new_values) :
    if 'is_public' not in new_values :
        new_values ['is_public'] = False
    common.require_attributes \
        ( _
        , cl
        , nodeid
        , new_values
        , 'name'
        , 'responsible'
        , 'project'
        , 'is_public'
        )
    prid = new_values ['project']
    uid  = db.getuid ()
    prj  = db.time_project.getnode (prid)
    if  (  uid != prj.responsible
        and uid != prj.deputy
        and not common.user_has_role (db, uid, 'Project')
        and uid != '1'
        ) :
        raise Reject, ("You may only create WPs for your own projects")
    act  = db.time_project_status.get (prj.status, 'active')
    if not act and uid != '1' :
        raise Reject, ("You may only create WPs for active projects")
    if 'durations_allowed' not in new_values :
        new_values ['durations_allowed'] = False
    common.check_prop_len (_, new_values ['name'])
    project = new_values  ['project']
    if 'wp_no' in new_values and not new_values ['wp_no'] :
        del new_values ['wp_no']
    for i in 'name', 'wp_no' :
        if i in new_values :
            check_duplicate_field_value (cl, project, i, new_values [i])
    status = db.time_project.get (project, 'status')
    new_values ['cost_center'] = prj.cost_center
# end def new_time_wp

def check_expiration (db, cl, nodeid, new_values) :
    if  (  'has_expiration_date' in new_values
        or 'time_end' in new_values
        or not nodeid
        ) :
        if 'time_end' in new_values :
            time_end = new_values ['time_end']
        elif nodeid :
            time_end = cl.get (nodeid, 'time_end')
        else :
            time_end = None
        if time_end :
            new_values ['has_expiration_date'] = True
        else :
            new_values ['has_expiration_date'] = False
# end def check_expiration

def check_name (db, cl, nodeid, new_values) :
    """ Ensure that names do not contain certain characters """
    forbidden = ',/"'
    if 'name' in new_values :
        name = new_values ['name']
        for c in forbidden :
            if c in name :
                raise Reject (_ ("Name contains forbidden character %s") % c)
# end def check_name

def check_summary_no (db, cl, nodeid, new_values) :
    """ Ensure that summary_no is filled in for wps that belong to a
        time_project with 'project=yes'
    """
    prid = new_values.get ('project')
    if not prid :
        assert nodeid
        prid = cl.get (nodeid, 'project')
    prj = db.time_project.getnode (prid)
    if prj.op_project :
        common.require_attributes \
            (_, cl, nodeid, new_values, 'time_wp_summary_no')
# end def check_summary_no

def check_epic_key (db, cl, nodeid, new_values) :
    """ Ensure that the epic_key matches the format of keys in Jira
    """
    if 'epic_key' in new_values :
        r = re.compile (r'^[A-Z][0-9A-Z_]+[0-9A-Z]-[0-9]+$')
        k = new_values ['epic_key']
        if k is not None and not r.search (k) :
            epickey = _ ('epic_key')
            raise Reject (_ ("Not a valid %(epickey)s: %(k)s") % locals ())
# end def check_epic_key

def wp_check_auto_wp (db, cl, nodeid, new_values) :
    """ Check that modifications to wp that has auto_wp set is ok
    """
    if not nodeid and 'auto_wp' not in new_values :
        return
    if nodeid :
        if not cl.get (nodeid, 'auto_wp') :
            if 'auto_wp' in new_values :
                raise Reject \
                    (_ ("Property %s may not change") % _ ('auto_wp'))
            return
    props = \
        ( 'auto_wp'
        , 'bookers'
        , 'durations_allowed'
        , 'contract_type'
        , 'org_location'
        , 'project'
        , 'travel'
        , 'is_public'
        )
    if nodeid :
        for p in props :
            if p in new_values :
                raise Reject \
                    (_ ("Property %s may not change for auto wp") % _ (p))
        bookers = cl.get (nodeid, 'bookers')
        auto_wp = cl.get (nodeid, 'auto_wp')
    else :
        common.require_attributes \
            ( _, cl, nodeid, new_values
            , 'bookers'
            , 'auto_wp'
            , 'travel'
            , 'time_project'
            , 'durations_allowed'
            )
        bookers = new_values ['bookers']
        auto_wp = new_values ['auto_wp']
    auto_wp = db.auto_wp.getnode (auto_wp)
    if 'time_start' not in new_values and 'time_end' not in new_values :
        return
    start = new_values.get ('time_start')
    end   = new_values.get ('time_end')
    if not start :
        assert nodeid
        start = cl.get (nodeid, 'time_start')
    if not end and nodeid :
        end = cl.get (nodeid, 'time_end')
    assert len (bookers) == 1
    booker = bookers [0]
    olo    = auto_wp.org_location
    freeze = freeze_date (db, booker)
    if freeze :
        if start < freeze and 'time_start' in new_values :
            raise Reject (_ ("No change of auto wp before freeze date"))
        if end and end in new_values and end < freeze :
            raise Reject (_ ("No change of auto wp before freeze date"))
    # Get dyn user for start
    dyn = user_dynamic.get_user_dynamic (db, booker, start)
    if not dyn and start != end :
        raise Reject (_ ("Invalid change of start/end: no dyn. user"))
    if not dyn :
        return
    if not lib_auto_wp.is_correct_dyn (dyn, olo) :
        raise Reject \
            (_ ("Invalid change of start: Invalid dyn. user"))
    # loop backwards through dyns
    if 'time_start' in new_values :
        # Find the first dyn user which matches up with our start date
        prev = dyn
        while prev.valid_from > start :
            p = user_dynamic.prev_user_dynamic (db, prev)
            if  (  p.valid_to != prev.valid_from
                or not lib_auto_wp.is_correct_dyn (p, olo)
                ) :
                raise Reject ("Invalid change of start: Invalid dyn. user")
            prev = p
        # We need to find previous wp if we don't start freezedate + day
        if prev.valid_from < start and start > freeze + common.day :
            d = dict \
                ( auto_wp  = auto_wp.id
                , time_end = common.pretty_range (None, start)
                )
            wps = db.time_wp.filter (None, d, sort = ('-', 'time_end'))
            if not wps :
                raise Reject (_ ("Invalid change of start: No prev. WP"))
            wp = db.time_wp.getnode (wps [0])
            if wp.valid_to != start :
                raise Reject (_ ("Invalid change of start: Invalid prev. WP"))
    # loop forward through dyns
    if 'time_end' in new_values :
        next = dyn
        # Need to find next wp if dyn is valid longer than end and not
        # limited by a duration
        dur_end = lib_auto_wp.auto_wp_duration_end (db, auto_wp, booker)
        while next.valid_to and (not end or next.valid_to < end) :
            if dur_end and dur_end <= next.valid_to :
                break
            n  = user_dynamic.next_user_dynamic (db, next)
            if  (  n.valid_from != next.valid_to
                or not lib_auto_wp.is_correct_dyn (n, olo)
                ) :
                raise Reject ("Invalid change of end: Invalid dyn. user")
            next = n
        if end and not dur_end and (not next.valid_to or end < next.valid_to) :
            d = dict \
                ( auto_wp    = auto_wp.id
                , time_start = common.pretty_range (end)
                )
            wps = db.time_wp.filter (None, d, sort = ('+', 'time_start'))
            if not wps :
                raise Reject (_ ("Invalid change of end: No next WP"))
            wp = db.time_wp.getnode (wps [0])
            if wp.valid_from != end :
                raise Reject (_ ("Invalid change of end: Invalid next WP"))
# end def wp_check_auto_wp

def init (db) :
    if 'time_wp' not in db.classes :
        return
    global _
    _   = get_translation \
        (db.config.TRACKER_LANGUAGE, db.config.TRACKER_HOME).gettext
    db.time_wp.audit  ("create", new_time_wp)
    db.time_wp.audit  ("set",    check_time_wp)
    db.time_wp.audit  ("create", check_expiration, priority = 400)
    db.time_wp.audit  ("set",    check_expiration, priority = 400)
    db.time_wp.audit  ("create", check_name)
    db.time_wp.audit  ("set",    check_name)
    db.time_wp.audit  ("create", check_summary_no, priority = 250)
    db.time_wp.audit  ("set",    check_summary_no, priority = 250)
    db.time_wp.audit  ("create", wp_check_auto_wp, priority = 300)
    db.time_wp.audit  ("set",    wp_check_auto_wp, priority = 300)
    db.time_wp.audit  ("create", check_epic_key)
    db.time_wp.audit  ("set",    check_epic_key)
    # Name check for time_project too
    db.time_project.audit  ("create", check_name)
    db.time_project.audit  ("set",    check_name)
# end def init

### __END__ time_wp
