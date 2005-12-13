# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004 TTTech Computertechnik AG. All rights reserved
# Schönbrunnerstraße 7, A--1040 Wien, Austria. office@mexx.mobile
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
#    schema
#
# Purpose
#    Specify the DB-Schema for the tttech2 issue tracker.
#
# Revision Dates
#    22-Jun-2004 (MPH) Creation
#     5-Jul-2004 (MPH) Work in progress.
#     6-Jul-2004 (MPH) Added `closed-obsolete` to `work_package_status`.
#    23-Jul-2004 (MPH) Removed `automatic` status changes from `feature_status`
#     5-Oct-2004 (MPH) Split `work_package` into `implementation_task` and
#                      `documentation_task`
#    14-Oct-2004 (pr) Major changes
#                      - `task` with `task_kind` instead of `*_task` and
#                        `testcase`
#                      - added `estimated_[begin|end]` to task
#                      - added `task` link to `defect` and vice versa, to
#                        have to possibility to add defects also to tasks
#                      - added `defects` multilink to `feature` (was missing)
#                      - cleanup of unused classes
#     4-Nov-2004 (MPH) Effort: `Interval` -> `Number`
#     8-Nov-2004 (MPH) Cleanup, removed `accepted-but-defects` from
#                      `document_status`
#     9-Nov-2004 (MPH) Added `completed-but-defects` to `feature_status`
#    16-Nov-2004 (MPH) Added `May Public Queries` permission to `query`
#     1-Dec-2004 (MPH) Added `is_alias` to Class `user`
#     5-Apr-2005 (MPH) Added `composed_of` and `part_of` to `feature`, added
#                      support for Online Peer Reviews
#     6-Apr-2005 (RSC) Factored from dbinit.py for roundup 0.8.2
#                      "May Public Queries"->"May publish Queries"
#    11-Apr-2005 (MPH) Fixed Multilink in `review` and `announcement` to link
#                      to `file` instead of `files`
#     6-Jun-2005 (RSC) Incorporate changes from dbinit.py
#     8-Jun-2005 (RSC) time_record and time_wp added.
#                      IssueClass used directly
#    15-Jun-2005 (RSC) i18n stuff for name translations
#    22-Jun-2005 (RSC) schema additions for time-tracking
#    22-Jun-2005 (RSC) schema additions for time-tracking
#                      moved some comments in the class definition into
#                      the extensions/help.py
#    ««revision-date»»···
#--
#

import sys, os
sys.path.insert (0, os.path.join (db.config.HOME, 'lib'))
from common import clearance_by
del sys.path [0]

class TTT_Issue_Class (Class, IssueClass) :
    """extends the IssueClass with some parameters common to all issues here
    at TTTech.
    Note: inheritance methodology stolen from roundup/backends/back_anydbm.py's
          IssueClass ;-)
    """
    def __init__ (self, db, classname, ** properties) :
        if not properties.has_key ("title") :
            properties ["title"]       = String    (indexme = "yes")
        if not properties.has_key ("responsible") :
            properties ["responsible"] = Link      ("user")
        if not properties.has_key ("nosy") :
            properties ["nosy"]        = Multilink ("user", do_journal = "no")
        if not properties.has_key ("messages") :
            properties ["messages"]    = Multilink ("msg")
        Class.__init__ (self, db, classname, ** properties)
    # end def __init__
# end class TTT_Issue_Class

# Helper classes
# Class automatically gets these properties:
#   creation = Date ()
#   activity = Date ()
#   creator  = Link ('user')
# Note: without "order" they get sorted by the key, "name" or "title" or
#       the alphabetically "first" attribute.
query = Class \
    ( db
    , ''"query"
    , klass                 = String    ()
    , name                  = String    ()
    , url                   = String    ()
    , private_for           = Link      ('user')
    )

milestone_class = Class \
    ( db
    , ''"milestone"
    , name                  = String    ()
    , description           = String    ()
    , planned               = Date      ()
    , reached               = Date      ()
    , order                 = Number    ()
    # the release this milestone belongs to - needed for reactors
    # updating the releases "status" field,  which represents the last
    # reached milestone.
    , release               = Link      ("release")
    )

task_status = Class \
    ( db
    , ''"task_status"
    , name                  = String    ()
    , description           = String    ()
    , abbreviation          = String    ()
    , transitions           = Multilink ("task_status")
    , order                 = String    ()
    )
task_status.setkey ("name")

task_kind = Class \
    ( db
    , ''"task_kind"
    , name                  = String    ()
    , description           = String    ()
    , order                 = String    ()
    )
task_kind.setkey ("name")

feature_status = Class \
    ( db
    , ''"feature_status"
    , name                  = String    ()
    , description           = String    ()
    , abbreviation          = String    ()
    , transitions           = Multilink ("feature_status")
    , order                 = String    ()
    )
