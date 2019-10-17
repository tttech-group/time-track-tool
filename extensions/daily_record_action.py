#! /usr/bin/python
# -*- coding: iso-8859-1 -*-
# Copyright (C) 2006-13 Dr. Ralf Schlatterbeck Open Source Consulting.
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
from urllib                         import quote as urlquote

from rsclib.autosuper               import autosuper

from roundup.cgi.actions            import Action, EditItemAction, SearchAction
from roundup.cgi.exceptions         import Redirect
from roundup.exceptions             import Reject
from roundup.cgi                    import templating
from roundup.date                   import Date, Interval, Range
from roundup                        import hyperdb
from roundup.cgi.TranslationService import get_translation

import common
import freeze
import rup_utils
import user_dynamic
import vacation

_ = lambda x : x

def prev_week (db, request) :
    try :
        db  = db._db
    except AttributeError :
        pass
    start, end = common.date_range (db, request.filterspec)
    n_end   = start - Interval ('1d')
    n_start = n_end - Interval ('6d')
    date    = common.pretty_range (n_start, n_end)
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
    start, end = common.date_range (db, request.filterspec)
    n_start = end     + Interval ('1d')
    n_end   = n_start + Interval ('6d')
    date    = common.pretty_range (n_start, n_end)
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
    if not date :
        return ''
    db = db._db
    try :
        _ = db._
    except AttributeError :
        pass
    supervisor = db.user.get (user,       'supervisor')
    if not supervisor :
        return ''
    clearance  = db.user.get (supervisor, 'clearance_by') or supervisor
    clearer    = db.user.getnode (clearance)
    nickname   = (clearer.nickname or '').upper () or clearer.username
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
    if not date :
        return ''
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

def freeze_user_script () :
     return \
        '''javascript:if(submit_once()){
            document.forms.itemSynopsis ['@action'].value = 'freeze_user';
            document.itemSynopsis.submit ();
           }
        '''
# end def freeze_user_script

def time_url (request, classname) :
    url = 'daily_record?:action=daily_record_action&:template=edit'
    if  (   classname == 'daily_record'
        and request.template not in ('approve', 'edit')
        ) :
        url = str \
            ( request.indexargs_url 
              (classname, {'@action':'daily_record_action', '@template':'edit'})
            )
    # double encode (!)
    enc_url = urlquote (url)
    return \
        """javascript:if(submit_once()){
             location.href = '%(enc_url)s'
           }
        """ % locals ()
