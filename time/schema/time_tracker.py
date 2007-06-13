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
#    company
#
# Purpose
#    Schema definitions for a company.
#
#--
#

from roundup.hyperdb import Class
from common          import clearance_by
from freeze          import frozen
from roundup.date    import Interval
import schemadef
import sum_common
import common

def init (db, Class, String, Date, Link, Multilink, Boolean, Number, ** kw) :
    cost_center = Class \
        ( db
        , ''"cost_center"
        , name                  = String    ()
        , description           = String    ()
        , status                = Link      ("cost_center_status")
        , cost_center_group     = Link      ("cost_center_group")
        , organisation          = Link      ("organisation")
        )
    cost_center.setkey ("name")

    cost_center_group = Class \
        ( db
        , ''"cost_center_group"
        , name                  = String    ()
        , description           = String    ()
        , responsible           = Link      ("user")
        , active                = Boolean   ()
        )
    cost_center_group.setkey ("name")

    cost_center_status = Class \
        ( db
        , ''"cost_center_status"
        , name                  = String    ()
        , description           = String    ()
        , active                = Boolean   ()
        )
    cost_center_status.setkey ("name")

    daily_record = Class \
        ( db
        , ''"daily_record"
        , user                  = Link      ("user",          do_journal = "no")
        , date                  = Date      (offset = 0)
        , status                = Link      ( "daily_record_status"
                                            , do_journal = "no"
                                            )
        , required_overtime     = Boolean   ()
        , weekend_allowed       = Boolean   ()
        , time_record           = Multilink ("time_record",   do_journal = "no")
        , tr_duration_ok        = Number    ()
        )
    daily_record.setlabelprop ('date')

    daily_record_freeze = Class \
        ( db
        , ''"daily_record_freeze"
        , user                  = Link      ("user",          do_journal = "no")
        , date                  = Date      (offset = 0)
        , frozen                = Boolean   ()
        , week_balance          = Number    ()
        , month_balance         = Number    ()
        , year_balance          = Number    ()
        )
    daily_record_freeze.setlabelprop ('date')

    overtime_correction = Class \
        ( db
        , ''"overtime_correction"
        , user                  = Link      ("user",          do_journal = "no")
        , date                  = Date      (offset = 0)
        , value                 = Number    ()
        , comment               = String    ()
        )
    overtime_correction.setlabelprop ('date')

    daily_record_status = Class \
        ( db
        , ''"daily_record_status"
        , name                  = String    ()
        , description           = String    ()
        )
    daily_record_status.setkey ("name")

    public_holiday = Class \
        ( db
        , ''"public_holiday"
        , name                  = String    ()
        , description           = String    ()
        , date                  = Date      (offset = 0)
        , locations             = Multilink ("location")
        , is_half               = Boolean   ()
        )

    summary_report = Class \
        ( db
        , ''"summary_report"
        , date                  = Date      (offset = 0)
        , user                  = Link      ("user")
        , department            = Link      ("department")
        , supervisor            = Link      ("user")
        , org_location          = Link      ("org_location")
        , time_wp               = Link      ("time_wp")
        , time_wp_group         = Link      ("time_wp_group")
        , cost_center           = Link      ("cost_center")
        , cost_center_group     = Link      ("cost_center_group")
        , time_project          = Link      ("time_project")
        , summary_type          = Link      ("summary_type")
        , summary               = Boolean   ()
        , status                = Link      ("daily_record_status")
        , show_empty            = Boolean   ()
        , show_all_users        = Boolean   ()
        , planned_effort        = Number    ()
        , show_missing          = Boolean   ()
        , all_in                = Boolean   ()
        , op_project            = Boolean   ()
        )

    summary_type = Class \
        ( db
        , ''"summary_type"
        , name                  = String    ()
        , is_staff              = Boolean   ()
        , order                 = Number    ()
        )
    summary_type.setkey ("name")

    time_activity = Class \
        ( db
        , ''"time_activity"
        , name                  = String    ()
        , description           = String    ()
        , travel                = Boolean   ()
        )
    time_activity.setkey ("name")

    time_project = Class \
        ( db
        , ''"time_project"
        , name                  = String    ()
        , description           = String    ()
        , responsible           = Link      ("user")
        , deputy                = Link      ("user")
        , organisation          = Link      ("organisation")
        , department            = Link      ("department")
        , planned_effort        = Number    ()
        , status                = Link      ("time_project_status")
        , work_location         = Link      ("work_location")
        , max_hours             = Number    ()
        , nosy                  = Multilink ("user")
        , op_project            = Boolean   ()
        , no_overtime           = Boolean   ()
        , is_public_holiday     = Boolean   ()
        )
    time_project.setkey ("name")

    time_project_status = Class \
        ( db
        , ''"time_project_status"
        , name                  = String    ()
        , description           = String    ()
        , active                = Boolean   ()
        )
    time_project_status.setkey ("name")

    time_record = Class \
        ( db
        , ''"time_record"
        , daily_record          = Link      ("daily_record",  do_journal = "no")
        , start                 = String    (indexme = "no")
        , end                   = String    (indexme = "no")
        , start_generated       = Boolean   ()
        , end_generated         = Boolean   ()
        , duration              = Number    ()
        , tr_duration           = Number    ()
        , wp                    = Link      ("time_wp",       do_journal = "no")
        , time_activity         = Link      ("time_activity", do_journal = "no")
        , work_location         = Link      ("work_location", do_journal = "no")
        , comment               = String    (indexme = "no")
        , dist                  = Number    ()
        )

    time_wp = Class \
        ( db
        , ''"time_wp"
        , name                  = String    ()
        , wp_no                 = String    ()
        , description           = String    ()
        , responsible           = Link      ("user")
        , project               = Link      ("time_project")
        , time_start            = Date      (offset = 0)
        , time_end              = Date      (offset = 0)
        , planned_effort        = Number    ()
        , bookers               = Multilink ("user")
        , durations_allowed     = Boolean   ()
        , cost_center           = Link      ("cost_center")
        , travel                = Boolean   ()
        )

    time_wp_group = Class \
        ( db
        , ''"time_wp_group"
        , name                  = String    ()
        , description           = String    ()
        , wps                   = Multilink ("time_wp")
        )
    time_wp_group.setkey ("name")

    overtime_period = Class \
        ( db
        , ''"overtime_period"
        , name                  = String    ()
        , order                 = Number    ()
        )
    overtime_period.setkey ("name")

    user_dynamic = Class \
        ( db
        , ''"user_dynamic"
        , user                  = Link      ("user")
        , valid_from            = Date      (offset = 0)
        , valid_to              = Date      (offset = 0)
        , booking_allowed       = Boolean   ()
        , travel_full           = Boolean   ()
        , durations_allowed     = Boolean   ()
        , weekend_allowed       = Boolean   ()
        , vacation_remaining    = Number    ()
        , vacation_yearly       = Number    ()
        , daily_worktime        = Number    ()
        , weekly_hours          = Number    ()
        , supp_weekly_hours     = Number    ()
        , supp_per_period       = Number    ()
        , hours_mon             = Number    ()
        , hours_tue             = Number    ()
        , hours_wed             = Number    ()
        , hours_thu             = Number    ()
        , hours_fri             = Number    ()
        , hours_sat             = Number    ()
        , hours_sun             = Number    ()
        , org_location          = Link      ("org_location")
        , department            = Link      ("department")
        , all_in                = Boolean   ()
        , additional_hours      = Number    ()
        , overtime_period       = Link      ("overtime_period")
        )

    work_location = Class \
        ( db
        , ''"work_location"
        , code                  = String    ()
        , description           = String    ()
        )
    work_location.setkey ("code")