feature_status.setkey ("name")

defect_status = Class \
    ( db
    , ''"defect_status"
    , name                  = String    ()
    , description           = String    ()
    , abbreviation          = String    ()
    , cert                  = Boolean   ()
    , cert_transitions      = Multilink ("defect_status")
    , transitions           = Multilink ("defect_status")
    , order                 = String    ()
    )
defect_status.setkey ("name")

action_item_status = Class \
    ( db
    , ''"action_item_status"
    , name                  = String    ()
    , description           = String    ()
    , order                 = String    ()
    )
action_item_status.setkey ("name")

review_status = Class \
    ( db
    , ''"review_status"
    , name                  = String    ()
    , description           = String    ()
    , order                 = String    ()
    )
review_status.setkey ("name")

comment_status = Class \
    ( db
    , ''"comment_status"
    , name                  = String    ()
    , description           = String    ()
    , transitions           = Multilink ("comment_status")
    , order                 = String    ()
    )
comment_status.setkey ("name")

document_status = Class \
    ( db
    , ''"document_status"
    , name                  = String    ()
    , description           = String    ()
    , abbreviation          = String    ()
    , transitions           = Multilink ("document_status")
    , order                 = String    ()
    )
document_status.setkey ("name")

document_type = Class \
    ( db
    , ''"document_type"
    , name                  = String    ()
    , description           = String    ()
    , order                 = String    ()
    )
document_type.setkey ("name")

severity = Class \
    ( db
    , ''"severity"
    , name                  = String    ()
    , order                 = String    ()
    )
severity.setkey ("name")

product = Class \
    ( db
    , ''"product"
    , name                  = String    ()
    , description           = String    ()
    , responsible           = Link      ("user")
    , nosy                  = Multilink ("user")
    # needs to be set, to let the "defect report" mechanism allow to
    # mark some defect against a specific product as belonging to
    # "cert".
    , certifiable           = Boolean   ()
    # XXX: no "order", gets sorted by "name" automatically.
    )
product.setkey ("name")

organisation = Class \
    ( db
    , ''"organisation"
    , name                  = String    ()
    , description           = String    ()
    # get automatically appended to the users mail address upon creation
    # of a new user.
    , mail_domain           = String    ()
    , valid_from            = Date      ()
    , valid_to              = Date      ()
    , domain_part           = String    ()
    , messages              = Multilink ("msg")
    )
organisation.setkey ("name")

location = Class \
    ( db
    , ''"location"
    , name                  = String    ()
    , address               = String    ()
    , country               = String    ()
    , domain_part           = String    ()
    )
location.setkey ("name")

org_location = Class \
    ( db
    , ''"org_location"
    , name                  = String    ()
    , phone                 = String    ()
    , organisation          = Link      ("organisation")
    , location              = Link      ("location")
    , smb_domain            = Link      ("smb_domain")
    , dhcp_server           = Link      ("machine_name")
    , domino_dn             = String    ()
    )
org_location.setkey ("name")

room = Class \
    ( db
    , ''"room"
    , name                  = String    ()
    , location              = Link      ("location")
    )
room.setkey ("name")

meeting_room = Class \
    ( db
    , ''"meeting_room"
    , name                  = String    ()
    , room                  = Link      ("room")
    )
meeting_room.setkey ("name")

cost_center_group = Class \
    ( db
    , ''"cost_center_group"
    , name                  = String    ()
    , description           = String    ()
    , responsible           = Link      ("user")
    , active                = Boolean   ()
    )
cost_center_group.setkey ("name")

department = Class \
    ( db
    , ''"department"
    , name                  = String    ()
    , description           = String    ()
    , manager               = Link      ("user")
    , part_of               = Link      ("department")
    , doc_num               = String    ()
    , valid_from            = Date      ()
    , valid_to              = Date      ()
    , messages              = Multilink ("msg")
    )
department.setkey ("name")

position = Class \
    ( db
    , ''"position"
    , position              = String    ()
    )
position.setkey ("position")

time_project_status = Class \
    ( db
    , ''"time_project_status"
    , name                  = String    ()
    , description           = String    ()
    , active                = Boolean   ()
    )
time_project_status.setkey ("name")

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
    )
time_project.setkey ("name")

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

work_location = Class \
    ( db
    , ''"work_location"
    , code                  = String    ()
    , description           = String    ()
    )
work_location.setkey ("code")

daily_record_status = Class \
    ( db
    , ''"daily_record_status"
    , name                  = String    ()
    , description           = String    ()
    )
daily_record_status.setkey ("name")

