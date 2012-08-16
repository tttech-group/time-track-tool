# -*- coding: iso-8859-1 -*-
# Copyright (C) 2010 Ralf Schlatterbeck. All rights reserved
# Reichergasse 131, A-3411 Weidling
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

import errno
import os
import shutil
import sys
import unittest
import logging

import user1_time, user2_time, user3_time

from operator import mul

from propl_abo     import properties as properties_abo
from propl_adr     import properties as properties_adr
from propl_erp     import properties as properties_erp
from propl_full    import properties as properties_full
from propl_it      import properties as properties_it
from propl_itadr   import properties as properties_itadr
from propl_kvats   import properties as properties_kvats
from propl_lielas  import properties as properties_lielas
from propl_sfull   import properties as properties_sfull

from sec_abo       import security as security_abo
from sec_adr       import security as security_adr
from sec_erp       import security as security_erp
from sec_full      import security as security_full
from sec_it        import security as security_it
from sec_itadr     import security as security_itadr
from sec_kvats     import security as security_kvats
from sec_lielas    import security as security_lielas
from sec_sfull     import security as security_sfull

from search_abo    import properties as sec_search_abo
from search_adr    import properties as sec_search_adr
from search_erp    import properties as sec_search_erp
from search_full   import properties as sec_search_full
from search_it     import properties as sec_search_it
from search_itadr  import properties as sec_search_itadr
from search_kvats  import properties as sec_search_kvats
from search_lielas import properties as sec_search_lielas
from search_sfull  import properties as sec_search_sfull

from trans_abo     import transprop_perms as transprop_abo
from trans_adr     import transprop_perms as transprop_adr
from trans_erp     import transprop_perms as transprop_erp
from trans_full    import transprop_perms as transprop_full
from trans_itadr   import transprop_perms as transprop_itadr
from trans_kvats   import transprop_perms as transprop_kvats
from trans_lielas  import transprop_perms as transprop_lielas
from trans_sfull   import transprop_perms as transprop_sfull

from trans_search  import classdict  as trans_classprops

from roundup       import instance, configuration, init, password, date
from roundup.cgi   import templating
sys.path.insert (0, os.path.abspath ('lib'))
sys.path.insert (0, os.path.abspath ('extensions'))
from user_dynamic import update_tr_duration, compute_balance
from user_dynamic import overtime_periods, first_user_dynamic, next_user_dynamic
from summary import Staff_Report
from summary import init as summary_init