# end def time_url

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
        start, end      = common.date_range (self.db, filterspec)
        self.start      = start
        self.end        = end
        max             = start + Interval ('31d')
        if end > max :
            msg = \
                ( "Error: Interval may not exceed one month: %s"
                % ' to '.join ([i.pretty (common.ymd) for i in (start, end)])
                )
            end = max
            request.filterspec ['date'] = common.pretty_range (start, end)
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
        if 'user' in filterspec :
            self.user = filterspec ['user'][0]
        else :
            self.user = self.db.getuid ()
        vacation.create_daily_recs (self.db, self.user, start, end)
        self.db.commit ()
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
            f_supervisor = self._ ('supervisor')
            user      = self.user
            msg       = self._ ("No %(f_supervisor)s for %(user)s") % locals ()
            url       = 'index?:error_message=' + msg 
            raise Redirect, url

        self.create_daily_records ()
        self.request.filterspec = \
            { 'date' : common.pretty_range (self.start, self.end)
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
            { 'date' : common.pretty_range (self.start, self.end)
            , 'user' : [self.user]
            }
        # insert into form for new request objects
        self.request.form ['date'].value = self.request.filterspec ['date']
        self.request.form ['user'].value = self.request.filterspec ['user'][0]
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
        filterspec ['date'] = common.pretty_range \
            (* common.from_week_number (year, weekno))
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
            fdate = db.daily_record_freeze.get (last_frozen [0], 'date') \
                  + common.day
            find_user ['date'] = fdate.pretty ('%Y-%m-%d;')
        dr_per_user = db.daily_record.filter (None, find_user)
        pending [u] = {}
        if dr_per_user :
            earliest = latest = None
            for p in dr_per_user :
                date = db.daily_record.get (p, 'date')
                week, year = common.weekno_year_from_day (date)
                if not earliest or date < earliest :
                    earliest = date
                if not latest   or date > latest :
                    latest   = date
                start, end = common.week_from_date (date)
                if fdate and start < fdate :
                    start = fdate
                filter ['date'] = common.pretty_range (start, end)
                filter ['user'] = u
                pending [u][(year, week)] = \
                    [ None
                    , request.indexargs_url ('', editdict)
                    , 'todo'
                    ]
            interval = latest - earliest
            for k in pending [u].iterkeys () :
                if interval < Interval ('31d') :
                    filter ['date'] = common.pretty_range (earliest, latest)
                    pending [u][k][0] = request.indexargs_url ('', editdict)
                else :
                    pending [u][k][0] = pending [u][k][1]
        else :
            dyn = user_dynamic.last_user_dynamic (db, u)
            if not dyn :
                print u, "no dyn"
            if dyn and (not dyn.valid_to or not fdate or dyn.valid_to > fdate) :
                date = now
                if dyn.valid_to and dyn.valid_to < date :
                    date = dyn.valid_to
                week, year = common.weekno_year_from_day (date)
                start, end = common.week_from_date (date)
                if fdate and start < fdate :
                    start = fdate
                if dyn.valid_to and dyn.valid_to < end :
                    end   = dyn.valid_to
                filter ['date'] = common.pretty_range (start, end)
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
    start, end = common.week_from_date (db.daily_record.get (drid, 'date'))
    user       = db.daily_record.get (drid, 'user')
    d   = start
    sum = 0.
    while d <= end :
        dr   = db.daily_record.filter \
            (None, dict (date = common.pretty_range (d, d), user = user))
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

def dynuser_copyurl (dyn) :
    db  = dyn._db
    dyn = dyn._klass.getnode (dyn._nodeid)
    fields = user_dynamic.dynuser_copyfields
    url = 'user_dynamic?:template=item&' + '&'.join \
        ('%s=%s' % (n, urlquote (str (dyn [n] or ''))) for n in fields)
    if _dynuser_half_frozen (db, dyn.user, dyn.valid_from, dyn.valid_to) :
        fr = freeze.frozen (db, dyn.user, dyn.valid_from) [0]
        fr = db.daily_record_freeze.get (fr, 'date') + common.day
        url += '&valid_from=%s' % fr.pretty (common.ymd)
    return url
# end def dynuser_copyurl

def _dynuser_half_frozen (db, userid, val_from, val_to) :
    return \
        (   freeze.frozen (db, userid, val_from)
        and (   val_to
            and not freeze.frozen (db, userid, val_to - common.day)
            or  not val_to
            )
        )
# end def _dynuser_half_frozen

def dynuser_half_frozen (dyn) :
    db       = dyn._db
    userid   = dyn.user.id
    val_from = Date (str (dyn.valid_from._value))
    val_to   = dyn.valid_to._value
    if val_to :
        val_to = Date (str (val_to))
    return _dynuser_half_frozen (db, userid, val_from, val_to - common.day)
# end def dynuser_half_frozen

def dynuser_frozen (dyn) :
    db       = dyn._db
    userid   = dyn.user.id
    val_to   = str (dyn.valid_to._value)
    if not val_to :
        return False
    val_to   = Date (val_to)
    return freeze.frozen (db, userid, val_to)
# end def dynuser_frozen

class Freeze_Action (Action, autosuper) :

    user_required_msg = ''"User is required"
    user_invalid_msg  = ''"Invalid User"
    def get_user (self) :
        self.request = templating.HTMLRequest (self.client)
        user         = self.request.form ['user'].value
        if not user :
            raise Reject, self._ (self.user_required_msg)
        try :
            self.user = self.db.user.lookup (user)
        except KeyError :
            raise Reject, self._ (self.user_invalid_msg)
        return self.user
    # end def get_user

    def handle (self) :
        if not self.request.form ['date'].value :
            raise Reject, self._ ("Date is required")
        self.date  = Date (self.request.form ['date'].value)
        msg = []
        for u in self.users :
            date = self.date
            dyn  = user_dynamic.get_user_dynamic (self.db, u, date)
            if not dyn :
                dyn = user_dynamic.find_user_dynamic \
                    (self.db, u, date, direction = '-')
                if dyn :
                    # there must be a valid_to date, otherwise
                    # get_user_dynamic would have found something above
                    date = dyn.valid_to - common.day
                    assert (date < self.date)
            if dyn :
                try :
                    self.db.daily_record_freeze.create \
                        (date = date, user = u, frozen = 1)
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
            + ':columns=id,date,user,frozen,balance,validity_date'
            + '&:sort=user,date&:filter=creation'
            + '&:pagesize=200&:startwith=0&creation=%s%%3B'
            ) % (Date ('.') - Interval ('00:05'))
        raise Redirect, url
    # end def handle