daily_record = Class \
    ( db
    , ''"daily_record"
    , user                  = Link      ("user",          do_journal = "no")
    , date                  = Date      (offset = 0)
    , status                = Link      ( "daily_record_status"
                                        , do_journal = "no"
                                        )
    , time_record           = Multilink ("time_record",   do_journal = "no")
    )

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

time_activity = Class \
    ( db
    , ''"time_activity"
    , name                  = String    ()
    , description           = String    ()
    , travel                = Boolean   ()
    )
time_activity.setkey ("name")

time_wp_group = Class \
    ( db
    , ''"time_wp_group"
    , name                  = String    ()
    , description           = String    ()
    , wps                   = Multilink ("time_wp")
    )
time_wp_group.setkey ("name")

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

cost_center_status = Class \
    ( db
    , ''"cost_center_status"
    , name                  = String    ()
    , description           = String    ()
    , active                = Boolean   ()
    )
cost_center_status.setkey ("name")

public_holiday = Class \
    ( db
    , ''"public_holiday"
    , name                  = String    ()
    , description           = String    ()
    , date                  = Date      (offset = 0)
    , locations             = Multilink ("location")
    , is_half               = Boolean   ()
    )

sex = Class \
    ( db
    , ''"sex"
    , name                  = String    ()
    )
sex.setkey ("name")

user_status = Class \
    ( db
    , ''"user_status"
    , name                  = String    ()
    , description           = String    ()
    )
user_status.setkey ("name")

# Note: roles is a comma-separated string of Role names
user = Class \
    ( db
    , ''"user"
    , username              = String    ()
    , nickname              = String    ()
    , password              = Password  ()
    , address               = String    ()
    , alternate_addresses   = String    ()
    , status                = Link      ("user_status")
    , firstname             = String    ()
    , lastname              = String    ()
    , realname              = String    ()
    , phone                 = String    ()
    , external_phone        = String    ()
    , private_phone         = String    ()
    , supervisor            = Link      ("user")
    , substitute            = Link      ("user")
    , subst_active          = Boolean   ()
    , clearance_by          = Link      ("user")
    , room                  = Link      ("room")
    , title                 = String    ()
    , position              = Link      ("position") # e.g. SW Developer
    , job_description       = String    ()
    , queries               = Multilink ("query")
    , roles                 = String    ()
    , timezone              = String    ()
    , pictures              = Multilink ("file")
    , lunch_start           = String    ()
    , lunch_duration        = Number    ()
    , sex                   = Link      ("sex")
    , is_lotus_user         = Boolean   ()
    , sync_with_ldap        = Boolean   ()
    , group                 = Link      ("group")
    , secondary_groups      = Multilink ("group")
    , uid                   = Number    () #
    , home_directory        = String    () #
    , login_shell           = String    () #
    , samba_home_drive      = String    () #
    , samba_home_path       = String    () #
    , samba_kickoff_time    = Date      () #
    , samba_lm_password     = String    () #
    , samba_logon_script    = String    () #
    , samba_nt_password     = String    () #
    , samba_profile_path    = String    () #
    , samba_pwd_can_change  = Date      () #
    , samba_pwd_last_set    = Date      () #
    , samba_pwd_must_change = Date      () #
    , user_password         = String    ()
    , shadow_last_change    = Date      ()
    , shadow_min            = Number    ()
    , shadow_max            = Number    ()
    , shadow_warning        = Number    ()
    , shadow_inactive       = Number    ()
    , shadow_expire         = Date      ()
    , shadow_used           = Boolean   ()
    , org_location          = Link      ("org_location")
    , department            = Link      ("department")
    # XXX: add wiki page url in the web-template based on firstname &
    #      lastname -> why not compute this on the fly (RSC)
    # Note: email adresses could get set automatically by a detector on
    #       creation of a new user, as its always <nickname>@tttech.com,
    #       <username>@tttech.com and <firstname>.<lastname>@tttech.com.
    #       However the "tttech.com" part should be part of the
    #       "organisation" ???
    )
user.setkey ("username")

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
    , hours_mon             = Number    ()
    , hours_tue             = Number    ()
    , hours_wed             = Number    ()
    , hours_thu             = Number    ()
    , hours_fri             = Number    ()
    , hours_sat             = Number    ()
    , hours_sun             = Number    ()
    , org_location          = Link      ("org_location")
    , department            = Link      ("department")
    )

summary_type = Class \
    ( db
    , ''"summary_type"
    , name                  = String    ()
    , order                 = Number    ()
    )
summary_type.setkey ("name")

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
    , planned_effort        = Number    ()
    )

network_interface = Class \
    ( db
    , ''"network_interface"
    , mac                   = String    ()
    , card_type             = String    ()
    , description           = String    ()
    , machine               = Link      ("machine")
    )
network_interface.setkey ("mac")