# end def init

    #
    # SECURITY SETTINGS
    #
    # See the configuration and customisation document for information
    # about security setup.
    # Assign the access and edit Permissions for issue, file and message
    # to regular users now

def security (db, ** kw) :
    roles = \
        [ ("Project",      "Project Office")
        , ("Project_View", "May view project data")
        ]

    #     classname
    # allowed to view   /  edit
    # For daily_record, time_record, additional restrictions apply
    classes = \
        [ ( "cost_center"
          , ["User"]
          , ["Controlling"]
          )
        , ( "cost_center_group"
          , ["User"]
          , ["Controlling"]
          )
        , ( "cost_center_status"
          , ["User"]
          , ["Controlling"]
          )
        , ( "daily_record"
          , ["User"]
          , []
          )
        , ( "daily_record_status"
          , ["User"]
          , []
          )
        , ( "public_holiday"
          , ["User"]
          , ["HR", "Controlling"]
          )
        , ( "summary_report"
          , ["User"]
          , []
          )
        , ( "summary_type"
          , ["User"]
          , []
          )
        , ( "time_activity"
          , ["User"]
          , ["Controlling"]
          )
        , ( "time_project_status"
          , ["User"]
          , ["Project"]
          )
        , ( "time_project"
          , ["Project_View", "Project", "Controlling"]
          , ["Project"]
          )
        , ( "time_record"
          , ["HR", "Controlling"]
          , ["HR", "Controlling"]
          )
        , ( "time_wp_group"
          , ["User"]
          , ["Project"]
          )
        , ( "time_wp"
          , ["Project_View", "Project", "Controlling"]
          , ["Project"]
          )
        , ( "user_dynamic"
          , ["HR"]
          , []
          )
        , ( "work_location"
          , ["User"]
          , ["Controlling"]
          )
        , ( "overtime_correction"
          , ["HR", "Controlling"]
          , []
          )
        , ( "daily_record_freeze"
          , ["HR", "Controlling"]
          , []
          )
        , ( "overtime_period"
          , ["User"]
          , []
          )
        ]

    prop_perms = \
        [ ( "time_wp",      "Edit", ["Controlling"]
          , ( "project",)
          )
        , ( "daily_record", "Edit", ["HR", "Controlling"]
          , ("status", "time_record")
          )
        , ( "daily_record", "Edit", ["HR"]
          , ("required_overtime", "weekend_allowed")
          )
        ]

    schemadef.register_roles             (db, roles)
    schemadef.register_class_permissions (db, classes, prop_perms)

    # For the following the use is regulated by auditors.
    db.security.addPermissionToRole ('User', 'Create', 'time_record')
    db.security.addPermissionToRole ('User', 'Create', 'daily_record')

    fixdoc = schemadef.security_doc_from_docstring

    def approver_daily_record (db, userid, itemid) :
        """User is allowed to edit daily record if he is supervisor.

           A negative itemid indicates that the record doesn't exits
           yet -- we allow creation in this case. Modification is only
           allowed by the supervisor.
        """
        if int (itemid) < 0 : # allow creation
            return True
        ownerid   = db.daily_record.get (itemid, 'user')
        if not ownerid :
            return False
        clearance = clearance_by (db, ownerid)
        return userid in clearance
    # end def approver_daily_record

    def ok_daily_record (db, userid, itemid) :
        """User is allowed to edit daily record if he is owner or
           supervisor.

           Determine if the user owns the daily record, a negative itemid
           indicates that the record doesn't exits yet -- we allow creation
           in this case. Modification is also allowed by the supervisor or
           the person to whom approvals are delegated.
        """
        ownerid   = db.daily_record.get (itemid, 'user')
        return userid == ownerid or approver_daily_record (db, userid, itemid)
    # end def ok_daily_record

    def own_time_record (db, userid, itemid) :
        """User may edit own time_records.

           Determine if the user owns the daily record, a negative itemid
           indicates that the record doesn't exits yet -- we allow creation
           in this case.
        """
        if int (itemid) < 0 : # allow creation
            return True
        dr      = db.time_record.get  (itemid, 'daily_record')
        ownerid = db.daily_record.get (dr, 'user')
        return userid == ownerid
    # end def own_time_record

    def may_see_time_record (db, userid, itemid) :
        """User is allowed to see time record if he is allowed to see
           all details on work package or 
        """
        dr = db.time_record.get (itemid, 'daily_record')
        wp = db.time_record.get (itemid, 'wp')
        if sum_common.daily_record_viewable (db, userid, dr) :
            return True
        if wp is None :
            return False
        return sum_common.time_wp_viewable (db, userid, wp)
    # end def may_see_time_record

    def is_project_owner_of_wp (db, userid, itemid) :
        """User is allowed to edit workpackage if he is time category
           owner.
        """
        if int (itemid) < 0 :
            return False
        prid    = db.time_wp.get (itemid, 'project')
        project = db.time_project.getnode (prid)
        return userid == project.responsible
    # end def is_project_owner_of_wp

    def ok_work_package (db, userid, itemid) :
        """User is allowed to view/edit workpackage if he is owner or project
           responsible/deputy.

           Check if user is responsible for wp or if user is responsible
           for project or is the deputy for project
        """
        if int (itemid) < 0 :
            return False
        ownerid = db.time_wp.get (itemid, 'responsible')
        if ownerid == userid :
            return True
        prid    = db.time_wp.get (itemid, 'project')
        project = db.time_project.getnode (prid)
        return userid == project.responsible or userid == project.deputy
    # end def ok_work_package

    def time_project_responsible_and_open (db, userid, itemid) :
        """ User is allowed to edit time category if the status is
            "Open" and he is responsible for the time category.

            Check if the user is responsible for the given time_project
            if yes *and* the time_project is in status open, the user
            may edit several fields.
        """
        if int (itemid) < 0 :
            return False
        ownerid = db.time_project.get (itemid, 'responsible')
        open    = db.time_project_status.lookup ('Open')
        status  = db.time_project.get (itemid, 'status')
        if ownerid == userid and status == open :
            return True
        return False
    # end def time_project_responsible_and_open

    def approval_for_time_record (db, userid, itemid) :
        """User is allowed to view time record if he is the supervisor
           or the person to whom approvals are delegated.

           Viewing is allowed by the supervisor or the person to whom
           approvals are delegated.
        """
        dr        = db.time_record.get  (itemid, 'daily_record')
        ownerid   = db.daily_record.get (dr, 'user')
        clearance = clearance_by (db, ownerid)
        return userid in clearance
    # end def approval_for_time_record

    def overtime_thawed (db, userid, itemid) :
        """User is allowed to edit overtime correction if the overtime
           correction is not frozen.

           Check that no daily_record_freeze is active at date
        """
        oc = db.overtime_correction.getnode (itemid)
        return not frozen (db, oc.user, oc.date)
    # end def overtime_thawed

    def dr_freeze_last_frozen (db, userid, itemid) :
        """User is allowed to edit freeze record if not frozen at the
           given date.

           Check that no daily_record_freeze is active after date
        """
        df = db.daily_record_freeze.getnode (itemid)
        return not frozen (db, df.user, df.date + Interval ('1d'))
    # end def dr_freeze_last_frozen

    def dynuser_thawed (db, userid, itemid) :
        """User is allowed to edit dynamic user data if not frozen in
           validity span of dynamic user record
        """
        dyn = db.user_dynamic.getnode (itemid)
        return not frozen (db, dyn.user, dyn.valid_from)
    # end def dynuser_thawed

    def wp_admitted (db, userid, itemid) :
        """User is allowed to view selected fields in work package if
           booking is allowed for this user
        """
        bookers = db.time_wp.get (itemid, 'bookers')
        if not bookers or userid in bookers :
            return True
        return False
    # end def wp_admitted

    def project_admitted (db, userid, itemid) :
        """User is allowed to view selected fields if booking is allowed
           for at least one work package for this user
        """
        wps = db.time_wp.filter (None, dict (project = itemid))
        for wp in wps :
            if wp_admitted (db, userid, wp) :
                return True
        return False
    # end def project_admitted

    def project_or_wp_name_visible (db, userid, itemid) :
        """User is allowed to view work package and time category names
           if he/she is department manager or supervisor or has role HR.
        """
        if common.user_has_role (db, userid, 'HR') :
            return True
        if db.department.filter (None, dict (manager = userid)) :
            return True
        if db.user.filter (None, dict (supervisor = userid)) :
            return True
    # end def project_or_wp_name_visible

    p = db.security.addPermission \
        ( name        = 'Edit'
        , klass       = 'time_wp'
        , check       = ok_work_package
        , description = fixdoc (ok_work_package.__doc__)
        , properties  = \
            ( 'description'
            , 'time_start', 'time_end', 'bookers', 'planned_effort'
            )
        )
    db.security.addPermissionToRole ('User', p)

    p = db.security.addPermission \
        ( name        = 'View'
        , klass       = 'time_wp'
        , check       = sum_common.time_wp_viewable
        , description = fixdoc (sum_common.time_wp_viewable.__doc__)
        )
    db.security.addPermissionToRole ('User', p)

    p = db.security.addPermission \
        ( name        = 'Edit'
        , klass       = 'time_wp'
        , check       = is_project_owner_of_wp
        , description = fixdoc (is_project_owner_of_wp.__doc__)
        , properties  = ('name', 'responsible', 'wp_no', 'cost_center')
        )
    db.security.addPermissionToRole ('User', p)

    p = db.security.addPermission \
        ( name        = 'Edit'
        , klass       = 'time_project'
        , check       = time_project_responsible_and_open
        , description = fixdoc (time_project_responsible_and_open.__doc__)
        , properties  = ('deputy', 'description', 'planned_effort', 'nosy')
        )
    db.security.addPermissionToRole ('User', p)

    for perm in 'View', 'Edit' :
        p = db.security.addPermission \
            ( name        = perm
            , klass       = 'daily_record'
            , check       = ok_daily_record
            , description = fixdoc (ok_daily_record.__doc__)
            , properties  = ('status', 'time_record')
            )
        db.security.addPermissionToRole ('User', p)

        p = db.security.addPermission \
            ( name        = perm
            , klass       = 'daily_record'
            , check       = approver_daily_record
            , description = fixdoc (approver_daily_record.__doc__)
            , properties  = ('required_overtime',)
            )
        #db.security.addPermissionToRole ('User', p)

        p = db.security.addPermission \
            ( name        = perm
            , klass       = 'time_record'
            , check       = own_time_record
            , description = fixdoc (own_time_record.__doc__)
            )
        db.security.addPermissionToRole ('User', p)

    p = db.security.addPermission \
        ( name        = 'View'
        , klass       = 'time_record'
        , check       = approval_for_time_record
        , description = fixdoc (approval_for_time_record.__doc__)
        )
    db.security.addPermissionToRole ('User', p)
    p = db.security.addPermission \
        ( name        = 'View'
        , klass       = 'time_record'
        , check       = may_see_time_record
        , description = ' '.join
            (( fixdoc (may_see_time_record.__doc__)
             , fixdoc (sum_common.daily_record_viewable.__doc__)
            ))
        )
    db.security.addPermissionToRole ('User', p)
    p = db.security.addPermission \
        ( name        = 'Edit'
        , klass       = 'overtime_correction'
        , check       = overtime_thawed
        , description = fixdoc (overtime_thawed.__doc__)
        )
    db.security.addPermissionToRole ('HR', p)
    db.security.addPermissionToRole ('HR', 'Create', 'overtime_correction')
    p = db.security.addPermission \
        ( name        = 'Edit'
        , klass       = 'daily_record_freeze'
        , check       = dr_freeze_last_frozen
        , description = fixdoc (dr_freeze_last_frozen.__doc__)
        , properties  = ('frozen',)
        )
    db.security.addPermissionToRole ('HR', p)
    db.security.addPermissionToRole ('HR', 'Create', 'daily_record_freeze')
    p = db.security.addPermission \
        ( name        = 'Edit'
        , klass       = 'user_dynamic'
        , check       = dynuser_thawed
        , description = fixdoc (dynuser_thawed.__doc__)
        )
    db.security.addPermissionToRole ('HR', p)
    db.security.addPermissionToRole ('HR', 'Create', 'user_dynamic')
    p = db.security.addPermission \
        ( name        = 'View'
        , klass       = 'time_wp'
        , check       = wp_admitted
        , description = fixdoc (wp_admitted.__doc__)
        , properties  =
            ( 'name', 'wp_no', 'description', 'responsible', 'project'
            , 'time_start', 'time_end', 'durations_allowed', 'travel'
            , 'cost_center', 'creation', 'creator', 'activity', 'actor'
            )
        )
    db.security.addPermissionToRole ('User', p)
    p = db.security.addPermission \
        ( name        = 'View'
        , klass       = 'time_project'
        , check       = sum_common.time_project_viewable
        , description = fixdoc (sum_common.time_project_viewable.__doc__)
        )
    db.security.addPermissionToRole ('User', p)
    p = db.security.addPermission \
        ( name        = 'View'
        , klass       = 'time_project'
        , check       = project_admitted
        , description = fixdoc (project_admitted.__doc__)
        , properties  =
            ( 'name', 'description', 'responsible', 'deputy', 'organisation'
            , 'department', 'status', 'work_location', 'op_project'
            , 'is_public_holiday', 'creation', 'creator', 'activity', 'actor'
            )
        )
    db.security.addPermissionToRole ('User', p)
    for klass in 'time_project', 'time_wp' :
        p = db.security.addPermission \
            ( name        = 'View'
            , klass       = klass
            , check       = project_or_wp_name_visible
            , description = fixdoc (project_or_wp_name_visible.__doc__)
            , properties  = ('name', 'project')
            )
        db.security.addPermissionToRole ('User', p)
# end def security