class _Test_Case (unittest.TestCase) :
    count = 0
    db = None
    roles = ['admin']
    allroles = dict.fromkeys \
        (('abo'
        , 'abo+invoice'
        , 'admin'
        , 'adr_readonly'
        , 'anonymous'
        , 'contact'
        , 'controlling'
        , 'discount'
        , 'doc_admin'
        , 'external'
        , 'guest'
        , 'hr'
        , 'hr-org-location'
        , 'invoice'
        , 'issue_admin'
        , 'it'
        , 'itview'
        , 'letter'
        , 'logger'
        , 'nosy'
        , 'office'
        , 'pgp'
        , 'product'
        , 'project'
        , 'project_view'
        , 'supportadmin'
        , 'type'
        , 'user'
        ))


    def setup_tracker (self, backend = 'postgresql') :
        """ Install and initialize tracker in dirname, return tracker instance.
            If directory exists, it is wiped out before the operation.
        """
        self.__class__.count += 1
        self.dirname = '_test_init_%s' % self.count
        self.backend = 'postgresql'
        self.config  = config = configuration.CoreConfig ()
        config.DATABASE       = 'db'
        config.RDBMS_NAME     = "rounduptestttt"
        config.RDBMS_HOST     = "localhost"
        config.RDBMS_USER     = "rounduptest"
        config.RDBMS_PASSWORD = "rounduptest"
        config.MAIL_DOMAIN    = "your.tracker.email.domain.example"
        config.TRACKER_WEB    = "http://localhost:4711/ttt/"
        config.RDBMS_TEMPLATE = "template0"
        config.init_logging ()
        self.tearDown ()
        srcdir = os.path.join (os.path.dirname (__file__), '..')
        os.mkdir (self.dirname)
        for f in ( 'detectors', 'extensions', 'html', 'initial_data.py'
                 , 'lib', 'locale', 'schema'
                 , 'schemas/%s.py' % self.schemaname
                 , 'TEMPLATE-INFO.txt', 'utils'
                 ) :
            ft = f
            if f.startswith ('schemas') :
                ft = 'schema.py'
            os.symlink \
                ( os.path.abspath (os.path.join (srcdir, f))
                , os.path.join (self.dirname, ft)
                )
        init.write_select_db (self.dirname, self.backend)
        self.config.save (os.path.join (self.dirname, 'config.ini'))
        tracker = instance.open (self.dirname)
        if tracker.exists () :
            tracker.nuke ()
            init.write_select_db (self.dirname, self.backend)
        tracker.init (password.Password (self.config.RDBMS_PASSWORD))
        self.tracker = tracker
    # end def setup_tracker

    def setUp (self) :
        self.log           = logging.getLogger ('roundup.test')
        self.properties    = globals () ['properties_' + self.schemaname]
        self.security_desc = globals () ['security_'   + self.schemaname]
        self.search_desc   = globals () ['sec_search_' + self.schemaname]
        self.setup_tracker ()
    # end def setUp

    def tearDown (self) :
        for k in 'db', 'db1', 'db2' :
            db = getattr (self, k, None)
            if db :
                db.clearCache ()
                db.close ()
        self.db = self.db1 = self.db2 = None
        if os.path.exists (self.dirname) :
            shutil.rmtree (self.dirname)
    # end def tearDown

    def test_0_roles (self) :
        self.log.debug ('test_0_roles')
        self.db = self.tracker.open ('admin')
        roles = list (sorted (self.db.security.role.iterkeys ()))
        self.assertEqual (roles, self.roles)
        for r in roles :
            self.assertEqual (r in self.allroles, True)
    # end def test_0_roles

    def test_1_schema (self) :
        self.log.debug ('test_1_schema')
        self.db = self.tracker.open ('admin')
        classnames = sorted (self.db.getclasses ())
        for (cl, props), cls in zip (self.properties, classnames) :
            self.assertEqual (cl, cls)
            clprops = sorted (self.db.getclass (cls).properties.keys ())
            self.assertEqual (props, clprops)
    # end def test_1_schema

    def test_2_security (self) :
        self.log.debug ('test_2_security')
        self.db = self.tracker.open ('admin')
        secdesc = self.security_desc.split ('\n')
        sd2     = []
        # sorting: python dicts are no longer stable from call to call
        for x in secdesc :
            if '[' in x :
                x0, x1 =  x.split ('[', 1)
                x1, x2 = x1.split (']', 1)
                x1 = ', '.join (sorted (x1.split (', ')))
                x = x0 + '[' + x1 + ']' + x2
            if '": (' in x :
                x0, x1 =  x.split ('": (', 1)
                x1, x2 = x1.split (') only', 1)
                x1 = ', '.join (sorted (x1.split (', ')))
                x = x0 + '": (' + x1 + ') only' + x2
            sd2.append (x)
        secdesc = sd2
        s = []
        s.append (secdesc [0])
        s.append (secdesc [1])
        roles = sorted (list (self.db.security.role.items ()))
        for rolename, role in roles :
            s.append ('Role "%(name)s":' % role.__dict__)
            perms = []
            for permission in role.permissions :
                d = permission.__dict__
                if permission.klass :
                    if permission.properties :
                        p = { 'properties'
                            : type (d ['properties'])
                                   (sorted (d ['properties']))
                            }
                        perms.append \
                            ( ' %(description)s (%(name)s for "%(klass)s"' %d
                            + ': %(properties)s only)' % p
                            )
                    else :
                        perms.append \
                            (' %(description)s (%(name)s for "%(klass)s" only)'
                            % d
                            )
                else:
                    perms.append (' %(description)s (%(name)s)' % d)
            s.extend (sorted (dict.fromkeys (perms).keys ()))
        lr1 = lr2 = None
        for s1, s2 in zip (secdesc, s) :
            if s1.startswith ('Role') :
                lr1 = s1
            if s2.startswith ('Role') :
                lr2 = s2
            self.assertEqual ((lr1, s1), (lr2, s2))
    # end def test_2_security

    def test_3_search (self) :
        self.log.debug ('test_3_search')
        self.db = self.tracker.open ('admin')
        self.create_test_users ()
        classnames = sorted (self.db.getclasses ())
        for (cl, props), cls in zip (self.search_desc, classnames) :
            self.assertEqual (cl, cls)
            clprops = []
            for p in sorted (self.db.getclass (cls).properties.keys ()) :
                users = []
                for user, uid in sorted (self.users.iteritems ()) :
                    if self.db.security.hasSearchPermission (uid, cl, p) :
                        users.append (user)
                clprops.append ((p, users))
            self.assertEqual ((cl, props), (cl, clprops))
    # end def test_3_search

    transprop_perms = []
    def test_4_transprops (self) :
        self.log.debug ('test_4_transprops')
        self.db = self.tracker.open ('admin')
        self.create_test_users ()
        perms = []
        for cl, props in sorted (trans_classprops.iteritems ()) :
            if cl not in self.db.classes :
                continue
            klass = self.db.classes [cl]
            for p in sorted (props) :
                ps = p.split ('.')
                if ps [0] not in klass.getprops () :
                    continue
                pusers = []
                for user, uid in sorted (self.users.iteritems ()) :
                    if self.db.security.hasSearchPermission (uid, cl, p) :
                        pusers.append (user)
                perms.append (('.'.join ((cl, p)), pusers))
        for a, b in zip (self.transprop_perms, perms):
            self.assertEqual (a, b)
        self.assertEqual (len (self.transprop_perms), len (perms))
    # end def test_4_transprops

    def create_test_users (self) :
        nouserroles = \
            [ 'adr_readonly'
            , 'guest'
            , 'hr-org-location'
            , 'logger'
            , 'nosy'
            , 'user'
            , 'external'
            ]
        self.users = {'admin' : '1', 'anonymous' : '2'}
        for u in self.allroles :
            if u in self.users :
                continue
            roles = u.split ('+')
            if u not in nouserroles :
                roles.append ('user')
            r_ok = (self.db.security.role.has_key (r) for r in roles)
            # wired and :-)
            if not reduce (mul, r_ok, 1) :
                continue
            params = dict \
                ( username = u
                , roles    = ','.join (roles)
                )
            try :
                status = self.db.user_status.lookup ('system')
                params ['status'] = status
            except ValueError :
                pass
            try :
                self.users [u] = self.db.user.create (**params)
            except ValueError :
                self.users [u] = self.db.user.lookup (u)
    # end def create_test_users

# end class _Test_Case

class Test_Case_Support_Timetracker (_Test_Case) :
    schemaname = 'sfull'
    roles = \
        [ 'admin', 'adr_readonly', 'anonymous', 'contact', 'controlling'
        , 'doc_admin', 'hr', 'hr-org-location', 'issue_admin', 'it'
        , 'itview', 'nosy'
        , 'office', 'project', 'project_view', 'supportadmin', 'type', 'user'
        ]
    transprop_perms = transprop_sfull
# end class Test_Case_Support_Timetracker