machine = Class \
    ( db
    , ''"machine"
    , inventory_no          = String    ()
    , link_field            = String    ()
    , description           = String    ()
    , owner                 = Link      ("user")
    , operating_system      = Multilink ("operating_system")
    , smb_name              = String    ()
    , machine_uid           = Number    ()
    , smb_domain            = Link      ("smb_domain")
    )
machine.setkey ("inventory_no")

operating_system = Class \
    ( db
    , ''"operating_system"
    , name_version          = String    ()
    , description           = String    ()
    )
operating_system.setkey ("name_version")

network_address = Class \
    ( db
    , ''"network_address"
    , ip                    = String    ()
    , org_location          = Link      ("org_location")
    , use_dhcp              = Boolean   ()
    , network_interface     = Link      ("network_interface")
    )
network_address.setkey ("ip")

ip_subnet = Class \
    ( db
    , ''"ip_subnet"
    , ip                    = String    ()
    , netmask               = Number    ()
    , org_location          = Link      ("org_location")
    , routers               = Multilink ("machine_name")
    , dns_servers           = Multilink ("machine_name")
    , dhcp_range            = String    ()
    , default_lease_time    = Number    ()
    , max_lease_time        = Number    ()
    )

dns_record_type = Class \
    ( db
    , ''"dns_record_type"
    , name                  = String    ()
    , description           = String    ()
    )
dns_record_type.setkey ("name")

machine_name = Class \
    ( db
    , ''"machine_name"
    , name                  = String    ()
    , network_address       = Multilink ("network_address")
    , machine_name          = Multilink ("machine_name")
    , do_reverse_mapping    = Boolean   ()
    , dns_record_type       = Link      ("dns_record_type")
    )
machine_name.setkey ("name")

group = Class \
    ( db
    , ''"group"
    , name                  = String    ()
    , description           = String    ()
    , gid                   = Number    ()
    , org_location          = Link      ("org_location")
    )
group.setkey ("name")

alias = Class \
    ( db
    , ''"alias"
    , name                  = String    ()
    , description           = String    ()
    , alias_to_alias        = Multilink ("alias")
    , alias_to_user         = Multilink ("user")
    , use_in_ln             = Boolean   ()
    , org_location          = Link      ("org_location")
    )

smb_domain = Class \
    ( db
    , ''"smb_domain"
    , name                  = String    ()
    , description           = String    ()
    , sid                   = String    ()
    , pdc                   = Link      ("machine")
    , uid_range             = String    ()
    , private_gid_range     = String    ()
    , machine_uid_range     = String    ()
    , gid_range             = String    ()
    , machine_group         = Number    ()
    , last_uid              = Number    ()
    , last_gid              = Number    ()
    , last_machine_uid      = Number    ()
    , org_location          = Link      ("org_location")
    , netbios_ns            = Multilink ("machine_name")
    , netbios_dd            = Link      ("machine_name")
    , netbios_nodetype      = String    ()
    )
smb_domain.setkey ("name")

# FileClass automatically gets these properties:
#   content = String()    [saved to disk in <tracker home>/db/files/]
#   (it also gets the Class properties creation, activity and creator)
msg = FileClass \
    ( db
    , ''"msg"
    , date                  = Date      ()
    , files                 = Multilink ("file")
    # Note: below fields are used by roundup internally (obviously by the
    #       mail-gateway)
    , author                = Link      ("user", do_journal='no')
    , recipients            = Multilink ("user", do_journal='no')
    , summary               = String    ()
    , messageid             = String    ()
    , inreplyto             = String    ()
    )

file = FileClass \
    ( db
    , ''"file"
    , name                  = String    ()
    , type                  = String    ()
    )

# TTT_Issue_Class automatically gets these properties:
#   title       = String    ()
#   responsible = Link      ("user")
#   nosy        = Multilink ("user")
#   messages    = Multilink ("msg")
#   (it also gets the Class properties creation, activity and creator)

meeting = TTT_Issue_Class \
    ( db
    , ''"meeting"
    , files                 = Multilink ("file")
    )

action_item = TTT_Issue_Class \
    ( db
    , ''"action_item"
    , files                 = Multilink ("file")
    , meeting               = Link      ("meeting")
    , status                = Link      ("action_item_status")
    , deadline              = Date      ()
    )

document = TTT_Issue_Class \
    ( db
    , ''"document"
    , files                 = Multilink ("file")
    , status                = Link      ("document_status")
    , release               = Link      ("release")
    , type                  = Link      ("document_type")
    )

release = TTT_Issue_Class \
    ( db
    , ''"release"
    # just to show something in the pop-up, gets set to the last reached
    # milestone
    , status                = Link      ("milestone")
    , documents             = Multilink ("document")
    , features              = Multilink ("feature")
    , planned_fixes         = Multilink ("defect")
    , bugs                  = Multilink ("defect")
    # Note: they get added automatically on creation of a new release
    # (by the auditor -
    , milestones            = Multilink ("milestone")
    )

