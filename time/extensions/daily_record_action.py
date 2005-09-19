#! /usr/bin/python
# -*- coding: iso-8859-1 -*-
# Copyright (C) 2005 Dr. Ralf Schlatterbeck Open Source Consulting.
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
#    daily_record_action
#
# Purpose
#
#    Various actions for editing of daily_record (and associated
#    time_record).
#
#    Daily_Record_Action:
#    Create daily records for given week, redirect to edit form.
#
#    Daily_Record_Edit_Action:
#    Edit form for daily records: Remove some form variables if only
#    values generated by hidden attributes are present.
#
#--

import os, sys
from roundup.cgi.actions    import Action, EditItemAction
from roundup.cgi.exceptions import Redirect
from roundup.exceptions     import Reject
from roundup.cgi            import templating
from roundup.date           import Date, Interval, Range
from roundup                import hyperdb
from time                   import gmtime
from copy                   import copy
from operator               import add

week_from_date = None
ymd            = None
pretty_range   = None
class _autosuper (type) :
    def __init__ (cls, name, bases, dict) :
        super   (_autosuper, cls).__init__ (name, bases, dict)
        setattr (cls, "_%s__super" % name, super (cls))
    # end def __init__
# end class _autosuper

class autosuper (object) :
    __metaclass__ = _autosuper
    pass
# end class autosuper

def date_range (db, filterspec) :
    if 'date' in filterspec :
        r = Range (filterspec ['date'], Date)
        if r.to_value is None :
            start = end = r.from_value
        elif r.from_value is None or r.from_value == r.to_value :
            start = end = r.to_value
        else :
            start = r.from_value
            end   = r.to_value
    else :
        date       = Date ('.')
        date       = Date (str (date.local (db.getUserTimezone ())))
        start, end = week_from_date (date)
    start.hours = start.minutes = start.seconds = 0
    end.hours   = end.minutes   = end.seconds   = 0
    return start, end
# end def date_range

def first_thursday (year) :
    """ compute first thursday in the given year as a Date
        >>> first_thursday (1998)
        <Date 1998-01-01.00:00:0.000000>
        >>> first_thursday ("1998")
        <Date 1998-01-01.00:00:0.000000>
        >>> first_thursday (1999)
        <Date 1999-01-07.00:00:0.000000>
        >>> first_thursday (2000)
        <Date 2000-01-06.00:00:0.000000>
        >>> first_thursday (2001)
        <Date 2001-01-04.00:00:0.000000>
        >>> first_thursday (2002)
        <Date 2002-01-03.00:00:0.000000>
        >>> first_thursday (2003)
        <Date 2003-01-02.00:00:0.000000>
        >>> first_thursday (2004)
        <Date 2004-01-01.00:00:0.000000>
        >>> first_thursday (2005)
        <Date 2005-01-06.00:00:0.000000>
        >>> first_thursday (2006)
        <Date 2006-01-05.00:00:0.000000>
        >>> first_thursday (2007)
        <Date 2007-01-04.00:00:0.000000>
        >>> first_thursday (2008)
        <Date 2008-01-03.00:00:0.000000>
        >>> first_thursday (2009)
        <Date 2009-01-01.00:00:0.000000>
        >>> first_thursday (2010)
        <Date 2010-01-07.00:00:0.000000>
        >>> first_thursday (2011)
        <Date 2011-01-06.00:00:0.000000>
        >>> first_thursday (2012)
        <Date 2012-01-05.00:00:0.000000>
        >>> first_thursday (2013)
        <Date 2013-01-03.00:00:0.000000>
        >>> first_thursday (2014)
        <Date 2014-01-02.00:00:0.000000>
        >>> first_thursday (2015)
        <Date 2015-01-01.00:00:0.000000>
        >>> first_thursday (2016)
        <Date 2016-01-07.00:00:0.000000>
        >>> first_thursday (2017)
        <Date 2017-01-05.00:00:0.000000>
        >>> first_thursday (2018)
        <Date 2018-01-04.00:00:0.000000>
        >>> first_thursday (2019)
        <Date 2019-01-03.00:00:0.000000>
        >>> first_thursday (2020)
        <Date 2020-01-02.00:00:0.000000>
        >>> first_thursday (2021)
        <Date 2021-01-07.00:00:0.000000>
    """
    for i in range (1, 8) :
        date = Date ('%s-01-%02d' % (year, i))
        if gmtime (date.timestamp ()) [6] == 3 : # Thursday
            return date
    assert (0)
