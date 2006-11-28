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
#    core
#
# Purpose
#    Schema definitions needed in any case by every tracker
#
#--
#

import schemadef

def init \
    ( db
    , Class
    , FileClass
    , Msg_Class
    , String
    , Password
    , Date
    , Link
    , Multilink
    , ** kw
    ) :
    # FileClass automatically gets these properties:
    #   content = String()    [saved to disk in <tracker home>/db/files/]
    #   (it also gets the Class properties creation, activity and creator)
    FileClass \
        ( db
        , ''"file"
        , name                  = String    (indexme = 'no')
        , type                  = String    (indexme = 'no')
        , content               = String    (indexme = 'no')
        )

    Msg_Class \
        ( db
        , ''"msg"
        , date                  = Date      ()
        , files                 = Multilink ("file")
        # Note: fields below are used by roundup internally (obviously
        #       by the mail-gateway)
        , author                = Link      ("user", do_journal='no')
        , recipients            = Multilink ("user", do_journal='no')
        , summary               = String    (indexme = 'no')
        , messageid             = String    (indexme = 'no')
        , inreplyto             = String    (indexme = 'no')
        , content               = String    (indexme = 'no')
        )

    query = Class \
        ( db
        , ''"query"
        , klass                 = String    ()
        , name                  = String    ()
        , url                   = String    ()
        , private_for           = Link      ('user')
        )

    User_Class = kw.get ('User_Class', Class)
    user = User_Class \
        ( db
        , ''"user"
        , username              = String    ()
        , password              = Password  ()
        , address               = String    ()
        , alternate_addresses   = String    ()
        , realname              = String    ()
        , phone                 = String    ()
        , queries               = Multilink ("query")
        , roles                 = String    ()
        , status                = Link      ("user_status")
        , timezone              = String    ()
        )
    user.setkey ('username')

    user_status = Class \
        ( db
        , ''"user_status"
        , name                  = String    ()
        , description           = String    ()
        )
    user_status.setkey ("name")
# end def init

def security (db, ** kw) :
    """ See the configuration and customisation document for information
        about security setup. Assign the access and edit Permissions for
        issue, file and message to regular users now
    """

    # Will have special handling for queries, see below
    #     classname        allowed to view   /  edit
    classes = \
        [ ("user_status"         , ["User"],  ["Admin"           ])
        , ("query"               , ["Admin"], ["Admin"           ])
        ]

    schemadef.register_class_permissions (db, classes, [])

    ### Query permissions ###
    def view_query (db, userid, itemid) :
        private_for = db.query.get (itemid, 'private_for')
        if not private_for : return True
        return userid == private_for
    # end def view_query

    def edit_query(db, userid, itemid):
        return userid == db.query.get(itemid, 'creator')
    # end def edit_query

    p = db.security.addPermission \
        ( name        = 'View'
        , klass       = 'query'
        , check       = view_query
        , description = "User is allowed to view their own and public queries"
        )
    db.security.addPermissionToRole('User', p)
    p = db.security.addPermission \
        ( name        = 'Edit'
        , klass       = 'query'
        , check       = edit_query
        , description = "User is allowed to edit their queries"
        )
    db.security.addPermissionToRole('User', p)
    p = db.security.addPermission \
        ( name        = 'Create'
        , klass       = 'query'
        , description = "User is allowed to create queries"
        )
    db.security.addPermissionToRole('User', p)

    # and give the regular users access to the web and email interface
    db.security.addPermissionToRole ('User', 'Web Access')
    db.security.addPermissionToRole ('User', 'Email Access')

# end def security