feature = TTT_Issue_Class \
    ( db
    , ''"feature"
    , stakeholder           = String    () # some freeform text
    # note: "status" is simplified to be only one of "raised",
    #       "suspended", "open" and "completed", all other *.accepted
    #       states can be computed directly from the status of the
    #       attached issues.
    #       There is now a seperate flag "test_ok" which covers the state
    #       of the testcases, and gets set automatically by a detector
    #       when the "test_ok" flag of some attached "testcase" changes.
    #       Changes to the "testcase"s "test_ok" are only allowed by the
    #       iv&v team, and are set manually at begin and later on this
    #       should be automatically, based on the success of a given
    #       testcase (identified by the issue no.).
    , status                = Link      ("feature_status")
    # gets set automatically by a detector depending on the testcases
    # test_ok switch:
    , test_ok               = Boolean   ()
    , tasks                 = Multilink ("task")
    , depends               = Multilink ("feature")
    , needs                 = Multilink ("feature")
    , release               = Link      ("release")
    , defects               = Multilink ("defect")
    , composed_of           = Multilink ("feature")
    , part_of               = Link      ("feature")
    , planned_begin         = Date      () # automatically by import
    , planned_end           = Date      () # automatically by import
    , actual_begin          = Date      () # automatically by status
    , actual_end            = Date      () # change of workpackages
    )

task = TTT_Issue_Class \
    ( db
    , ''"task"
    , status                = Link      ("task_status")
    , kind                  = Link      ("task_kind")
    , effort                = Number    () # not Interval, as it's
                                           # actually in workingdays
    , depends               = Multilink ("task")
    , needs                 = Multilink ("task")
    , files                 = Multilink ("file")
    , feature               = Link      ("feature")
    , defects               = Multilink ("defect")
    , test_ok               = Boolean   () # if kind == "testcase"
    , planned_begin         = Date      () #
    , planned_end           = Date      () # == durchlaufzeit 5d
    , actual_begin          = Date      () #
    , actual_end            = Date      () # == tatsächliche dauer 2h
    , estimated_begin       = Date      () #
    , estimated_end         = Date      () # == geschätze dauer 8w
    )

defect = TTT_Issue_Class \
    ( db
    , ''"defect"
    , status                = Link      ("defect_status")
    , superseder            = Link      ("defect")
    , cert                  = Boolean   ()
    # in which "release" it gets repaired.  i.e. it is in the
    # "planned_fixes" of that release:
    , solved_in_release     = Link      ("release")
    # where it was initially found.  "solved_in_release" is initially
    # set to "found_in_release":
    , found_in_release      = Link      ("release")
    , estimated_effort      = Number    ()
    # currently optional, but the opinions differ if it is generally
    # good to only say how long does it take, or to give some point in
    # time where it is actually fixed... mph thinks that the
    # estimated_effort is best - and gives some rough estimation on how
    # much time we actually need to add for big-fixing. in tal's opinion
    # it is important to know when it will be ready. but the past showed
    # that "deadlines" in general are a bad idea - as they always point
    # to some point back in time ;):
    , fixed_until           = Date      ()
    , severity              = Link      ("severity")
    , product               = Link      ("product")
    , version               = String    ()
    , files                 = Multilink ("file")
    , fixed_in              = String    ()
    , files_affected        = String    () # XXX only cert ???
    , closed                = Date      ()
    # if it opens again, than we have a shortcut to who actually closed
    # it last time. as we are also setting the "closed" date for this,
    # we can also set the "closer" here:
    , closer                = Link      ("user")
    , belongs_to_feature    = Link      ("feature") # if known
    , belongs_to_task       = Link      ("task")    # if known
    )

TTT_Issue_Class \
    ( db
    , ''"review"
    # `moderator` is implemented with `responsible`
    , status                = Link      ("review_status")
    , authors               = Multilink ("user")
    , qa_representative     = Link      ("user")
    , recorder              = Link      ("user")
    , peer_reviewers        = Multilink ("user")
    , opt_reviewers         = Multilink ("user")
    , cut_off_date          = Date      ()
    , final_meeting_date    = Date      ()
    , files                 = Multilink ("file")
    , announcements         = Multilink ("announcement")
    )

TTT_Issue_Class \
    ( db
    , ''"announcement"
    , version               = String    ()
    , meeting_room          = Link      ("meeting_room")
    , comments              = Multilink ("comment")
    , review                = Link      ("review")
    , status                = Link      ("review_status")
    , files                 = Multilink ("file")
    )