# end class Freeze_Action

class Freeze_All_Action (Freeze_Action) :
    def handle (self) :
        self.request = templating.HTMLRequest (self.client)
        if 'user' in self.request.form and self.request.form ['user'].value :
            raise Reject, self._ ('''Don't specify a user for "Freeze all"''')
        self.users   = self.db.user.getnodeids ()
        return self.__super.handle ()
    # end def handle
# end class Freeze_All_Action

class Freeze_User_Action (Freeze_Action) :
    def handle (self) :
        self.users = [self.get_user ()]
        return self.__super.handle ()
    # end def handle
# end class Freeze_User_Action

class Freeze_Supervisor_Action (Freeze_Action) :
    user_required_msg = ''"Supervisor (in User field) is required"
    user_invalid_msg  = ''"Invalid Supervisor"
    def handle (self) :
        self.get_user ()
        self.users = self.db.user.filter (None, dict (supervisor = self.user))
        return self.__super.handle ()
    # end def handle
# end class Freeze_Supervisor_Action

class Split_Dynamic_User_Action (Action) :
    """ Get date of last freeze-record and split dynamic user record
        around the freeze date. A precondition is that the dyn user
        record is half-frozen, i.e., the valid_from is frozen and the
        valid_to is not (or valid_to is None).
        This is no longer in use, since it closes the existing record
        first before creating a new one. Instead we now display only the
        'New dynamic user' link with a valid_from = frozen date if the
        record is half-frozen.
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
        perm     = self.db.security.hasPermission
        if not common.user_has_role (self.db, self.db.getuid (), 'HR') :
            raise Reject, "Not allowed"
        fields   = user_dynamic.dynuser_copyfields + ['valid_to']
        param    = dict ((i, dyn [i]) for i in fields)
        if dyn.valid_to :
            date = common.pretty_range \
                (dyn.valid_from, dyn.valid_to - common.day)
        else :
            date = dyn.valid_from.pretty (common.ymd) + ';'
        
        frozen   = self.db.daily_record_freeze.filter \
            ( None
            , dict (user = dyn.user, date = date, frozen = True)
            , group = [('-', 'date')]
            )
        assert (frozen)
        frozen               = self.db.daily_record_freeze.getnode (frozen [0])
        splitdate            = frozen.date + common.day
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

    def fakeFilterVars (self) :
        """ Fix search-strings for lookalike-computation: run
            search-strings from the form through translate
        """
        SearchAction.fakeFilterVars (self)
        cls = self.db.classes [self.classname]
        try :
            fields = self.form ['@filter']
        except KeyError :
            return
        if not isinstance (fields, list) :
            fields = [fields]
        for k in fields :
            key = k.value
            if not key.split ('.') [-1].startswith ('lookalike_') :
                continue
            prop = cls.get_transitive_prop (str (key))
            if not prop or not isinstance(prop, hyperdb.String) :
                continue
            value = self.form [key]
            if not isinstance (value, list) :
                value = [value]
            for v in value :
                v.value = rup_utils.translate (v.value)
    # end def fakeFilterVars
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
    actn ('freeze_user',              Freeze_User_Action)
    actn ('split_dynamic_user',       Split_Dynamic_User_Action)
    actn ('searchwithtemplate',       SearchActionWithTemplate)
    util = instance.registerUtil
    util ('next_week',                next_week)
    util ('prev_week',                prev_week)
    util ("button_submit_to",         button_submit_to)
    util ("button_action",            button_action)
    util ('weekno_year',              common.weekno_year_from_day)
    util ('daysum',                   daysum)
    util ('weeksum',                  weeksum)
    util ("approvals_pending",        approvals_pending)
    util ("is_end_of_week",           is_end_of_week)
    util ("freeze_all_script",        freeze_all_script)
    util ("freeze_supervisor_script", freeze_supervisor_script)
    util ("freeze_user_script",       freeze_user_script)
    util ("frozen",                   freeze.frozen)
    util ("range_frozen",             freeze.range_frozen)
    util ("time_url",                 time_url)
    util ("next_dr_freeze",           freeze.next_dr_freeze)
    util ("prev_dr_freeze",           freeze.prev_dr_freeze)
    util ("week_freeze_date",         common.week_freeze_date)
    util ("dynuser_half_frozen",      dynuser_half_frozen)
    util ("dynuser_frozen",           dynuser_frozen)
    util ("dynuser_copyurl",          dynuser_copyurl)
# end def init