# end def first_thursday

def from_week_number (year, week_no) :
    """ Get first thursday in year, then add days.
        >>> from_week_number (1998, 52)
        (<Date 1998-12-21.00:00:0.000000>, <Date 1998-12-27.00:00:0.000000>)
        >>> from_week_number (1998, 53)
        (<Date 1998-12-28.00:00:0.000000>, <Date 1999-01-03.00:00:0.000000>)
        >>> from_week_number (1999,  1)
        (<Date 1999-01-04.00:00:0.000000>, <Date 1999-01-10.00:00:0.000000>)
        >>> from_week_number (1999, 52)
        (<Date 1999-12-27.00:00:0.000000>, <Date 2000-01-02.00:00:0.000000>)
        >>> from_week_number (2000,  1)
        (<Date 2000-01-03.00:00:0.000000>, <Date 2000-01-09.00:00:0.000000>)
        >>> from_week_number (2000, 52)
        (<Date 2000-12-25.00:00:0.000000>, <Date 2000-12-31.00:00:0.000000>)
        >>> from_week_number (2001,  1)
        (<Date 2001-01-01.00:00:0.000000>, <Date 2001-01-07.00:00:0.000000>)
        >>> from_week_number (2001, 52)
        (<Date 2001-12-24.00:00:0.000000>, <Date 2001-12-30.00:00:0.000000>)
        >>> from_week_number (2002,  1)
        (<Date 2001-12-31.00:00:0.000000>, <Date 2002-01-06.00:00:0.000000>)
        >>> from_week_number (2002, 52)
        (<Date 2002-12-23.00:00:0.000000>, <Date 2002-12-29.00:00:0.000000>)
        >>> from_week_number (2003,  1)
        (<Date 2002-12-30.00:00:0.000000>, <Date 2003-01-05.00:00:0.000000>)
        >>> from_week_number (2003, 52)
        (<Date 2003-12-22.00:00:0.000000>, <Date 2003-12-28.00:00:0.000000>)
        >>> from_week_number (2004,  1)
        (<Date 2003-12-29.00:00:0.000000>, <Date 2004-01-04.00:00:0.000000>)
        >>> from_week_number (2004, 52)
        (<Date 2004-12-20.00:00:0.000000>, <Date 2004-12-26.00:00:0.000000>)
        >>> from_week_number (2004, 53)
        (<Date 2004-12-27.00:00:0.000000>, <Date 2005-01-02.00:00:0.000000>)
        >>> from_week_number (2005,  1)
        (<Date 2005-01-03.00:00:0.000000>, <Date 2005-01-09.00:00:0.000000>)
        >>> from_week_number (2005, 29)
        (<Date 2005-07-18.00:00:0.000000>, <Date 2005-07-24.00:00:0.000000>)
        >>> from_week_number (2005, 52)
        (<Date 2005-12-26.00:00:0.000000>, <Date 2006-01-01.00:00:0.000000>)
        >>> from_week_number (2006,  1)
        (<Date 2006-01-02.00:00:0.000000>, <Date 2006-01-08.00:00:0.000000>)
        >>> from_week_number (2006, 52)
        (<Date 2006-12-25.00:00:0.000000>, <Date 2006-12-31.00:00:0.000000>)
        >>> from_week_number (2007,  1)
        (<Date 2007-01-01.00:00:0.000000>, <Date 2007-01-07.00:00:0.000000>)
        >>> from_week_number (2007, 52)
        (<Date 2007-12-24.00:00:0.000000>, <Date 2007-12-30.00:00:0.000000>)
        >>> from_week_number (2008,  1)
        (<Date 2007-12-31.00:00:0.000000>, <Date 2008-01-06.00:00:0.000000>)
        >>> from_week_number (2008, 52)
        (<Date 2008-12-22.00:00:0.000000>, <Date 2008-12-28.00:00:0.000000>)
        >>> from_week_number (2009,  1)
        (<Date 2008-12-29.00:00:0.000000>, <Date 2009-01-04.00:00:0.000000>)
        >>> from_week_number (2009, 52)
        (<Date 2009-12-21.00:00:0.000000>, <Date 2009-12-27.00:00:0.000000>)
        >>> from_week_number (2009, 53)
        (<Date 2009-12-28.00:00:0.000000>, <Date 2010-01-03.00:00:0.000000>)
        >>> from_week_number (2010,  1)
        (<Date 2010-01-04.00:00:0.000000>, <Date 2010-01-10.00:00:0.000000>)
        >>> from_week_number (2010, 52)
        (<Date 2010-12-27.00:00:0.000000>, <Date 2011-01-02.00:00:0.000000>)
    """
    date = first_thursday (year)
    date = date + Interval ('%dd' % ((week_no - 1) * 7))
    return week_from_date (date)