TTT_Issue_Class \
    ( db
    , ''"comment"
    , severity              = Link      ("severity")
    , status                = Link      ("comment_status")
    , review                = Link      ("review")
    , announcement          = Link      ("announcement")
    , file_name             = String    ()
    , line_number           = String    ()
    )

#
# SECURITY SETTINGS
#
# See the configuration and customisation document for information
# about security setup.
# Assign the access and edit Permissions for issue, file and message
# to regular users now

# roles: user, admin, nosy, teamleader, ccb, office (to edit the users
#        only)
#     classname        allowed to view   /  edit
classes = \
    [ ("department"          , ["User"], ["Controlling"     ])
    , ("file"                , ["User"], ["User"            ])
    , ("location"            , ["User"], ["HR"              ])
    , ("meeting_room"        , ["User"], ["HR"              ])
    , ("msg"                 , ["User"], ["User"            ])
    , ("organisation"        , ["User"], ["HR","Controlling"])
    , ("org_location"        , ["User"], ["HR"              ])
    , ("position"            , ["User"], ["HR"              ])
    , ("query"               , ["User"], ["User"            ])
    , ("room"                , ["User"], ["HR"              ])
    , ("sex"                 , ["User"], ["Admin"           ])
#   , ("user"                , See below -- individual fields)
    , ("user_status"         , ["User"], ["Admin"           ])
    # Issue Tracker classes:
    # no permission for now -- once we roll this out we want it enabled.
    #, ("action_item"         , ["User"], ["User"            ])
    #, ("action_item_status"  , ["User"], ["Admin"           ])
    #, ("announcement"        , ["User"], ["User"            ])
    #, ("comment"             , ["User"], ["User"            ])
    #, ("comment_status"      , ["User"], ["Admin"           ])
    #, ("defect"              , ["User"], ["User"            ])
    #, ("defect_status"       , ["User"], ["Admin"           ])
    #, ("document"            , ["User"], ["User"            ])
    #, ("document_status"     , ["User"], ["Admin"           ])
    #, ("document_type"       , ["User"], ["Admin"           ])
    #, ("feature"             , ["User"], ["Releasemanager"  ])
    #, ("feature_status"      , ["User"], ["Admin"           ])
    #, ("meeting"             , ["User"], ["Admin"           ])
    #, ("milestone"           , ["User"], ["Releasemanager"  ])
    #, ("product"             , ["User"], ["Admin"           ])
    #, ("release"             , ["User"], ["Releasemanager"  ])
    #, ("review"              , ["User"], ["User"            ])
    #, ("review_status"       , ["User"], ["Admin"           ])
    #, ("severity"            , ["User"], ["Admin"           ])
    #, ("task"                , ["User"], ["User"            ])
    #, ("task_kind"           , ["User"], ["Admin"           ])
    #, ("task_status"         , ["User"], ["Admin"           ])
    # Time-Tracking classes
    # For daily_record, time_record, additional restrictions apply
    , ("cost_center"         , ["User"],             ["Controlling"     ])
    , ("cost_center_group"   , ["User"],             ["Controlling"     ])
    , ("cost_center_status"  , ["User"],             ["Controlling"     ])
    , ("daily_record"        , ["HR","Controlling"], ["HR","Controlling"])
    , ("daily_record_status" , ["User"],             ["Admin"           ])
    , ("public_holiday"      , ["User"],             ["HR","Controlling"])
    , ("summary_report"      , ["User"],             [                  ])
    , ("summary_type"        , ["User"],             ["Admin"           ])
    , ("time_activity"       , ["User"],             ["Controlling"     ])
    , ("time_project_status" , ["User"],             ["Project"         ])
    , ("time_project"        , ["User"],             ["Project"         ])
    , ("time_record"         , ["HR","Controlling"], ["HR","Controlling"])
    , ("time_wp_group"       , ["User"],             ["Project"         ])
    , ("time_wp"             , ["User"],             ["Project"         ])
    , ("user_dynamic"        , ["HR","Controlling"], ["HR"              ])
    , ("work_location"       , ["User"],             ["Controlling"     ])
    # System-Management classes
    , ("alias"               , ["IT", "ITView"],     ["IT"     ])
    , ("dns_record_type"     , ["IT", "ITView"],     ["Admin"  ])
    , ("group"               , ["IT", "ITView"],     ["IT"     ])
    , ("ip_subnet"           , ["IT", "ITView"],     ["IT"     ])
    , ("machine"             , ["IT", "ITView"],     ["IT"     ])
    , ("machine_name"        , ["IT", "ITView"],     ["IT"     ])
    , ("network_address"     , ["IT", "ITView"],     ["IT"     ])
    , ("network_interface"   , ["IT", "ITView"],     ["IT"     ])
    , ("operating_system"    , ["IT", "ITView"],     ["IT"     ])
    , ("smb_domain"          , ["IT", "ITView"],     ["IT"     ])
    ]