class Test_Case_Timetracker (_Test_Case) :
    schemaname = 'full'
    roles = \
        [ 'admin', 'anonymous', 'contact', 'controlling', 'doc_admin'
        , 'external', 'hr', 'hr-org-location', 'issue_admin', 'it'
        , 'itview', 'nosy'
        , 'office', 'pgp', 'project', 'project_view', 'supportadmin', 'user'
        ]
    transprop_perms = transprop_full

    def setup_db (self) :
        self.db = self.tracker.open ('admin')
        self.db.overtime_period.create \
            ( name   = 'yearly/weekly'
            , months = 12
            , order  = 1.5
            , weekly = True
            )
        self.org = self.db.organisation.create \
            ( name        = 'The Org'
            , description = 'A Test Organisation'
            , mail_domain = 'example.com'
            , valid_from  = date.Date ('2004-01-01')
            )
        self.loc = self.db.location.create \
            ( name    = 'Vienna'
            , country = 'Austria'
            , address = 'Vienna, Austria'
            )
        self.olo = self.db.org_location.create \
            ( name         = 'The Org, Vienna'
            , location     = self.loc
            , organisation = self.org
            )
        self.dep = self.db.department.create \
            ( name       = 'Software Development'
            , valid_from = date.Date ('2004-01-01')
            )
        self.username0 = 'testuser0'
        self.user0 = self.db.user.create \
            ( username     = self.username0
            , firstname    = 'Test'
            , lastname     = 'User0'
            , org_location = self.olo
            , department   = self.dep
            , roles        = 'User,Nosy,HR,controlling,project,ITView,IT'
            )
        self.username1 = 'testuser1'
        self.user1 = self.db.user.create \
            ( username     = self.username1
            , firstname    = 'Test'
            , lastname     = 'User1'
            , org_location = self.olo
            , department   = self.dep
            )
        self.username2 = 'testuser2'
        self.user2 = self.db.user.create \
            ( username     = self.username2
            , firstname    = 'Test'
            , lastname     = 'User2'
            , org_location = self.olo
            , department   = self.dep
            )
        # create initial dyn_user record for each user
        # others will follow during tests
        ud = self.db.user_dynamic.filter (None, dict (user = self.user1))
        self.assertEqual (len (ud), 1)
        self.db.user_dynamic.set \
            ( ud [0]
            , valid_from      = date.Date ('2005-09-01')
            , booking_allowed = False
            , vacation_yearly = 25
            , all_in          = True
            , hours_mon       = 7.75
            , hours_tue       = 7.75
            , hours_wed       = 7.75
            , hours_thu       = 7.75
            , hours_fri       = 7.5
            )
        self.db.user_dynamic.create \
            ( user              = self.user1
            , valid_from        = date.Date ('2005-10-01')
            , booking_allowed   = True
            , vacation_yearly   = 25
            , all_in            = False
            , hours_mon         = 0.0
            , hours_tue         = 0.0
            , hours_wed         = 0.0
            , hours_thu         = 0.0
            , hours_fri         = 0.0
            , daily_worktime    = 0.0
            , org_location      = self.olo
            , department        = self.dep
            , supp_weekly_hours = 40
            , overtime_period   = self.db.overtime_period.lookup ('week')
            )
        self.assertEqual \
            ( self.db.user_dynamic.get (ud [0], 'valid_to')
            , date.Date ('2005-10-01')
            )
        ud = self.db.user_dynamic.filter (None, dict (user = self.user2))
        self.assertEqual (len (ud), 1)
        self.db.user_dynamic.set \
            ( ud [0]
            , valid_from       = date.Date ('2008-11-03')
            , booking_allowed  = True
            , vacation_yearly  = 25
            , all_in           = True
            , hours_mon        = 7.75
            , hours_tue        = 7.75
            , hours_wed        = 7.75
            , hours_thu        = 7.75
            , hours_fri        = 7.5
            , supp_per_period  = 40
            , additional_hours = 40
            )
        f = self.db.daily_record_freeze.create \
            ( user           = self.user1
            , balance        = 0.0
            , achieved_hours = 0.0
            , frozen         = True
            , date           = date.Date ('2005-12-31')
            )
        f = self.db.daily_record_freeze.getnode (f)
        self.assertEqual (f.balance,        0.0)
        self.assertEqual (f.achieved_hours, 0.0)
        self.assertEqual (f.validity_date,  date.Date ('2005-12-25'))
        wl_off    = self.db.work_location.lookup ('off')
        wl_trav   = self.db.work_location.lookup ('off-site/trav.')
        stat_open = self.db.time_project_status.lookup ('Open')
        self.ccg = self.db.cost_center_group.create (name = 'CCG')
        self.cc = self.db.cost_center.create \
            ( name              = 'CC'
            , cost_center_group = self.ccg
            , status            = self.db.cost_center_status.lookup ('Open')
            )
        self.holiday_tp = self.db.time_project.create \
            ( name = 'Public Holiday'
            , work_location     = wl_off
            , op_project        = False
            , no_overtime       = True
            , is_public_holiday = True
            , responsible       = '1'
            , department        = self.dep
            , status            = stat_open
            , cost_center       = self.cc
            )
        self.unpaid_tp = self.db.time_project.create \
            ( name = 'Leave'
            , work_location     = wl_off
            , op_project        = False
            , no_overtime       = True
            , responsible       = '1'
            , department        = self.dep
            , status            = stat_open
            , cost_center       = self.cc
            )
        self.travel_tp = self.db.time_project.create \
            ( name = 'Travel'
            , work_location     = wl_trav
            , op_project        = False
            , responsible       = '1'
            , department        = self.dep
            , status            = stat_open
            , cost_center       = self.cc
            )
        self.normal_tp = self.db.time_project.create \
            ( name = 'A Project'
            , op_project        = True
            , responsible       = self.user1
            , department        = self.dep
            , organisation      = self.org
            , cost_center       = self.cc
            )
        self.holiday_wp = self.db.time_wp.create \
            ( name              = 'Holiday'
            , project           = self.holiday_tp
            , time_start        = date.Date ('2004-01-01')
            , durations_allowed = True
            , responsible       = '1'
            , bookers           = [self.user1, self.user2]
            , cost_center       = self.cc
            )
        self.unpaid_wp = self.db.time_wp.create \
            ( name              = 'Unpaid'
            , project           = self.holiday_tp
            , time_start        = date.Date ('2004-01-01')
            , durations_allowed = True
            , responsible       = '1'
            , bookers           = [self.user1, self.user2]
            , cost_center       = self.cc
            )
        self.travel_wp = self.db.time_wp.create \
            ( name              = 'Travel'
            , project           = self.holiday_tp
            , time_start        = date.Date ('2004-01-01')
            , travel            = True
            , responsible       = '1'
            , bookers           = [self.user1, self.user2]
            , cost_center       = self.cc
            )
        for i in xrange (40) :
            self.db.time_wp.create \
                ( name              = 'Work Package %s' % i
                , project           = self.normal_tp
                , time_start        = date.Date ('2004-01-01')
                , travel            = True
                , responsible       = '1'
                , bookers           = [self.user1, self.user2]
                , cost_center       = self.cc
                )
        self.db.commit ()
        self.log.debug ("End of setup")
    # end def setup_db

    def setup_user3 (self) :
        self.username3 = 'testuser3'
        self.user3 = self.db.user.create \
            ( username     = self.username3
            , firstname    = 'NochEinTest'
            , lastname     = 'User3'
            , org_location = self.olo
            , department   = self.dep
            )
        # create initial dyn_user record for user
        ud = self.db.user_dynamic.filter (None, dict (user = self.user3))
        self.assertEqual (len (ud), 1)
        p = self.db.overtime_period.lookup ('yearly/weekly')
        self.db.user_dynamic.set \
            ( ud [0]
            , valid_from        = date.Date ('2010-01-01')
            , booking_allowed   = True
            , vacation_yearly   = 25
            , all_in            = False
            , hours_mon         = 7.75
            , hours_tue         = 7.75
            , hours_wed         = 7.75
            , hours_thu         = 7.75
            , hours_fri         = 7.5
            , additional_hours  = 40
            , supp_weekly_hours = 45.0
            , supp_per_period   = 84.0
            , overtime_period   = p
            , weekend_allowed   = True
            )
        self.db.commit ()
    # end def setup_user3

    def test_rename_status (self) :
        self.log.debug ('test_rename_status')
        self.setup_db ()
        # test that renaming the 'New' cost_center status will still work
        ccs = self.db.cost_center_status.lookup ('New')
        self.db.cost_center_status.set (ccs, name = 'Something')
        self.cc = self.db.cost_center.create \
            ( name              = 'CC-New'
            , cost_center_group = self.ccg
            )
        # test that renaming the 'New' time_project_status will still work
        tps = self.db.time_project_status.lookup ('New')
        self.db.time_project_status.set (tps, name = 'Something')
        self.normal_tp = self.db.time_project.create \
            ( name = 'Another Project'
            , op_project        = True
            , responsible       = self.user1
            , department        = self.dep
            , organisation      = self.org
            , cost_center       = self.cc
            )
    # end def test_rename_status

    def test_user1 (self) :
        self.log.debug ('test_user1')
        self.setup_db ()
        self.db.close ()
        self.db = self.tracker.open (self.username1)
        user1_time.import_data_1 (self.db, self.user1)
        self.db.close ()
        self.db = self.tracker.open ('admin')
        self.db.overtime_correction.create \
            ( user    = self.user1
            , value   = 910.0
            , comment = 'Auf null stellen, da keine Eintraege'
            , date    = date.Date ('2008-09-07')
            )
        dr = self.db.daily_record.filter \
            (None, dict (user = self.user1, date = '2006-01-23')) [0]
        dr = self.db.daily_record.getnode (dr)
        update_tr_duration (self.db, dr)
        self.assertEqual (dr.tr_duration_ok, 0)
        self.db.user_dynamic.create \
            ( user              = self.user1
            , valid_from        = date.Date ('2006-01-01')
            , booking_allowed   = True
            , vacation_yearly   = 25
            , all_in            = True
            , hours_mon         = 7.75
            , hours_tue         = 7.75
            , hours_wed         = 7.75
            , hours_thu         = 7.75
            , hours_fri         = 7.5
            , daily_worktime    = 0.0
            , org_location      = self.olo
            , department        = self.dep
            )
        self.db.clearCache ()
        self.assertEqual (dr.tr_duration_ok, None)
        self.db.user_dynamic.create \
            ( user              = self.user1
            , valid_from        = date.Date ('2008-01-01')
            , valid_to          = date.Date ('2008-09-11')
            , booking_allowed   = True
            , vacation_yearly   = 25
            , all_in            = False
            , hours_mon         = 5.0
            , hours_tue         = 5.0
            , hours_wed         = 5.0
            , hours_thu         = 5.0
            , hours_fri         = 5.0
            , daily_worktime    = 0.0
            , supp_weekly_hours = 25.
            , org_location      = self.olo
            , department        = self.dep
            , overtime_period   = self.db.overtime_period.lookup ('week')
            )
        self.db.user_dynamic.create \
            ( user              = self.user1
            , valid_from        = date.Date ('2009-01-04')
            , booking_allowed   = True
            , vacation_yearly   = 25
            , all_in            = True
            , hours_mon         = 2.0
            , hours_tue         = 2.0
            , hours_wed         = 2.0
            , hours_thu         = 2.0
            , hours_fri         = 2.0
            , daily_worktime    = 0.0
            , org_location      = self.olo
            , department        = self.dep
            )
        self.db.user_dynamic.create \
            ( user              = self.user1
            , valid_from        = date.Date ('2010-01-01')
            , booking_allowed   = True
            , vacation_yearly   = 25
            , all_in            = True
            , hours_mon         = 2.0
            , hours_tue         = 2.0
            , hours_wed         = 2.0
            , hours_thu         = 2.0
            , hours_fri         = 2.0
            , daily_worktime    = 0.0
            , org_location      = self.olo
            , department        = self.dep
            )
        self.db.commit ()
        self.db.close  ()
        self.db = self.tracker.open (self.username1)
        fs = { 'user'         : [self.user1]
             , 'date'         : '2008-09-01;2008-09-10'
             , 'summary_type' : [2, 4]
             }
        class r : filterspec = fs
        summary_init (self.tracker)
        sr = Staff_Report (self.db, r, templating.TemplatingUtils (None))
        lines = [x.strip ().split (',') for x in sr.as_csv ().split ('\n')]
        self.assertEqual (len (lines), 5)
        self.assertEqual (lines [1] [1], 'WW 36/2008')
        self.assertEqual (lines [2] [1], 'WW 37/2008')
        self.assertEqual (lines [3] [1], '2008-09-01;2008-09-10')
        self.assertEqual (lines [1][10], '15.00')
        self.assertEqual (lines [2][10], '0.00')
        self.assertEqual (lines [3][10], '0.00')
        self.assertEqual (lines [3] [9], '910.0')
        fs = { 'user'         : [self.user1]
             , 'date'         : '2009-12-21;2010-01-03'
             , 'summary_type' : [2, 4]
             }
        class r : filterspec = fs
        sr = Staff_Report (self.db, r, templating.TemplatingUtils (None))
        lines = [x.strip ().split (',') for x in sr.as_csv ().split ('\n')]
        self.assertEqual (lines [1] [1], 'WW 52/2009')
        self.assertEqual (lines [2] [1], 'WW 53/2009')
        self.assertEqual (lines [3] [1], '2009-12-21;2010-01-03')
        self.assertEqual (lines [1][10], '0.00')
        self.assertEqual (lines [2][10], '0.00')
        self.assertEqual (lines [3][10], '0.00')

        for d in ('2006-12-31', '2007-12-31') :
            f = self.db.daily_record_freeze.create \
                ( user           = self.user1
                , frozen         = True
                , date           = date.Date (d)
                )
            f = self.db.daily_record_freeze.getnode (f)
            self.assertEqual (f.balance,        0.0)
            self.assertEqual (f.achieved_hours, 0.0)
            self.assertEqual (f.validity_date,  date.Date (d))

        f = self.db.daily_record_freeze.create \
            ( user           = self.user1
            , frozen         = True
            , date           = date.Date ('2008-09-10')
            )
        f = self.db.daily_record_freeze.getnode (f)
        self.assertEqual (f.balance,       15.0)
        self.assertEqual (f.achieved_hours, 0.0)
        self.assertEqual (f.validity_date,  date.Date ('2008-09-07'))

        dyn = first_user_dynamic (self.db, self.user1)
        self.assertEqual (dyn.valid_from, date.Date ('2005-09-01'))
        op  = overtime_periods \
            (self.db, self.user1, dyn.valid_from, date.Date ('2009-12-31'))
        self.assertEqual (len (op), 1)
        self.assertEqual (op [0][0], date.Date ('2005-10-01'))
        self.assertEqual (op [0][1], date.Date ('2008-09-10'))
        self.assertEqual (op [0][2].name, 'week')
        dyn = next_user_dynamic (self.db, dyn)
        self.assertEqual (dyn.valid_from, date.Date ('2005-10-01'))
        dyn = next_user_dynamic (self.db, dyn)
        self.assertEqual (dyn.valid_from, date.Date ('2006-01-01'))
        self.assertEqual (dyn.overtime_period, None)

        bal = compute_balance \
            (self.db, self.user1, date.Date ('2009-12-31'), sharp_end = True)
        self.assertEqual (bal, (0.0, 0))
        bal = compute_balance \
            (self.db, self.user1, date.Date ('2009-12-27'), sharp_end = True)
        self.assertEqual (bal, (0.0, 0))
        bal = compute_balance \
            (self.db, self.user1, date.Date ('2010-01-03'), sharp_end = True)
        self.assertEqual (bal, (0.0, 0))

        bal = compute_balance \
            (self.db, self.user1, date.Date ('2009-12-31'), not_after = True)
        self.assertEqual (bal, (0.0, 0))
        bal = compute_balance \
            (self.db, self.user1, date.Date ('2009-12-27'), not_after = True)
        self.assertEqual (bal, (0.0, 0))
        bal = compute_balance \
            (self.db, self.user1, date.Date ('2010-01-03'), not_after = True)
        self.assertEqual (bal, (0.0, 0))

        sr = Staff_Report (self.db, r, templating.TemplatingUtils (None))
        lines = [x.strip ().split (',') for x in sr.as_csv ().split ('\n')]
        self.assertEqual (lines [1] [1], 'WW 52/2009')
        self.assertEqual (lines [2] [1], 'WW 53/2009')
        self.assertEqual (lines [3] [1], '2009-12-21;2010-01-03')
        self.assertEqual (lines [1][10], '0.00')
        self.assertEqual (lines [2][10], '0.00')
        self.assertEqual (lines [3][10], '0.00')

        f = self.db.daily_record_freeze.create \
            ( user           = self.user1
            , frozen         = True
            , date           = date.Date ('2009-12-31')
            )
        f = self.db.daily_record_freeze.getnode (f)
        self.assertEqual (f.balance,        0.0)
        self.assertEqual (f.achieved_hours, 0.0)
        self.assertEqual (f.validity_date,  date.Date ('2009-12-31'))

        self.db.daily_record_freeze.set (f.id, frozen = False)
        self.assertEqual (f.balance, None)
        self.db.daily_record_freeze.set (f.id, frozen = True)

        self.db.clearCache ()
        self.assertEqual (f.balance,        0.0)
        self.assertEqual (f.achieved_hours, 0.0)
        self.assertEqual (f.validity_date,  date.Date ('2009-12-31'))

        self.db.clearCache ()

        sr = Staff_Report (self.db, r, templating.TemplatingUtils (None))
        lines = [x.strip ().split (',') for x in sr.as_csv ().split ('\n')]
        self.assertEqual (lines [1] [1], 'WW 52/2009')
        self.assertEqual (lines [2] [1], 'WW 53/2009')
        self.assertEqual (lines [3] [1], '2009-12-21;2010-01-03')
        self.assertEqual (lines [1][10], '0.00')
        self.assertEqual (lines [2][10], '0.00')
        self.assertEqual (lines [3][10], '0.00')
    # end def test_user1

    def test_user2 (self) :
        self.log.debug ('test_user2')
        self.setup_db ()
        self.db.close ()
        self.db = self.tracker.open (self.username2)
        user2_time.import_data_2 (self.db, self.user2)
        self.db.close ()
        self.db = self.tracker.open ('admin')
        self.db.user_dynamic.create \
            ( user              = self.user2
            , valid_from        = date.Date ('2009-01-01')
            , booking_allowed   = True
            , vacation_yearly   = 25
            , all_in            = False
            , hours_mon         = 7.75
            , hours_tue         = 7.75
            , hours_wed         = 7.75
            , hours_thu         = 7.75
            , hours_fri         = 7.5
            , supp_weekly_hours = 38.5
            , additional_hours  = 38.5
            , overtime_period   = self.db.overtime_period.lookup ('week')
            , org_location      = self.olo
            , department        = self.dep
            )
        f = self.db.daily_record_freeze.create \
            ( user           = self.user2
            , frozen         = True
            , date           = date.Date ('2008-12-31')
            )
        f = self.db.daily_record_freeze.getnode (f)
        self.assertEqual (f.balance,        0.0)
        self.assertEqual (f.achieved_hours, 0.0)
        self.assertEqual (f.validity_date,  date.Date ('2008-12-31'))
        self.db.commit ()
        self.db.close  ()
        self.db = self.tracker.open (self.username2)
        fs = { 'user'         : [self.user2]
             , 'date'         : '2008-12-22;2009-01-04'
             , 'summary_type' : [2, 4]
             }
        class r : filterspec = fs
        summary_init (self.tracker)
        ndr = self.db.daily_record.getnode ('51')
        self.assertEqual (len (ndr.time_record), 2)
        sr = Staff_Report (self.db, r, templating.TemplatingUtils (None))
        lines = [x.strip ().split (',') for x in sr.as_csv ().split ('\n')]
        self.assertEqual (len (lines), 5)
        self.assertEqual (lines [1] [1], 'WW 52/2008')
        self.assertEqual (lines [2] [1], 'WW 1/2009')
        self.assertEqual (lines [3] [1], '2008-12-22;2009-01-04')
        self.assertEqual (lines [1][10], '0.00')
        self.assertEqual (lines [2][10], '0.00')
        self.assertEqual (lines [3][10], '0.00')

        fs = { 'user'         : [self.user2]
             , 'date'         : '2009-12-21;2010-01-03'
             , 'summary_type' : [2, 4]
             }
        class r : filterspec = fs
        sr = Staff_Report (self.db, r, templating.TemplatingUtils (None))
        lines = [x.strip ().split (',') for x in sr.as_csv ().split ('\n')]
        self.assertEqual (len (lines), 5)
        self.assertEqual (lines [1] [1], 'WW 52/2009')
        self.assertEqual (lines [2] [1], 'WW 53/2009')
        self.assertEqual (lines [3] [1], '2009-12-21;2010-01-03')
        self.assertEqual (lines [1][10], '113.12')
        self.assertEqual (lines [2][10], '113.12')
        self.assertEqual (lines [3][10], '113.12')
        f = self.db.daily_record_freeze.create \
            ( user           = self.user2
            , frozen         = True
            , date           = date.Date ('2009-12-31')
            )
        f = self.db.daily_record_freeze.getnode (f)
        self.assertEqual (f.balance,        113.125)
        self.assertEqual (f.achieved_hours, 0.0)
        self.assertEqual (f.validity_date,  date.Date ('2009-12-27'))
        # test split of frozen dyn record and reset of tr_duration
        dr1 = self.db.daily_record.filter \
            (None, dict (user = self.user2, date = '2009-12-31')) [0]
        dr1 = self.db.daily_record.getnode (dr1)
        update_tr_duration (self.db, dr1)
        self.assertEqual (dr1.tr_duration_ok, 7.75)
        dr2 = self.db.daily_record.filter \
            (None, dict (user = self.user2, date = '2010-01-01')) [0]
        dr2 = self.db.daily_record.getnode (dr2)
        update_tr_duration (self.db, dr2)
        self.assertEqual (dr2.tr_duration_ok, 7.5)
        self.db.user_dynamic.create \
            ( user              = self.user2
            , valid_from        = date.Date ('2010-01-01')
            , booking_allowed   = True
            , vacation_yearly   = 25
            , all_in            = False
            , hours_mon         = 7.75
            , hours_tue         = 7.75
            , hours_wed         = 7.75
            , hours_thu         = 7.75
            , hours_fri         = 7.5
            , supp_weekly_hours = 38.5
            , additional_hours  = 38.5
            , overtime_period   = self.db.overtime_period.lookup ('week')
            , org_location      = self.olo
            , department        = self.dep
            )
        self.db.clearCache ()
        self.assertEqual (dr1.tr_duration_ok, 7.75)
        self.assertEqual (dr2.tr_duration_ok, None)
    # end def test_user2

    def test_user3 (self) :
        self.log.debug ('test_user3')
        self.setup_db ()
        self.setup_user3 ()
        self.db.close ()
        self.db = self.tracker.open (self.username3)
        user3_time.import_data_3 (self.db, self.user3)
        self.db.close ()
        self.db = self.tracker.open (self.username0)
        summary_init (self.tracker)
        fs = { 'user'         : [self.user3]
             , 'date'         : '2010-01-01;2010-05-31'
             , 'summary_type' : [2, 3, 4]
             }
        class r : filterspec = fs
        sr = Staff_Report (self.db, r, templating.TemplatingUtils (None))
        lines = [x.strip ().split (',') for x in sr.as_csv ().split ('\n')]
        self.assertEqual (len (lines), 31)
        self.assertEqual (lines [0]  [1], 'Time Period')
        self.assertEqual (lines [0] [12], 'Achieved supplementary hours')
        self.assertEqual (lines [1]  [1], 'WW 53/2009')
        self.assertEqual (lines [2]  [1], 'WW 1/2010')
        self.assertEqual (lines [16] [6], '57.62')
        self.assertEqual (lines [16] [8], '45.00')
        self.assertEqual (lines [16][10], '12.62')
        self.assertEqual (lines [16][12], '5.00')
        self.assertEqual (lines [17] [6], '52.88')
        self.assertEqual (lines [17] [8], '45.00')
        self.assertEqual (lines [17][10], '20.50')
        self.assertEqual (lines [17][12], '10.00')
        self.assertEqual (lines [18] [1], 'WW 17/2010')
        self.assertEqual (lines [18] [6], '38.50')
        self.assertEqual (lines [18] [8], '45.00')
        self.assertEqual (lines [18][10], '20.50')
        self.assertEqual (lines [18][12], '10.00')
        self.assertEqual (lines [19] [1], 'WW 18/2010')
        self.assertEqual (lines [19] [6], '38.50')
        self.assertEqual (lines [19] [8], '45.00')
        self.assertEqual (lines [19][10], '20.50')
        self.assertEqual (lines [19][12], '10.00')
    # end def test_user3

    def concurrency (self, method) :
        """ Ensure that no cached values from previous transaction are used.
            It is no concurrency test (which would fail due to a
            concurrent update) in the sense that we have two concurrent
            transactions.
        """
        trid = '4'
        self.setup_db ()
        self.db.close ()
        self.db = None
        self.db = self.tracker.open (self.username1)
        user1_time.import_data_1 (self.db, self.user1)
        self.db.close ()
        self.db  = None

        self.db1 = self.tracker.open ('admin')
        self.db2 = self.tracker.open ('admin')
        self.db1.time_record.set (trid, duration = 7)
        self.db1.time_record.set (trid, duration = 8)
        drid = self.db1.time_record.get (trid, 'daily_record')
        tr_d1 = self.db1.time_record.get  (trid, 'tr_duration')
        dr_d1 = self.db1.daily_record.get (drid, 'tr_duration_ok')
        self.log.debug ("db1.commit after time_record.set")
        self.db1.commit ()

        dr  = self.db2.daily_record.getnode (drid)
        dud = dr.tr_duration_ok
        tr  = self.db2.time_record.getnode (trid)
        dut = tr.tr_duration
        self.log.debug ("db2.commit - 1 after get")
        self.db2.commit ()
        update_tr_duration (self.db2, dr)
        self.log.debug ("db2.commit - 2 after update_tr_duration")
        self.db2.commit ()

        self.db1.commit ()

        self.log.debug ("before method")
        method (drid, trid)
        self.log.debug ("after  method")
        self.db1.commit ()

        self.db1.clearCache ()

        self.assertEqual \
            (self.db1.daily_record.get (drid, 'tr_duration_ok'), None)
    # end def concurrency

    def concurrency_create (self, drid, trid) :
        self.db1.time_record.create (duration = 5, daily_record = drid)
    # end def concurrency_set

    def concurrency_retire (self, drid, trid) :
        self.db1.time_record.set (trid, duration = None)
    # end def concurrency_set

    def concurrency_set (self, drid, trid) :
        self.db1.time_record.set (trid, duration = 5)
    # end def concurrency_set

    def test_concurrency_create (self) :
        self.log.debug ('test_concurrency_create')
        self.concurrency (self.concurrency_create)
    # end def test_concurrency_create

    def test_concurrency_retire (self) :
        self.log.debug ('test_concurrency_retire')
        self.concurrency (self.concurrency_retire)
    # end def test_concurrency_retire

    def test_concurrency_set (self) :
        self.log.debug ('test_concurrency_set')
        self.concurrency (self.concurrency_set)
    # end def test_concurrency_set

    def test_maturity_index (self) :
        self.log.debug ('test_maturity_index')
        self.db = self.tracker.open ('admin')
        user = self.db.user.create \
            ( username = 'user'
            , status = self.db.user_status.lookup ('system')
            , roles = 'User,Nosy'
            )
        pending = self.db.category.lookup ('pending')
        self.db.category.set (pending, responsible = user)
        self.db.commit ()
        self.db.clearCache ()
        self.db.close ()
        self.db = self.tracker.open ('user')
        opn = self.db.status.lookup ('open')
        m1 = self.db.msg.create (content="new issue", subject="new issue")
        m2 = self.db.msg.create (content="Mistaken", subject="Mistaken")
        mc = self.db.issue.create \
            ( title          = "Master Container"
            , messages       = [m1]
            , release        = 'None'
            , status         = opn
            , numeric_effort = 1
            , category       = pending
            )
        c1 = self.db.issue.create \
            ( title          = "Container"
            , messages       = [m1]
            , release        = 'None'
            , status         = opn
            , numeric_effort = 1
            , category       = pending
            , part_of        = mc
            )
        self.assertEqual (self.db.issue.get (c1, 'status'), opn)
        self.assertEqual (self.db.issue.get (c1, 'maturity_index'), 5.0)
        c2 = self.db.issue.create \
            ( title          = "Container"
            , messages       = [m1]
            , release        = 'None'
            , status         = opn
            , numeric_effort = 1
            , category       = pending
            , part_of        = mc
            )
        self.assertEqual (self.db.issue.get (c2, 'status'), opn)
        self.assertEqual (self.db.issue.get (c2, 'maturity_index'), 5.0)
        i1 = self.db.issue.create \
            ( title    = "Issue no. 1"
            , messages = [m1]
            , release  = '1'
            , status   = opn
            , part_of  = c1
            )
        self.assertEqual (self.db.issue.get (c1, 'maturity_index'), 10.0)
        i2 = self.db.issue.create \
            ( title    = "Issue no. 2"
            , messages = [m1]
            , release  = '2'
            , status   = opn
            , part_of  = c1
            )
        self.assertEqual (self.db.issue.get (c1, 'maturity_index'), 20.0)
        i3 = self.db.issue.create \
            ( title    = "Issue no. 3"
            , messages = [m1]
            , release  = '3'
            , status   = opn
            , part_of  = c2
            )
        self.db.commit ()
        self.assertEqual (self.db.issue.get (i1, 'maturity_index'), 10.0)
        self.assertEqual (self.db.issue.get (i2, 'maturity_index'), 10.0)
        self.assertEqual (self.db.issue.get (i3, 'maturity_index'), 10.0)
        self.assertEqual (self.db.issue.get (c1, 'maturity_index'), 20.0)
        self.assertEqual (self.db.issue.get (c2, 'maturity_index'), 10.0)
        self.assertEqual (self.db.issue.get (mc, 'maturity_index'), 30.0)

        self.db.issue.set (i1, part_of = c2)
        self.assertEqual (self.db.issue.get (i1, 'maturity_index'), 10.0)
        self.assertEqual (self.db.issue.get (c1, 'maturity_index'), 10.0)
        self.assertEqual (self.db.issue.get (c2, 'maturity_index'), 20.0)
        self.assertEqual (self.db.issue.get (mc, 'maturity_index'), 30.0)

        # close
        mistaken = self.db.kind.lookup ('Mistaken')
        self.db.issue.set (i1, kind = mistaken, messages = [m1, m2])
        self.assertEqual (self.db.issue.get (i1, 'maturity_index'),  0.0)
        self.assertEqual (self.db.issue.get (c2, 'maturity_index'), 10.0)
        self.assertEqual (self.db.issue.get (mc, 'maturity_index'), 20.0)

        self.db2 = self.tracker.open ('user')
        self.db2.issue.get (c1, 'maturity_index')
        self.db2.issue.get (c2, 'maturity_index')
        self.db2.commit ()

        self.db.commit ()

        # concurrency: check that we don't cache values over commits
        self.assertEqual (self.db2.issue.get (c1, 'maturity_index'), 10.0)
        self.assertEqual (self.db2.issue.get (c2, 'maturity_index'), 10.0)
        self.assertEqual (self.db2.issue.get (mc, 'maturity_index'), 20.0)
        self.db2.issue.set (i3, part_of = c1)
        self.db2.commit ()
        self.assertEqual (self.db2.issue.get (c1, 'maturity_index'), 20.0)
        self.assertEqual (self.db2.issue.get (c2, 'maturity_index'),  0.0)
        self.assertEqual (self.db2.issue.get (mc, 'maturity_index'), 20.0)
    # end def test_maturity_index

    def test_tr_duration (self) :
        self.log.debug ('test_tr_duration')
        trid = '4'
        self.setup_db ()
        self.db.close ()
        self.db = None
        self.db = self.tracker.open (self.username1)
        user1_time.import_data_1 (self.db, self.user1)
        self.db.close ()
        self.db = self.tracker.open ('admin')

        self.db.time_record.set (trid, duration = 7)
        self.db.time_record.set (trid, duration = 8)
        drid = self.db.time_record.get (trid, 'daily_record')
        self.db.commit ()
        self.db.clearCache ()

        trok = self.db.daily_record.get (drid, 'tr_duration_ok')
        self.assertEqual (trok, None)
        self.assertEqual (self.db.time_record.get (trid, 'duration'), 8)
        self.assertEqual (self.db.time_record.get (trid, 'tr_duration'), None)
        self.db.clearCache ()

        dr = self.db.daily_record.getnode (drid)
        update_tr_duration (self.db, dr)
        self.db.commit ()
        self.db.clearCache ()
        self.assertEqual (self.db.time_record.get (trid, 'duration'), 8)
        self.assertEqual (self.db.time_record.get (trid, 'tr_duration'), 8)
        self.assertEqual (self.db.daily_record.get (drid, 'tr_duration_ok'), 8)
    # end def test_tr_duration
