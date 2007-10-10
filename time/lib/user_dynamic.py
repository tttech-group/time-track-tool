#! /usr/bin/python
# -*- coding: iso-8859-1 -*-
# Copyright (C) 2006 Dr. Ralf Schlatterbeck Open Source Consulting.
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
#    user_dynamic
#
# Purpose
#    access routines for 'user_dynamic'
#

import sys

from time         import gmtime
from bisect       import bisect_left
from operator     import add

from roundup.date import Date

from common       import ymd, next_search_date, end_of_period, freeze_date
from common       import pretty_range, day, period_week, period_is_weekly
from freeze       import find_prev_dr_freeze

last_dynamic = None # simple one-element cache

def get_user_dynamic (db, user, date) :
    """ Get a user_dynamic record by user and date.
        Return None if no record could be found.
    """
    global last_dynamic
    user = str  (user)
    date = Date (date)
    if  (   last_dynamic
        and last_dynamic.user == user
        and last_dynamic.valid_from < date
        and (not last_dynamic.valid_to or last_dynamic.valid_to > date)
        ) :
        return last_dynamic
    ids = db.user_dynamic.filter \
        ( None, dict (user = user, valid_from = date.pretty (';%Y-%m-%d'))
        , group = ('-', 'valid_from')
        )
    if ids :
        last_dynamic = db.user_dynamic.getnode (ids [0])
        if not last_dynamic.valid_to or last_dynamic.valid_to > date :
            return last_dynamic
    return None
# end def get_user_dynamic

def first_user_dynamic (db, user, direction = '+', date = None) :
    """Search for first user_dynamic record, optionally starting at
       date.
       
       The direction may be specified as '-' to search for the last
       record, see last_user_dynamic
    """
    filter_dict = dict (user = user)
    if date :
        format = '%Y-%m-%d;'
        if direction == '-' :
            format = ';%Y-%m-%d'
        filter_dict ['valid_from'] = date.pretty (format)
    ids = db.user_dynamic.filter \
        (None, filter_dict, group = (direction, 'valid_from'))
    if ids :
        dyn = db.user_dynamic.getnode (ids [0])
        # one record too far?
        if date and direction == '+' and dyn.valid_from > date :
            d = prev_user_dynamic (db, dyn)
            if d and d.valid_from <= date and d.valid_to > date :
                return d
        return dyn
    elif date and direction == '+' :
        dyn = last_user_dynamic (db, user)
        if  (   dyn
            and dyn.valid_from <= date
            and (not dyn.valid_to or dyn.valid_to > date)
            ) :
            return dyn
    return None
# end def first_user_dynamic

def last_user_dynamic (db, user, date = None) :
    """Search for last user_dynamic record, optionally searching
       backwards from date.
    """
    return first_user_dynamic (db, user, direction = '-', date = date)
# end def last_user_dynamic

def find_user_dynamic (db, user, date, direction = '+') :
    date = next_search_date (date, direction)
    ids = db.user_dynamic.filter \
        ( None, dict (user = user, valid_from = date)
        , group = (direction, 'valid_from')
        )
    if ids :
        return db.user_dynamic.getnode (ids [0])
    return None
# end def find_user_dynamic

def _next_user_dynamic (db, dynuser, direction = '+') :
    id = dynuser.user
    try :
        db = db._db
        id = id.id
    except AttributeError :
        pass
    return find_user_dynamic (db, id, dynuser.valid_from, direction = direction)
# end def _find_user_dynamic

def next_user_dynamic (db, dynuser) :
    return _next_user_dynamic (db, dynuser)
# end def next_user_dynamic

def prev_user_dynamic (db, dynuser) :
    return _next_user_dynamic (db, dynuser, direction = '-')
# end def prev_user_dynamic

def act_or_latest_user_dynamic (db, user) :
    ud = get_user_dynamic (db, user, Date ('.'))
    if not ud :
        ud = last_user_dynamic (db, user)
    return ud
# end def act_or_latest_user_dynamic

wdays = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']

def day_work_hours (dynuser, date) :
    """ Compute hours for a holiday etc from the date """
    wday  = gmtime (date.timestamp ())[6]
    return _day_work_hours (dynuser, wday)
# end def day_work_hours

def _day_work_hours (dynuser, wday) :
    hours = dynuser ['hours_' + wdays [wday]]
    if hours is not None :
        return hours
    if wday in (5, 6) or not dynuser.weekly_hours :
        return 0
    return dynuser.weekly_hours / 5.