# end def from_week_number

def weekno_from_day (date) :
    """ Compute the week number from the given date
        >>> weekno_from_day (Date ('2005-08-26'))
        34
        >>> weekno_from_day (Date ("1998-12-21"))
        52
        >>> weekno_from_day (Date ("1998-12-27"))
        52
        >>> weekno_from_day (Date ("1998-12-28"))
        53
        >>> weekno_from_day (Date ("1999-01-03"))
        53
        >>> weekno_from_day (Date ("1999-01-04"))
        1
        >>> weekno_from_day (Date ("1999-01-10"))
        1
        >>> weekno_from_day (Date ("1999-12-27"))
        52
        >>> weekno_from_day (Date ("2000-01-02"))
        52
        >>> weekno_from_day (Date ("2000-01-03"))
        1
        >>> weekno_from_day (Date ("2000-01-09"))
        1
        >>> weekno_from_day (Date ("2000-12-25"))
        52
        >>> weekno_from_day (Date ("2000-12-31"))
        52
        >>> weekno_from_day (Date ("2001-01-01"))
        1
        >>> weekno_from_day (Date ("2001-01-07"))
        1
        >>> weekno_from_day (Date ("2001-12-24"))
        52
        >>> weekno_from_day (Date ("2001-12-30"))
        52
        >>> weekno_from_day (Date ("2001-12-31"))
        1
        >>> weekno_from_day (Date ("2002-01-06"))
        1
        >>> weekno_from_day (Date ("2002-12-23"))
        52
        >>> weekno_from_day (Date ("2002-12-29"))
        52
        >>> weekno_from_day (Date ("2002-12-30"))
        1
        >>> weekno_from_day (Date ("2003-01-05"))
        1
        >>> weekno_from_day (Date ("2003-12-22"))
        52
        >>> weekno_from_day (Date ("2003-12-28"))
        52
        >>> weekno_from_day (Date ("2003-12-29"))
        1
        >>> weekno_from_day (Date ("2004-01-04"))
        1
        >>> weekno_from_day (Date ("2004-12-20"))
        52
        >>> weekno_from_day (Date ("2004-12-26"))
        52
        >>> weekno_from_day (Date ("2004-12-27"))
        53
        >>> weekno_from_day (Date ("2005-01-02"))
        53
        >>> weekno_from_day (Date ("2005-01-03"))
        1
        >>> weekno_from_day (Date ("2005-01-09"))
        1
        >>> weekno_from_day (Date ("2005-07-18"))
        29
        >>> weekno_from_day (Date ("2005-07-24"))
        29
        >>> weekno_from_day (Date ("2005-12-26"))
        52
        >>> weekno_from_day (Date ("2006-01-01"))
        52
        >>> weekno_from_day (Date ("2006-01-02"))
        1
        >>> weekno_from_day (Date ("2006-01-08"))
        1
        >>> weekno_from_day (Date ("2006-12-25"))
        52
        >>> weekno_from_day (Date ("2006-12-31"))
        52
        >>> weekno_from_day (Date ("2007-01-01"))
        1
        >>> weekno_from_day (Date ("2007-01-07"))
        1
        >>> weekno_from_day (Date ("2007-12-24"))
        52
        >>> weekno_from_day (Date ("2007-12-30"))
        52
        >>> weekno_from_day (Date ("2007-12-31"))
        1
        >>> weekno_from_day (Date ("2008-01-06"))
        1
        >>> weekno_from_day (Date ("2008-12-22"))
        52
        >>> weekno_from_day (Date ("2008-12-28"))
        52
        >>> weekno_from_day (Date ("2008-12-29"))
        1
        >>> weekno_from_day (Date ("2009-01-04"))
        1
        >>> weekno_from_day (Date ("2009-12-21"))
        52
        >>> weekno_from_day (Date ("2009-12-27"))
        52
        >>> weekno_from_day (Date ("2009-12-28"))
        53
        >>> weekno_from_day (Date ("2010-01-03"))
        53
        >>> weekno_from_day (Date ("2010-01-04"))
        1
        >>> weekno_from_day (Date ("2010-01-10"))
        1
        >>> weekno_from_day (Date ("2010-12-27"))
        52
        >>> weekno_from_day (Date ("2011-01-02"))
        52
    """
    date   = Date (str (date))
    wday   = gmtime (date.timestamp ())[6]
    date   = date + Interval ('%dd' % (3 - wday)) # Thursday that week
    yday2  = gmtime (date.timestamp ())[7]
    d      = first_thursday (date.year)
    yday1  = gmtime (d.timestamp    ())[7]
    assert ((yday2 - yday1) % 7 == 0)
    return int ((yday2 - yday1) / 7 + 1)