# end class Test_Case_Timetracker

class Test_Case_Abo (_Test_Case) :
    schemaname = 'abo'
    roles = \
        [ 'abo', 'admin', 'adr_readonly', 'anonymous', 'contact'
        , 'invoice', 'letter', 'product', 'type', 'user'
        ]
    transprop_perms = transprop_abo
# end class Test_Case_Abo

class Test_Case_Adr (_Test_Case) :
    schemaname = 'adr'
    roles = \
        [ 'admin', 'adr_readonly', 'anonymous', 'contact', 'letter'
        , 'type', 'user'
        ]
    transprop_perms = transprop_adr
# end class Test_Case_Adr

class Test_Case_ERP (_Test_Case) :
    schemaname = 'erp'
    roles = \
        [ 'admin', 'adr_readonly', 'anonymous', 'contact', 'discount'
        , 'invoice', 'letter', 'product', 'type', 'user'
        ]
    transprop_perms = transprop_erp
# end class Test_Case_ERP

class Test_Case_IT (_Test_Case) :
    schemaname = 'it'
    roles = ['admin', 'anonymous', 'it', 'itview', 'nosy', 'user']
# end class Test_Case_IT

class Test_Case_ITAdr (_Test_Case) :
    schemaname = 'itadr'
    roles = \
        [ 'admin', 'adr_readonly', 'anonymous', 'contact', 'it'
        , 'itview', 'nosy', 'type', 'user'
        ]
    transprop_perms = transprop_itadr
