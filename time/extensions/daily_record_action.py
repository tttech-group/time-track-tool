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

from time                           import gmtime
from copy                           import copy
from operator                       import add

from rsclib.autosuper               import autosuper

from roundup.cgi.actions            import Action, EditItemAction, SearchAction
from roundup.cgi.exceptions         import Redirect
from roundup.exceptions             import Reject
from roundup.cgi                    import templating
from roundup.date                   import Date, Interval, Range
from roundup                        import hyperdb
from roundup.cgi.TranslationService import get_translation

from common                         import pretty_range, freeze_date
from common                         import week_from_date, ymd, date_range
from common                         import weekno_year_from_day
from common                         import from_week_number
from user_dynamic                   import get_user_dynamic, day_work_hours
from user_dynamic                   import round_daily_work_hours, day
from user_dynamic                   import last_user_dynamic
from freeze                         import frozen, range_frozen, next_dr_freeze
from freeze                         import prev_dr_freeze

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
            if(submit_once()) {
              document.forms.edit_daily_record ['date'].value = '%s';
              document.edit_daily_record.submit ();
            }
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
            if(submit_once()) {
              document.forms.edit_daily_record ['date'].value = '%s';
              document.edit_daily_record.submit ();
            }
        ''' % date
# end def next_week

def button_submit_to (db, user, date) :
    """ Create the submit_to button for time tracking submissions. We
        get the supervisor of the user and check if clearance is
        delegated.
    """
    db = db._db
    supervisor = db.user.get (user,       'supervisor')
    clearance  = db.user.get (supervisor, 'clearance_by') or supervisor
    nickname   = db.user.get (clearance,  'nickname').upper ()
    return \
        '''<input type="button" value="%s"
            onClick="
            if(submit_once()) {
                document.forms.edit_daily_record ['@action'].value =
                    'daily_record_submit';
                document.forms.edit_daily_record ['date'].value = '%s';
                document.edit_daily_record.submit ();
            }
            ">
        ''' % (_ ("Submit to %(nickname)s" % locals ()), date)
# end def button_submit_to

def button_action (date, action, value) :
    """ Create a button for time-tracking actions """
    ''"approve", ''"deny", ''"edit again"
    return \
        '''<input type="button" value="%s"
            onClick="
            if(submit_once()) {
                document.forms.edit_daily_record ['@action'].value =
                    'daily_record_%s';
                document.forms.edit_daily_record ['date'].value = '%s'
                document.edit_daily_record.submit ();
            }
            ">
        ''' % (value, action, date)
# end def button_action

def freeze_all_script () :
     return \
        '''javascript:if(submit_once()){
            document.forms.itemSynopsis ['@action'].value = 'freeze_all';
            document.itemSynopsis.submit ();
           }
        '''
# end def freeze_all_script

def freeze_supervisor_script () :
     return \
        '''javascript:if(submit_once()){
            document.forms.itemSynopsis ['@action'].value = 'freeze_supervisor';
            document.itemSynopsis.submit ();
           }
        '''
# end def freeze_supervisor_script

def time_url (request, classname) :
    url = 'daily_record?:action=daily_record_action&:template=edit'
    if  (   classname == 'daily_record'
        and request.template not in ('approve', 'edit')
        ) :
        url = str \
            ( request.indexargs_url 
              (classname, {'@action':'daily_record_action', '@template':'edit'})
            )
    return \
        """javascript:if(submit_once()){
             location.href = '%(url)s'
           }
        """ % locals ()
# end def time_url

def try_create_public_holiday (db, daily_record, date, user) :
    dyn = get_user_dynamic (db, user, date)
    wh  = day_work_hours   (dyn, date)
    if wh :
        loc = db.org_location.get (dyn.org_location, 'location')
        hol = db.public_holiday.filter \
            (None, {'date' : pretty_range (date, date), 'locations' : loc})
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
            comment = '\n'.join ((holiday.name, holiday.description))
            if holiday.is_half :
                wh = wh / 2.
            wh = round_daily_work_hours (wh)
            db.time_record.create \
                ( daily_record  = daily_record
                , duration      = wh
                , wp            = wp
                , comment       = comment
                , work_location = db.work_location.lookup ('off')
                )
# end def try_create_public_holiday

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
                    ( user              = self.user
                    , date              = d
                    , weekend_allowed   = False
                    , required_overtime = False
                    )
                try_create_public_holiday (self.db, x, d, self.user)
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
        uid = self.db.user.lookup (self.user)
        if not self.db.user.get (uid, 'supervisor') :
            f_supervisor = _ ('supervisor')
            user         = self.user
            msg          = _ ("No %(f_supervisor)s for %(user)s") % locals ()
            url          = 'index?:error_message=' + msg 
            raise Redirect, url

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

class Daily_Record_Reopen (Daily_Record_Change_State) :
    def handle (self) :
        self.state_from = self.db.daily_record_status.lookup ('accepted')
        self.state_to   = self.db.daily_record_status.lookup ('open')
        return self.__super.handle ()
    # end def handle
# end class Daily_Record_Reopen

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
    now       = Date ('.')
    for u in userlist :
        find_user   = dict (user = u, status = submitted)
        fdate       = None
        last_frozen = db.daily_record_freeze.filter \
            ( None
            , dict (user = u, date = now.pretty (';%Y-%m-%d'), frozen = True)
            , group = [('-', 'date')]
            )
        if last_frozen :
            fdate = db.daily_record_freeze.get (last_frozen [0], 'date') + day
            find_user ['date'] = fdate.pretty ('%Y-%m-%d;')
        dr_per_user = db.daily_record.filter (None, find_user)
        pending [u] = {}
        if dr_per_user :
            earliest = latest = None
            for p in dr_per_user :
                date = db.daily_record.get (p, 'date')
                week, year = weekno_year_from_day (date)
                if not earliest or date < earliest :
                    earliest = date
                if not latest   or date > latest :
                    latest   = date
                start, end = week_from_date (date)
                if fdate and start < fdate :
                    start = fdate
                filter ['date'] = pretty_range (start, end)
                filter ['user'] = u
                pending [u][(year, week)] = \
                    [ None
                    , request.indexargs_url ('', editdict)
                    , 'todo'
                    ]
            interval = latest - earliest
            for k in pending [u].iterkeys () :
                if interval < Interval ('31d') :
                    filter ['date'] = pretty_range (earliest, latest)
                    pending [u][k][0] = request.indexargs_url ('', editdict)
                else :
                    pending [u][k][0] = pending [u][k][1]
        else :
            dyn = last_user_dynamic (db, u)
            if not dyn :
                print u, "no dyn"
            if dyn and (not dyn.valid_to or not fdate or dyn.valid_to > fdate) :
                date = now
                if dyn.valid_to and dyn.valid_to < date :
                    date = dyn.valid_to
                week, year = weekno_year_from_day (date)
                start, end = week_from_date (date)
                if fdate and start < fdate :
                    start = fdate
                if dyn.valid_to and dyn.valid_to < end :
                    end   = dyn.valid_to
                filter ['date'] = pretty_range (start, end)
                filter ['user'] = u
                url = request.indexargs_url ('', editdict)
                pending [u][(year, week)] = [url, url, 'done']
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
        if len (dr) == 0 :
            d = d + Interval ('1d')
            continue
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

dynuser_copyfields = \
     [ 'user'
     , 'booking_allowed'
     , 'durations_allowed'
     , 'daily_worktime'
     , 'weekend_allowed'
     , 'travel_full'
     , 'vacation_yearly'
     , 'weekly_hours'
     , 'supp_weekly_hours'
     , 'supp_per_period'
     , 'hours_mon'
     , 'hours_tue'
     , 'hours_wed'
     , 'hours_thu'
     , 'hours_fri'
     , 'hours_sat'
     , 'hours_sun'
     , 'org_location'
     , 'department'
     , 'all_in'
     , 'additional_hours'
     , 'overtime_period'
     ]

def dynuser_half_frozen (db, dyn) :
    userid   = dyn.user.id
    val_from = dyn.valid_from._value
    val_to   = dyn.valid_to._value
    return \
        (   frozen (db, userid, val_from)
        and val_to
        and not frozen (db, userid, val_to - day)
        )
# end def dynuser_half_frozen

class Freeze_Action (Action, autosuper) :
    def handle (self) :
        if not self.request.form ['date'].value :
            raise Reject, _ ("Date is required")
        self.date  = Date (request.form ['date'].value)
        msg = []
        for u in self.users :
            dyn = get_user_dynamic (self.db, u, self.date)
            if dyn :
                try :
                    self.db.daily_record_freeze.create \
                        (date = self.date, user = u, frozen = 1)
                except Reject, cause :
                    msg.append ((str (cause), u))
        self.db.commit ()
        if msg :
            msg.sort ()
            old   = None
            o_u   = None
            count = 1
            new_m = []
            msg.append ((None, None))
            for m, u in msg :
                if m == old :
                    count += 1
                else :
                    if old :
                        if count > 1 :
                            new_m.append ('%s (%d)' % (old, count))
                        else :
                            new_m.append \
                                ( '%s (%s)'
                                % (old, self.db.user.get (o_u, 'username'))
                                )
                    count = 1
                    old   = m
                    o_u   = u
            msg = new_m [:10]
            msg = '@ok_message=Warning: ' + '<br>Warning: '.join (msg) + '&'
        else :
            msg = ''
        url = \
            ( 'daily_record_freeze?'
            + msg
            + ':columns=id,date,user,frozen,'
            + 'week_balance,month_balance,year_balance'
            + '&:sort=user,date&:filter=date'
            + '&:pagesize=200&:startwith=0&date=%s'
            ) % self.date
        raise Redirect, url
    # end def handle
# end class Freeze_Action

class Freeze_All_Action (Freeze_Action) :
    def handle (self) :
        self.request = templating.HTMLRequest (self.client)
        self.users   = self.db.user.getnodeids ()
        return self.__super.handle ()
    # end def handle
# end class Freeze_All_Action

class Freeze_Supervisor_Action (Freeze_Action) :
    def handle (self) :
        self.request = templating.HTMLRequest (self.client)
        user         = self.request.form ['user'].value
        if not user :
            raise Reject, _ ("Supervisor (in User field) is required")
        try :
            user   = self.db.user.lookup (user)
        except KeyError :
            raise Reject, _ ("Invalid Supervisor")
        self.users = self.db.user.filter (None, dict (supervisor = user))
        return self.__super.handle ()
    # end def handle
# end class Freeze_Supervisor_Action

class Split_Dynamic_User_Action (Action) :
    """ Get date of last freeze-record and split dynamic user record
        around the freeze date. A precondition is that the dyn user
        record is half-frozen, i.e., the valid_from is frozen and the
        valid_to is not.
    """
    def handle (self) :
        self.request = templating.HTMLRequest (self.client)
        assert \
            (   self.request.classname
            and self.request.classname == 'user_dynamic'
            and self.client.nodeid
            )
        id       = self.client.nodeid
        dyn      = self.db.user_dynamic.getnode (id)
        fields   = dynuser_copyfields + ['valid_to']
        param    = dict ((i, dyn [i]) for i in fields)
        frozen   = self.db.daily_record_freeze.filter \
            ( None
            , dict 
                ( user   = dyn.user
                , date   = pretty_range (dyn.valid_from, dyn.valid_to - day)
                , frozen = True
                )
            , group = [('-', 'date')]
            )
        assert (frozen)
        frozen               = self.db.daily_record_freeze.getnode (frozen [0])
        splitdate            = frozen.date + day
        self.db.user_dynamic.set (id, valid_to = splitdate)
        param ['valid_from'] = splitdate
        newid                = self.db.user_dynamic.create (** param)
        self.db.commit ()
        raise Redirect, 'user_dynamic%s' % newid
    # end def handle
# end class Split_Dynamic_User_Action

class SearchActionWithTemplate(SearchAction):
    def getCurrentURL (self, req) :
        template = self.getFromForm ('template')
        if template and template != 'index' :
            return req.indexargs_url ('', {'@template' : template}) [1:]
        return req.indexargs_url('', {})[1:]
    # end def getCurrentURL
# end class SearchActionWithTemplate

def init (instance) :
    global _
    _   = get_translation \
        (instance.config.TRACKER_LANGUAGE, instance.config.TRACKER_HOME).gettext
    actn = instance.registerAction
    actn ('daily_record_edit_action', Daily_Record_Edit_Action)
    actn ('daily_record_action',      Daily_Record_Action)
    actn ('daily_record_submit',      Daily_Record_Submit)
    actn ('daily_record_approve',     Daily_Record_Approve)
    actn ('daily_record_deny',        Daily_Record_Deny)
    actn ('daily_record_reopen',      Daily_Record_Reopen)
    actn ('weekno_action',            Weekno_Action)
    actn ('freeze_all',               Freeze_All_Action)
    actn ('freeze_supervisor',        Freeze_Supervisor_Action)
    actn ('split_dynamic_user',       Split_Dynamic_User_Action)
    actn ('searchwithtemplate',       SearchActionWithTemplate)
    util = instance.registerUtil
    util ('next_week',                next_week)
    util ('prev_week',                prev_week)
    util ("button_submit_to",         button_submit_to)
    util ("button_action",            button_action)
    util ('weekno_year',              weekno_year_from_day)
    util ('daysum',                   daysum)
    util ('weeksum',                  weeksum)
    util ("approvals_pending",        approvals_pending)
    util ("is_end_of_week",           is_end_of_week)
    util ("freeze_all_script",        freeze_all_script)
    util ("freeze_supervisor_script", freeze_supervisor_script)
    util ("frozen",                   frozen)
    util ("range_frozen",             range_frozen)
    util ("time_url",                 time_url)
    util ("next_dr_freeze",           next_dr_freeze)
    util ("prev_dr_freeze",           prev_dr_freeze)
    util ("freeze_date",              freeze_date)
    util ("dynuser_half_frozen",      dynuser_half_frozen)
    util ("dynuser_copyfields",       dynuser_copyfields)
# end def init
