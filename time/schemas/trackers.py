#! /usr/bin/python
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
#    schema-kvats
#
# Purpose
#    Specify the DB-Schema for an extended tracker
#    Link this file to schema.py
#--
#

import sys, os

sys.path.insert (0, os.path.join (db.config.HOME, 'lib'))
sys.path.insert (0, os.path.join (db.config.HOME, 'schema'))
from common import clearance_by
import schemadef

# sub-schema definitins to include
# Note: order matters, core is always last.
schemas = \
    ( 'issue'
    , 'it_tracker'
    , 'core'
    )

importer = schemadef.Importer (globals (), schemas)
del sys.path [0:1]

#
# SECURITY SETTINGS
#
# See the configuration and customisation document for information
# about security setup.
# Assign the access and edit Permissions for issue, file and message
# to regular users now

importer.update_security ()
p = db.security.addPermission \
    ( name        = 'Edit'
    , klass       = 'user'
    , check       = schemadef.own_user_record
    , description = \
        "User is allowed to edit (some of) their own user details"
    , properties  = \
        ('password', 'address', 'alternate_addresses', 'timezone', 'phone')
    )
db.security.addPermissionToRole('User', p)

perms = [ ( "user", "View", ["User"]
          , ( "username"
            , "realname"
            , "creation"
            , "creator"
            , "activity"
            , "actor"
            )
          )
        ]
schemadef.register_class_permissions (db, [], perms)

# oh, g'wan, let anonymous access the web interface too
# NOT really !!!
db.security.addPermissionToRole('Anonymous', 'Web Access')
#SHA: f6118fb5aa97dc121092fc0ebd4f379a6d3eacb1