# end class Test_Case_ITAdr

class Test_Case_Kvats (_Test_Case) :
    schemaname = 'kvats'
    roles = ['admin', 'anonymous', 'issue_admin', 'nosy', 'user']
    transprop_perms = transprop_kvats
# end class Test_Case_Kvats

class Test_Case_Lielas (_Test_Case) :
    schemaname = 'lielas'
    roles = ['admin', 'anonymous', 'guest', 'logger', 'user']
    transprop_perms = transprop_lielas
# end class Test_Case_Lielas

def test_suite () :
    suite = unittest.TestSuite ()
    suite.addTest (unittest.makeSuite (Test_Case_Abo))
    suite.addTest (unittest.makeSuite (Test_Case_Adr))
    suite.addTest (unittest.makeSuite (Test_Case_ERP))
    suite.addTest (unittest.makeSuite (Test_Case_IT))
    suite.addTest (unittest.makeSuite (Test_Case_ITAdr))
    suite.addTest (unittest.makeSuite (Test_Case_Kvats))
    suite.addTest (unittest.makeSuite (Test_Case_Lielas))
    suite.addTest (unittest.makeSuite (Test_Case_Support_Timetracker))
    suite.addTest (unittest.makeSuite (Test_Case_Timetracker))
    return suite
# end def test_suite