# end def weekno_from_day

def prev_week (db, request) :
    try :
        db  = db._db
    except AttributeError :
        pass
    start, end = date_range (db, request.filterspec)
    n_end   = start - Interval ('1d')
    n_start = n_end - Interval ('6d')
    date    = pretty_range (n_start, n_end)
    return \
        '''javascript:
            document.forms.edit_daily_record ['date'].value = '%s';
            document.edit_daily_record.submit ();
        ''' % date
# end def prev_week

def next_week (db, request) :
    try :
        db  = db._db
    except AttributeError :
        pass
    start, end = date_range (db, request.filterspec)
    n_start = end     + Interval ('1d')
    n_end   = n_start + Interval ('6d')
    date    = pretty_range (n_start, n_end)
    return \
        '''javascript:
            document.forms.edit_daily_record ['date'].value = '%s';
            document.edit_daily_record.submit ();
        ''' % date
# end def next_week

class Daily_Record_Common (Action, autosuper) :
    """ Methods for creation of daily records that do not yet exist """

    permissionType = 'View'

    def set_request (self) :
        """ figure the request """
        if not hasattr (self, 'request') :
            self.request = templating.HTMLRequest (self.client)
    # end def set_request

    def create_daily_records (self) :
        self.set_request ()
        request         = self.request
        filterspec      = request.filterspec
        columns         = request.columns
        assert (request.classname == 'daily_record')
        start, end      = date_range (self.db, filterspec)
        self.start      = start
        self.end        = end
        max             = start + Interval ('31d')
        if end > max :
            msg = \
                ( "Error: Interval may not exceed one month: %s"
                % ' to '.join ([i.pretty (ymd) for i in (start, end)])
                )
            end = max
            request.filterspec ['date'] = pretty_range (start, end)
            url = request.indexargs_url \
                ( ''
                , { ':action'        : 'search'
                  , ':template'      : 'edit'
                  , ':sort'          : 'date'
                  , ':group'         : 'user'
                  , ':filter'        : ','.join (request.filterspec.keys ())
                  , ':startwith'     : '0'
                  , ':error_message' : msg
                  }
                )
            raise Redirect, url
        d = start
        if 'user' in filterspec :
            self.user = filterspec ['user'][0]
        else :
            self.user = self.db.getuid ()
        while d <= end :
            try :
                x = self.db.daily_record.create \
                    ( user = self.user
                    , date = d
                    )
                self.db.commit ()
            except Reject :
                pass
            d = d + Interval ('1d')
    # end def create_daily_records

# end class Daily_Record_Common