# end def _day_work_hours

def weekly_hours (dynuser) :
    return sum (_day_work_hours (dynuser, wday) for wday in range (7))
# end def weekly_hours

def is_work_day (dynuser, date) :
    """ Return True if the given date is a work day for this user.
        Usually returns True if not on a weekend day but individual work
        times can be defined with field_mon, ..., field_sun
    """
    return bool (day_work_hours (dynuser, date))
# end def is_work_day

def use_work_hours (db, dynuser, period) :
    """ Check if work hours for given dynuser record should be used at
        all in overtime computation. They will not be used if the sum of
        required hours or the sum of overtime is zero (period denotes if
        we want the result for week/month/year).
    """
    overtime   = dynuser.additional_hours
    period_id  = dynuser.overtime_period
    if period_is_weekly (period) :
        overtime = dynuser.supp_weekly_hours
    return bool (dynuser.weekly_hours and overtime and period_id == period.id)
# end def use_work_hours

def work_days (dynuser) :
    """ Work days per week for this user. Returns number of days for
        which a non-zero day_work_hours is defined. This is used for
        overtime and additional time computation: We need to know the
        ratio for a given day...
    """
    sum   = reduce (add, (bool (dynuser ['hours_' + f]) for f in wdays))
    return sum or 5
# end def work_days

def round_daily_work_hours (hours) :
    """ Rounding of daily work hours.
        >>> round_daily_work_hours (38.5 / 5)
        7.75
    """
    return int (hours * 4. + .5) / 4.
# end def round_daily_work_hours

def travel_worktime (full_hours, half_hours, daily_hours) :
    """Compute the time taking halved travel into account. Return a
       tuple consisting of the travel work-time and the ratio by which
       the work-time was reduced.
    
       >>> travel_worktime ( 8,  4, 8)
       (8, 1.0)
       >>> travel_worktime (12,  6, 8)
       (8, 0.66666666666666663)
       >>> travel_worktime (12,  9, 8)
       (9, 0.5)
       >>> travel_worktime (16,  8, 8)
       (8, 0.5)
       >>> travel_worktime (18,  9, 8)
       (9, 0.5)
       >>> travel_worktime (18, 11, 8)
       (11, 0.5)
       >>> travel_worktime (18, 11, 0)
       (11, 0.5)
       >>> travel_worktime ( 2,  1, 0)
       (1, 0.5)
    """
    ret     = min (full_hours, daily_hours)
    travel  = (full_hours - half_hours) * 2.
    if half_hours > daily_hours :
        ret = half_hours
    if travel :
        ratio = (travel - (full_hours - ret)) / travel
    else :
        ratio = 1.0
    return ret, ratio
# end def travel_worktime

def update_tr_duration (db, dr)  :
    """Compute duration including travel for the given daily record.
       The dr must be the node from the db not just the id.
       Travel time records will have their tr_duration field updated.
    """
    if dr.tr_duration_ok is not None :
        return dr.tr_duration_ok
    hours   = 0.0
    hhours  = 0.0
    dyn     = get_user_dynamic (db, dr.user, dr.date) 
    tr_full = True
    wh      = 0
    if dyn :
        tr_full = dyn.travel_full
        wh      = round_daily_work_hours (day_work_hours (dyn, dr.date))
    trs     = []
    trvl_tr = {}
    for t in dr.time_record :
        tr     = db.time_record.getnode (t)
        trs.append (tr)
        hours += tr.duration
        act    = tr.time_activity
        travel = not tr_full and act and db.time_activity.get (act, 'travel')
        if travel :
            hhours  += tr.duration / 2.
            trvl_tr [tr.id] = tr
        else :
            hhours  += tr.duration
    sum, ratio = travel_worktime (hours, hhours, wh)
    for tr in trs :
        if tr.id in trvl_tr :
            tr_duration = ratio * tr.duration
        else :
            tr_duration = tr.duration
        if tr.tr_duration != tr_duration :
            db.time_record.set (tr.id, tr_duration = tr_duration)
    db.daily_record.set (dr.id, tr_duration_ok = sum)
    return sum
# end def update_tr_duration

daily_record_cache = {}
dr_user_date       = {}

def _update_empty_dr (user, date, next) :
    d = next
    while d <= date :
        daily_record_cache [(user, d.pretty (ymd))] = None
        d = d + day