class_field_perms = \
    [ ( "location", "Edit", ["IT"]
      , ("domain_part",)
      )
    , ( "org_location", "Edit", ["IT"]
      , ("smb_domain", "dhcp_server", "domino_dn")
      )
    , ( "organisation", "Edit", ["IT"]
      , ("domain_part",)
      )
    , ( "user", "Edit", ["Admin", "HR", "IT"]
      , ( "address"
        , "alternate_addresses"
        , "nickname"
        , "password"
        , "timezone"
        , "username"
        )
      )
    , ( "user", "Edit", ["Admin", "HR"]
      , ( "clearance_by", "external_phone", "firstname"
        , "job_description", "lastname", "lunch_duration", "lunch_start"
        , "phone", "pictures", "position", "private_phone", "realname"
        , "room", "sex", "status", "subst_active", "substitute", "supervisor"
        , "title", "roles"
        )
      )
    , ( "user", "Edit", ["IT"]
      , ( "is_lotus_user", "sync_with_ldap", "group"
        , "secondary_groups", "uid", "home_directory", "login_shell"
        , "samba_home_drive", "samba_home_path", "samba_kickoff_time"
        , "samba_lm_password", "samba_logon_script", "samba_nt_password"
        , "samba_profile_path", "samba_pwd_can_change", "samba_pwd_last_set"
        , "samba_pwd_must_change", "user_password", "shadow_last_change"
        , "shadow_min", "shadow_max", "shadow_warning", "shadow_inactive"
        , "shadow_expire", "shadow_used"
        )
      )
    , ( "user", "View", ["Controlling"], ( "roles"))
    , ( "user", "View", ["User"]
      , ( "activity", "actor", "address", "alternate_addresses"
        , "clearance_by", "creation", "creator", "department"
        , "external_phone", "firstname", "job_description", "lastname"
        , "lunch_duration", "lunch_start", "nickname", "password", "phone"
        , "pictures", "position", "queries", "realname", "room", "sex"
        , "status", "subst_active", "substitute", "supervisor", "timezone"
        , "title", "username", "home_directory", "login_shell"
        , "samba_home_drive", "samba_home_path"
        )
      )
    , ( "time_wp", "Edit", ["Controlling"], ( "project",))
    ]

roles = \
    [ ("Nosy"          , "Allowed on nosy list"          )
    , ("CCB"           , "Member of Change Control Board")
    , ("Office"        , "Member of Office"              )
    , ("Releasemanager", "Allowed to manage a SW Release")
    , ("IV&V"          , "Member of the IV&V Team."      )
    , ("halfweek"      , "User works only the half week" )
    , ("HR"            , "Human Ressources team"         )
    , ("Controlling"   , "Controlling"                   )
    , ("IT"            , "IT-Department"                 )
    , ("Project"       , "Project Office"                )
    , ("ITView"        , "View but not change IT data"   )
    ]

for name, desc in roles :
    db.security.addRole (name = name, description = desc)

db.security.addPermissionToRole ('HR',   'Create', 'user')
# the following is further checked in an auditor:
db.security.addPermissionToRole ('User', 'Create', 'time_wp')

for cl, view_list, edit_list in classes :
    for viewer in view_list :
        db.security.addPermissionToRole (viewer, 'View', cl)
    for editor in edit_list :
        db.security.addPermissionToRole (editor, 'Edit',   cl)
        db.security.addPermissionToRole (editor, 'Create', cl)

# For the following the use is regulated by auditors.
db.security.addPermissionToRole ('User', 'Create', 'time_record')
db.security.addPermissionToRole ('User', 'Create', 'daily_record')

for cl, perm, roles, props in class_field_perms :
    p = db.security.addPermission \
        ( name        = perm
        , klass       = cl
        , description = "Allowed to edit this property"
        , properties  = props
        )
    for r in roles :
        db.security.addPermissionToRole (r, p)

# HR should be able to create new users:
db.security.addPermissionToRole ("HR", "Create", "user")

def own_user_record (db, userid, itemid) :
    """Determine whether the userid matches the item being accessed"""
    return userid == itemid
# end def own_user_record

def ok_daily_record (db, userid, itemid) :
    """Determine if the user owns the daily record, a negative itemid
       indicates that the record doesn't exits yet -- we allow creation
       in this case. Modification is also allowed by the supervisor or
       the person to whom approvals are delegated.
    """
    if int (itemid) < 0 : # allow creation
        return True
    ownerid   = db.daily_record.get (itemid, 'user')
    if not ownerid :
        return False
    clearance = clearance_by (db, ownerid)
    return userid == ownerid or userid in clearance