class Daily_Record_Action (Daily_Record_Common) :
    """ Move to the given date range for the given user after creating
        the daily records for the given range.
        Note: No editing is performed.
    """

    name           = 'daily_record_action'

    def handle (self) :
        self.create_daily_records ()
        self.request.filterspec = \
            { 'date' : pretty_range (self.start, self.end)
            , 'user' : [self.user]
            }
        url = self.request.indexargs_url \
            ( ''
            , { ':action'    : 'search'
              , ':template'  : 'edit'
              , ':sort'      : 'date'
              , ':group'     : 'user'
              , ':startwith' : '0'
              , ':filter'    : ','.join (self.request.filterspec.keys ())
              }
            )
        raise Redirect, url
    # end def handle

# end class Daily_Record_Action

class Daily_Record_Edit_Action (EditItemAction, Daily_Record_Common) :
    """ Remove items that did not change (for which we defined a hidden
        attribute in the mask) from the new items. Then proceed as usual
        like for EditItemAction. The filterspec is modified from the
        date input field before doing the editing, so after editing we
        move to the new selection.
    """

    name           = 'daily_record_edit_action'
    permissionType = 'Edit'

    def _editnodes (self, props, links) :
        # use props.items here, with iteritems we get a RuntimeError
        # "dictionary changed size during iteration"
        for (cl, id), val in props.items () :
            if cl == 'time_record' :
                if int (id) < 0 and val.keys () == ['daily_record'] :
                    del props [(cl, id)]
        self.ok_msg = EditItemAction._editnodes (self, props, links)
        return self.ok_msg
    # end def _editnodes

    def handle (self) :
        self.create_daily_records ()
        self.request.filterspec = \
            { 'date' : pretty_range (self.start, self.end)
            , 'user' : [self.user]
            }
        # returns only in error case
        return self.__super.handle ()
    # end def handle

# end class Daily_Record_Edit_Action

class Weekno_Action (Daily_Record_Edit_Action) :
    """ Parse the weekno field and move to the given week instead of to
        the range given in the date attribute after editing.
    """

    name = 'weekno_action'

    def handle (self) :
        self.set_request ()
        filterspec   = self.request.filterspec
        try :
            weeknostr = filterspec ['weekno']
        except KeyError :
            weeknostr = self.request.form ['weekno'].value
        try :
            year, weekno = [int (i) for i in weeknostr.split ('/')]
        except ValueError :
            year = Date ('.').year
            weekno = int (weeknostr)
        filterspec ['date'] = pretty_range (* from_week_number (year, weekno))
        try :
            return self.__super.handle ()
        except Redirect :
            pass
        args = \
            { ':action'        : 'search'
            , ':template'      : 'edit'
            , ':sort'          : 'date'
            , ':group'         : 'user'
            , ':filter'        : ','.join (self.request.filterspec.keys ())
            , ':startwith'     : '0'
            , ':ok_message'    : self.ok_msg
            }
        url = self.request.indexargs_url ('', args)
        raise Redirect, url
    # end def handle
# end class Weekno_Action

class Daily_Record_Change_State (Daily_Record_Edit_Action) :
    """ Handle editing. If everything is OK, try to change state for the
        current selection, otherwise display error messages from the
        edit.  If the state change creates errors they are shown.
        Otherwise move to the *current* selection.
    """

    def handle (self) :
        try :
            # returns only in case of error
            return self.__super.handle ()
        except Redirect :
            pass
        # figure the request
        request    = self.request
        sort       = request.sort
        group      = request.group
        klass      = self.db.getclass (request.classname)
        msg        = []
        for itemid in klass.filter (None, request.filterspec, sort, group) :
            try :
                if klass.get (itemid, 'status') == self.state_from :
                    klass.set (itemid, status = self.state_to)
            except Reject, cause :
                msg.append (str (cause).replace ("\n", "<br>"))
        args = \
            { ':action'        : 'search'
            , ':template'      : 'edit'
            , ':sort'          : 'date'
            , ':group'         : 'user'
            , ':filter'        : ','.join (request.filterspec.keys ())
            , ':startwith'     : '0'
            }
        if msg :
            self.db.rollback ()
            args [':error_message'] = "<br>".join (msg)
        else :
            args [':ok_message']    = self.ok_msg
            self.db.commit ()
        url = request.indexargs_url ('', args)
        raise Redirect, url
    # end def handle
