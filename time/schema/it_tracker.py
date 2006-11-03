# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004 Dr. Ralf Schlatterbeck Open Source Consulting.
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
#    it_tracker
#
# Purpose
#    Schema definitions for a simple IT Issue tracker
#
#--
#

from roundup.hyperdb import Class
import schemadef

def init \
    (db, Class, Ext_Issue_Class, String, Date, Link, Multilink, Number, ** kw) :
    it_category = Class \
        ( db
        , ''"it_category"
        , name                  = String    ()
        , description           = String    ()
        )
    it_category.setkey ("name")

    Ext_Issue_Class \
        ( db
        , ''"it_issue"
        , status                = Link      ("it_issue_status",
                                                            do_journal='no')
        , it_prio               = Link      ("it_prio",     do_journal='no')
        , category              = Link      ("it_category", do_journal='no')
        , stakeholder           = Link      ("user",        do_journal='no')
        , deadline              = Date      ()
        , files                 = Multilink ("file")
        , it_project            = Link      ("it_project")
        , superseder            = Multilink ("it_issue")
        )

    it_issue_status = Class \
        ( db
        , ''"it_issue_status"
        , name                  = String    ()
        , description           = String    ()
        , transitions           = Multilink ("it_issue_status")
        , order                 = Number    ()
        )
    it_issue_status.setkey ("name")

    it_prio = Class \
        ( db
        , ''"it_prio"
        , name                  = String    ()
        , order                 = Number    ()
        )
    it_prio.setkey ("name")

    Ext_Issue_Class \
        ( db
        , ''"it_project"
        , status                = Link      ("it_project_status",
                                                            do_journal = 'no')
        , it_prio               = Link      ("it_prio",     do_journal = 'no')
        , category              = Link      ("it_category", do_journal = 'no')
        , stakeholder           = Link      ("user",        do_journal = 'no')
        , deadline              = Date      ()
        , files                 = Multilink ("file")
        )

    it_project_status = Class \
        ( db
        , ''"it_project_status"
        , name                  = String    ()
        , description           = String    ()
        , transitions           = Multilink ("it_project_status")
        , order                 = Number    ()
        )
    it_project_status.setkey ("name")
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
        [ ("IT"            , "IT-Department"                 )
        , ("ITView"        , "View but not change IT data"   )
        ]

    #     classname        allowed to view   /  edit
    classes = \
        [ ("it_category"         , ["User"        ],     ["IT"     ])
        , ("it_issue_status"     , ["User"        ],     ["Admin"  ])
        , ("it_issue"            , ["User"        ],     ["IT"     ])
        , ("it_prio"             , ["User"        ],     ["Admin"  ])
        , ("it_project"          , ["User"        ],     ["IT"     ])
        , ("it_project_status"   , ["User"        ],     ["Admin"  ])
        ]

    prop_perms = \
        [ ( "location", "Edit", ["IT"]
          , ("domain_part",)
          )
        , ( "it_issue",   "Edit", ["User"]
          , ("messages", "files", "nosy")
          )
        , ( "it_project",   "Edit", ["User"]
          , ("messages", "files", "nosy")
          )
        , ( "org_location", "Edit", ["IT"]
          , ("smb_domain", "dhcp_server", "domino_dn")
          )
        , ( "organisation", "Edit", ["IT"]
          , ("domain_part",)
          )
        , ( "user", "Edit", ["Admin", "IT"]
          , ( "address", "alternate_addresses", "nickname"
            , "password", "timezone", "username"
            , "is_lotus_user", "sync_with_ldap", "group"
            , "secondary_groups", "uid", "home_directory", "login_shell"
            , "samba_home_drive", "samba_home_path", "samba_kickoff_time"
            , "samba_lm_password", "samba_logon_script", "samba_nt_password"
            , "samba_profile_path", "samba_pwd_can_change", "samba_pwd_last_set"
            , "samba_pwd_must_change", "user_password", "shadow_last_change"
            , "shadow_min", "shadow_max", "shadow_warning", "shadow_inactive"
            , "shadow_expire", "shadow_used"
            )
          )
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
        ]


    schemadef.register_roles             (db, roles)
    schemadef.register_class_permissions (db, classes, prop_perms)

    def responsible_or_stakeholder (db, userid, itemid) :
        """Determine whether the user is responsible for or the
           stakeholder of an issue
        """
        return \
            (  db.it_issue.get (itemid, 'responsible') == userid
            or db.it_issue.get (itemid, 'stakeholder') == userid
            )
    # end def responsible_or_stakeholder

    p = db.security.addPermission \
        ( name        = 'Edit'
        , klass       = 'it_issue'
        , check       = responsible_or_stakeholder
        , description = "Stakeholder/Responsible may edit several fields"
        , properties  = ('deadline', 'responsible', 'status', 'title')
        )
    db.security.addPermissionToRole ('User', p)

    db.security.addPermissionToRole ('User', 'Create', 'it_issue')

# end def security