# end def _update_empty_dr

def get_daily_record (db, user, date) :
    """ Use caching: prefetch all records from given date until now and
        store them. Use a per-user cache of the earliest dr found.
    """
    pdate = date.pretty (ymd)
    date  = Date (pdate)
    now   = Date (Date ('.').pretty (ymd))
    if (user, pdate) not in daily_record_cache :
        if date < now :
            start = date
            end   = now
        else :
            start = now
            end   = date
        if user in dr_user_date :
            s, e = dr_user_date [user]
            assert (start < s or end > e)
            if start > s :
                start = e + day
            if end < e :
                end = s - day
        range = pretty_range (start, end)
        drs = db.daily_record.filter \
            (None, dict (user = user, date = range), sort = ('+', 'date'))
        next = start
        for drid in drs :
            dr = db.daily_record.getnode (drid)
            _update_empty_dr (user, dr.date, next)
            daily_record_cache [(user, dr.date.pretty (ymd))] = dr
            next = dr.date + day
        _update_empty_dr (user, end, next)
    return daily_record_cache [(user, pdate)]
# end def get_daily_record

duration_cache = {}

class Duration (object) :
    def __init__ \
        ( self
        , db
        , dyn               = None
        , tr_duration       = 0
        , day_work_hours    = 0
        , supp_weekly_hours = 0
        , additional_hours  = 0
        , dr_status         = None
        , require_overtime  = None
        , supp_per_period   = 0
        ) :
        self.db                = db
        self.dyn               = dyn
        self.tr_duration       = tr_duration
        self.day_work_hours    = day_work_hours
        self.supp_weekly_hours = supp_weekly_hours
        self.additional_hours  = additional_hours
        self.dr_status         = dr_status
        self.require_overtime  = require_overtime
        self.supp_per_period   = supp_per_period
        if dyn :
            self.supp_per_period = dyn.supp_per_period
    # end def __init__
# end class Duration

def durations (db, user, date) :
    pdate = date.pretty (ymd)
    if (user, pdate) not in duration_cache :
        wday  = gmtime (date.timestamp ())[6]
        dyn   = get_user_dynamic (db, user, date)
        if dyn :
            dc = duration_cache [(user, pdate)] = Duration \
                ( db, dyn
                , day_work_hours    = day_work_hours (dyn, date)
                , supp_weekly_hours = \
                    (dyn.supp_weekly_hours or 0) * is_work_day (dyn, date)
                    / work_days (dyn)
                , additional_hours  = \
                    (dyn.additional_hours  or 0) * is_work_day (dyn, date)
                    / work_days (dyn)
                )
            dr = get_daily_record (db, user, date)
            if dr :
                dc.tr_duration      = update_tr_duration (db, dr)
                dc.dr_status        = dr.status
                dc.require_overtime = dr.required_overtime
        else :
            duration_cache [(user, pdate)] = Duration (db)
    return duration_cache [(user, pdate)]
# end def durations

class Period_Data (object) :
    def __init__ (self, db, user, start, end, end_ov, period) :
        use_additional = not period_is_weekly (period)
        overtime       = 0
        required       = 0
        worked         = 0
        compute        = False
        date           = start
        over_per       = 0
        days           = 0.0
        while date <= end_ov :
            dur       = durations (db, user, date)
            over_per += (use_additional and dur.supp_per_period) or 0
            days     += 1
            work      = dur.tr_duration
            req       = dur.day_work_hours
            over      = dur.supp_weekly_hours
            do_over   = use_work_hours (db, dur.dyn, period)
            if date > end :
                work  = 0
                req   = 0
            if use_additional :
                over    = dur.additional_hours
            overtime += over * do_over
            required += req  * do_over
            worked   += work * do_over
            compute   = compute or do_over
            date += day
        assert (days)
        self.overtime_per_period = over_per / days
        self.achieved_supp       = 0
        if worked > overtime and use_additional :
            self.achieved_supp = \
                max (worked - overtime, self.overtime_per_period)
        overtime += self.overtime_per_period
        if worked > overtime :
            self.overtime_balance = worked - overtime
        elif worked < required :
            self.overtime_balance = worked - required
        else :
            self.overtime_balance = 0
    # end def __init__
# end class Period_Data

def invalidate_cache (user, date) :
    pdate = date.pretty (ymd)
    if (user, pdate) in duration_cache :
        del duration_cache [(user, pdate)]
# end def invalidate_cache