# end class Daily_Record_Change_State

class Daily_Record_Submit (Daily_Record_Change_State) :
    def handle (self) :
        self.state_from = self.db.daily_record_status.lookup ('open')
        self.state_to   = self.db.daily_record_status.lookup ('submitted')
        return self.__super.handle ()
    # end def handle
# end class Daily_Record_Submit

class Daily_Record_Approve (Daily_Record_Change_State) :
    def handle (self) :
        self.state_from = self.db.daily_record_status.lookup ('submitted')
        self.state_to   = self.db.daily_record_status.lookup ('accepted')
        return self.__super.handle ()
    # end def handle
# end class Daily_Record_Approve

class Daily_Record_Deny (Daily_Record_Change_State) :
    def handle (self) :
        self.state_from = self.db.daily_record_status.lookup ('submitted')
        self.state_to   = self.db.daily_record_status.lookup ('open')
        return self.__super.handle ()
    # end def handle
# end class Daily_Record_Deny

def approvals_pending (db, request, userlist) :
    try :
        db  = db._db
    except AttributeError :
        pass
    pending   = {}
    submitted = db.daily_record_status.lookup ('submitted')
    spec      = copy (request.filterspec)
    filter    = request.filterspec
    editdict  = {':template' : 'edit', ':filter' : 'user,date'}
    for u in userlist :
        p_user = db.daily_record.find (user = u, status = submitted)
        if p_user :
            pending [u] = {}
            earliest = latest = None
            for p in p_user :
                date = db.daily_record.get (p, 'date')
                week = int (weekno_from_day (date))
                if not earliest or date < earliest :
                    earliest = date
                if not latest   or date > latest :
                    latest   = date
                filter ['date'] = pretty_range (* week_from_date (date))
                filter ['user'] = u
                pending [u][week] = \
                    [ None
                    , request.indexargs_url ('', editdict)
                    ]
            interval = latest - earliest
            for k in pending [u].iterkeys () :
                if interval < Interval ('31d') :
                    filter ['date'] = pretty_range (earliest, latest)
                    pending [u][k][0] = request.indexargs_url ('', editdict)
                else :
                    pending [u][k][0] = pending [u][k][1]
    request.filterspec = spec
    return pending
# end def approvals_pending

def daysum (db, daily_record, format = None) :
    tr  = db.daily_record.get (daily_record, 'time_record')
    val =  reduce (add, [db.time_record.get (i, 'duration') for i in tr], 0)
    if format :
        return format % val
    return val
# end def daysum

def weeksum (db, drid, format = None) :
    start, end = week_from_date (db.daily_record.get (drid, 'date'))
    user       = db.daily_record.get (drid, 'user')
    d   = start
    sum = 0.
    while d <= end :
        dr   = db.daily_record.filter \
            (None, dict (date = pretty_range (d, d), user = user))
        assert (len (dr) == 1)
        dr   = dr [0]
        sum += daysum (db, dr)
        d    = d + Interval ('1d')
    if format :
        return format % sum
    return sum
# end def weeksum

def is_end_of_week (date) :
    date = Date (str (date))
    wday = gmtime (date.timestamp ())[6]
    return wday == 6
# end def is_end_of_week

def init (instance) :
    global pretty_range, week_from_date, ymd
    sys.path.insert (0, os.path.join (instance.config.HOME, 'lib'))
    from common import pretty_range, week_from_date, ymd
    del sys.path [0]
    actn = instance.registerAction
    actn ('daily_record_edit_action', Daily_Record_Edit_Action)
    actn ('daily_record_action',      Daily_Record_Action)
    actn ('daily_record_submit',      Daily_Record_Submit)
    actn ('daily_record_approve',     Daily_Record_Approve)
    actn ('daily_record_deny',        Daily_Record_Deny)
    actn ('weekno_action',            Weekno_Action)
    util = instance.registerUtil
    util ('next_week',                next_week)
    util ('prev_week',                prev_week)
    util ('weekno',                   weekno_from_day)
    util ('daysum',                   daysum)
    util ('weeksum',                  weeksum)
    util ("approvals_pending",        approvals_pending)
    util ("is_end_of_week",           is_end_of_week)
# end def init