# end def ok_daily_record

def own_time_record (db, userid, itemid) :
    """Determine if the user owns the daily record, a negative itemid
       indicates that the record doesn't exits yet -- we allow creation
       in this case.
    """
    if int (itemid) < 0 : # allow creation
        return True
    dr      = db.time_record.get  (itemid, 'daily_record')
    ownerid = db.daily_record.get (dr, 'user')
    return userid == ownerid
# end def own_time_record

def is_project_owner_of_wp (db, userid, itemid) :
    """ Check if user is owner of wp """
    if int (itemid) < 0 :
        return False
    prid    = db.time_wp.get (itemid, 'project')
    project = db.time_project.getnode (prid)
    return userid == project.responsible
# end def is_project_owner_of_wp

def ok_work_package (db, userid, itemid) :
    """ Check if user is responsible for wp or if user is responsible
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

def approval_for_time_record (db, userid, itemid) :
    """Viewing is allowed by the supervisor or the person to whom
       approvals are delegated.
    """
    dr        = db.time_record.get  (itemid, 'daily_record')
    ownerid   = db.daily_record.get (dr, 'user')
    clearance = clearance_by (db, ownerid)
    return userid in clearance
# end def approval_for_time_record

p = db.security.addPermission \
    ( name        = 'Edit'
    , klass       = 'user'
    , check       = own_user_record
    , description = "User is allowed to edit (some of) their own user details"
    , properties  = \
        ( 'password', 'realname', 'phone', 'private_phone', 'external_phone'
        , 'substitute', 'subst_active', 'title', 'queries'
        , 'lunch_start', 'lunch_duration', 'room', 'timezone'
        )
    )
db.security.addPermissionToRole('User', p)

p = db.security.addPermission \
    ( name        = 'Edit'
    , klass       = 'time_wp'
    , check       = ok_work_package
    , description = "User is allowed to edit (some of) their own user wps"
    , properties  = \
        ( 'responsible', 'description', 'cost_center'
        , 'time_start', 'time_end', 'bookers', 'planned_effort'
        )
    )
db.security.addPermissionToRole('User', p)

p = db.security.addPermission \
    ( name        = 'Edit'
    , klass       = 'time_wp'
    , check       = is_project_owner_of_wp
    , description = "User is allowed to edit name and wp_no"
    , properties  = ('name', 'wp_no')
    )
db.security.addPermissionToRole('User', p)

for perm in 'View', 'Edit' :
    p = db.security.addPermission \
        ( name        = perm
        , klass       = 'daily_record'
        , check       = ok_daily_record
        , description = 'User and approver may edit daily_records'
        )
    db.security.addPermissionToRole('User', p)

    p = db.security.addPermission \
        ( name        = perm
        , klass       = 'time_record'
        , check       = own_time_record
        , description = 'User may edit own time_records'
        )
    db.security.addPermissionToRole('User', p)

p = db.security.addPermission \
    ( name        = 'View'
    , klass       = 'time_record'
    , check       = approval_for_time_record
    , description = 'Supervisor may see time record'
    )
db.security.addPermissionToRole('User', p)

# add permission "May Change Status" to role "CCB" and "Admin"
p = db.security.addPermission (name="May Change Status", klass="defect")
db.security.addPermissionToRole("CCB",   "May Change Status", "defect")
db.security.addPermissionToRole("Admin", "May Change Status", "defect")

# add permission "May publish Queries" to role "Releasemanager and "Admin"
p = db.security.addPermission (name="May publish Queries", klass="query")
db.security.addPermissionToRole \
    ("Releasemanager", "May publish Queries", "query")
db.security.addPermissionToRole \
    ("Admin",          "May publish Queries", "query")

# Add special permission for receiving nosy msgs. In this way we may
# spare in-house people from receiving notifications from roundup,
# more importantly we can add external listeners for nosy messages.
nosy_classes = [ "document"
               , "release"
               , "feature"
               , "task"
               , "defect"
               , "meeting"
               , "action_item"
               , "review"
               , "announcement"
               , "comment"
               ]
for klass in nosy_classes :
    db.security.addPermission \
        ( name        = "Nosy"
        , klass       = klass
        , description = "User may get nosy messages for %s" % klass
        )
    db.security.addPermissionToRole ("Nosy", "Nosy", klass)

# and give the regular users access to the web and email interface
db.security.addPermissionToRole ('User', 'Web Access')
db.security.addPermissionToRole ('User', 'Email Access')

# editing of roles:
for r in "Admin", "HR", "IT" :
    db.security.addPermissionToRole (r, 'Web Roles')

# oh, g'wan, let anonymous access the web interface too
# NOT really !!!
db.security.addPermissionToRole('Anonymous', 'Web Access')