def overtime_periods (db, user, start, end) :
    periods = {}
    if start > end :
        return periods
    dyn = first_user_dynamic (db, user, date = start)
    while (dyn and dyn.valid_from <= end) :
        if dyn.overtime_period :
            ot = db.overtime_period.getnode (dyn.overtime_period)
            periods [ot.name] = ot
        dyn = next_user_dynamic (db, dyn)
    return periods
# end def overtime_periods

def compute_saved_balance \
    (db, user, start, date, is_monthly, not_after = False) :
    """ Compute the saved overtime balance before or at the given day
        and the date on which this balance is valid.
        
        This looks through saved values in freeze records and determines
        a matching freeze record and returns the value for the given
        weekly/monthly period.

        If not_after is True, we use the next end of period for
        searching for existing freeze records. This is used for
        freezing: we don't want to find records at the freeze date.

        Implementation note: we search for freeze records before the end
        of period one day *after* date. This is exactly the same end of
        period as for date in the usual case. In case date *is* the end
        of period, this will include freeze records with freeze_date ==
        date.
    """
    period = None
    periods = sorted \
        ( overtime_periods (db, user, start, date).itervalues ()
        , key = lambda p : p.months
        )
    try :
        if is_monthly :
            period = periods [-1]
            if not period.months :
                period = None
        else :
            period = periods [0]
            if period.months :
                period = None
    except IndexError :
        pass
    eop = date
    if period and not not_after :
        eop = end_of_period (date + day, period)
    r = find_prev_dr_freeze (db, user, eop)
    if r :
        if is_monthly :
            return r.month_balance, r.month_validity_date
        return r.week_balance, freeze_date (r.date, period_week)
    return 0.0, None
# end def compute_saved_balance

def compute_running_balance (db, user, start, date, period, sharp_end = False) :
    """ Compute the overtime balance at the given date.
        if not_after is True, we use the next end of period for
        searching for existing freeze records.

        If sharp_end is True, we compute the exact balance on that day,
        not on the end of previous period.

        If not_after is True, we use the next end of period for
        searching for existing freeze records. This is used for
        freezing: we don't want to find records at the freeze date.
    """
    c_end = end = freeze_date (date, period)
    if sharp_end :
        c_end = date
    p_date    = start
    p_balance = 0

    corr = db.overtime_correction.filter \
        (None, dict (user = user, date = pretty_range (p_date, c_end)))
    for c in corr :
        oc  = db.overtime_correction.getnode (c)
        dyn = get_user_dynamic (db, user, oc.date)
        if dyn and use_work_hours (db, dyn, period) :
            p_balance += oc.value or 0
    while p_date < end :
        eop = end_of_period (p_date, period)
        pd  = Period_Data (db, user, p_date, eop, eop, period)
        p_balance += pd.overtime_balance
        #print "OTB:", pd.overtime_balance
        p_date = eop + day
    print p_date, end
    assert (p_date >= end + day and p_date <= date)
    eop = end_of_period (date, period)
    if sharp_end and date != eop :
        pd = Period_Data (db, user, p_date, date, eop, period)
        p_balance += pd.overtime_balance
        #print "OTBSE:", pd.overtime_balance
    return p_balance
# end def compute_running_balance

def compute_balance \
    (db, user, date, is_monthly, sharp_end = False, not_after = False) :
    """ Compute the overtime balance at the given day.
        if not_after is True, we use the next end of period for
        searching for existing freeze records.

        If sharp_end is True, we compute the exact balance on that day,
        not on the end of previous period.

        If not_after is True, we use the next end of period for
        searching for existing freeze records. This is used for
        freezing: we don't want to find records at the freeze date.
    """
    dyn   = first_user_dynamic (db, user)
    if dyn :
        start = dyn.valid_from
    else :
        start = date + day
    print "START:", start,
    balance, n_start = compute_saved_balance \
        (db, user, start, date, is_monthly, not_after)
    #print "SAVED:", date.pretty (ymd), is_monthly, balance, n_start
    if n_start :
        start = n_start + day # start after freeze date
    print "START:", start, "date:", date
    periods = overtime_periods (db, user, start, date)
    for p in periods.itervalues () :
        if (is_monthly and p.months) or (not is_monthly and not p.months) :
            rb = compute_running_balance \
                (db, user, start, date, p, sharp_end)
            print "PERIOD", p.name, rb
            balance += rb
    return balance
# end compute_balance
