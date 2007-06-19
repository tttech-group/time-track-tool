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
#    issue
#
# Purpose
#    Schema definitions for issue tracker derived from gnats
#
#--
#

from roundup.hyperdb import Class
import schemadef

def init \
    ( db
    , Class
    , Ext_Mixin
    , Superseder_Issue_Class
    , String
    , Date
    , Link
    , Multilink
    , Number
    , Boolean
    , ** kw
    ) :
    area = Class \
        ( db, "area"
        , name                = String    (indexme = 'no')
        , description         = String    (indexme = 'no')
        )
    area.setkey ("name")

    category = Class \
        ( db, "category"
        , name                = String    (indexme = 'no')
        , description         = String    (indexme = 'no')
        , responsible         = Link      ("user")
        , nosy                = Multilink ("user")
        , valid               = Boolean   ()
        , cert_sw             = Boolean   ()
        )
    category.setkey ("name")

    kind = Class \
        ( db, "kind"
        , name                = String    (indexme = 'no')
        , description         = String    (indexme = 'no')
        )
    kind.setkey ("name")

    keyword = Class \
        ( db, "keyword"
        , name                = String    (indexme = 'no')
        , description         = String    (indexme = 'no')
        )
    keyword.setkey ("name")

    stat = Class \
        ( db, "status"
        , name                = String    (indexme = 'no')
        , description         = String    (indexme = 'no')
        , order               = String    (indexme = 'no')
        , transitions         = Multilink ("status_transition")
        )
    stat.setkey ("name")

    trans = Class \
        ( db, "status_transition"
        , target              = Link      ("status")
        , require_resp_change = Boolean   ()
        , require_msg         = Boolean   ()
        , name                = String    (indexme = 'no')
        )
    trans.setkey ("name")

    sev = Class \
        ( db, "severity"
        , name                = String    (indexme = 'no')
        , abbreviation        = String    (indexme = 'no')
        , order               = Number    ()
        )
    sev.setkey ("name")

    msg_keyword = Class \
        ( db, "msg_keyword"
        , name                = String    (indexme = 'no')
        , description         = String    (indexme = 'no')
        )
    msg_keyword.setkey("name")

    Superseder_Issue_Class \
        ( db, "issue"
        , keywords            = Multilink ("keyword",     do_journal = 'no')
        , priority            = Number    ()
        , effective_prio      = Number    ()
        , status              = Link      ("status",      do_journal = 'no')
        , closed              = Date      ()
        , release             = String    (indexme = 'no')
        , fixed_in            = String    (indexme = 'no')
        , files_affected      = String    (indexme = 'no')
        , category            = Link      ("category",    do_journal = 'no')
        , kind                = Link      ("kind",        do_journal = 'no')
        , area                = Link      ("area",        do_journal = 'no')
        , depends             = Multilink ("issue")
        , needs               = Multilink ("issue")
        , effort              = String    (indexme = 'no')
        , deadline            = Date      ()
        , earliest_start      = Date      ()
        , planned_begin       = Date      ()
        , planned_end         = Date      ()
        , cur_est_begin       = Date      () # current estimate
        , cur_est_end         = Date      () # current estimate
        , composed_of         = Multilink ("issue") # should be read only
        , part_of             = Link      ("issue") # should change composed_of
        , severity            = Link      ("severity")
        , maturity_index      = Number    ()
        , confidential        = Boolean   ()
        )

    Cls = kw ['Msg_Class']
    class Msg_Class (Cls) :
        """ extends the normal FileClass with some attributes for message
        """
        def __init__ (self, db, classname, ** properties) :
            self.update_properties \
                ( header      = String    (indexme = 'no')
                , keywords    = Multilink ("msg_keyword", do_journal = 'no')
                , subject     = String    (indexme = 'no')
                )
            self.__super.__init__ (db, classname, ** properties)
        # end def __init__
    # end class Msg_Class
    return dict (Msg_Class = Msg_Class)
# end def init

def security (db, ** kw) :
    roles = \
        [ ("Issue_Admin", "Admin for issue tracker")
        , ("Nosy",        "Allowed on nosy list")
        ]
    #     classname             allowed to view   /  edit
    classes = \
        [ ("issue",             ["Issue_Admin"], ["Issue_Admin"])
        , ("area",              ["User"],        ["Issue_Admin"])
        , ("category",          ["User"],        ["Issue_Admin"])
        , ("keyword",           ["User"],        ["Issue_Admin"])
        , ("kind",              ["User"],        ["Issue_Admin"])
        , ("msg_keyword",       ["User"],        ["Issue_Admin"])
        , ("status",            ["User"],        ["Issue_Admin"])
        , ("status_transition", ["User"],        ["Issue_Admin"])
        , ("severity",          ["User"],        ["Issue_Admin"])
        ]

    schemadef.register_roles                 (db, roles)
    schemadef.register_class_permissions     (db, classes, ())
    schemadef.register_nosy_classes          (db, ['issue'])
    db.security.addPermissionToRole          ('User', 'Create', 'issue')
    schemadef.register_confidentiality_check (db, 'issue', ('View', 'Edit'))
# end def security
