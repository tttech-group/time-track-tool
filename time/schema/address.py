#! /usr/bin/python
# -*- coding: iso-8859-1 -*-
# Copyright (C) 2006 Dr. Ralf Schlatterbeck Open Source Consulting.
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
#++
# Name
#    address
#
# Purpose
#    Schema definitions for address and other contact information

from roundup.hyperdb import Class
import schemadef

def init \
    ( db
    , Class
    , Ext_Class
    , Min_Issue_Class
    , String
    , Date
    , Link
    , Multilink
    , Boolean
    , Number
    , ** kw
    ) :

    do_index = "yes"
    export   = {}

    class Address_Class (Min_Issue_Class) :
        """ Create address class with default attributes, may be
            extended by other definitions.
        """
        def __init__ (self, db, classname, ** properties) :
            self.update_properties \
                ( title               = String    (indexme = "no")
                , lettertitle         = String    (indexme = "no")
                , firstname           = String    (indexme = do_index)
                , initial             = String    (indexme = "no")
                , lastname            = String    (indexme = do_index)
                , function            = String    (indexme = do_index)
                , street              = String    (indexme = do_index)
                , country             = String    (indexme = "no")
                , postalcode          = String    (indexme = "no")
                , city                = String    (indexme = do_index)
                , salutation          = String    (indexme = "no")
                , adr_type            = Multilink ("adr_type")
                , valid               = Link      ("valid")
                , letters             = Multilink ("letter")
                , lookalike_lastname  = String    (indexme = do_index)
                , lookalike_firstname = String    (indexme = do_index)
                , lookalike_city      = String    (indexme = do_index)
                , lookalike_street    = String    (indexme = do_index)
                , lookalike_function  = String    (indexme = do_index)
                , contacts            = Multilink ("contact")
                )
            self.__super.__init__ (db, classname, ** properties)
            self.setlabelprop ('lastname')
        # end def __init__
    # end class Address_Class
    export.update (dict (Address_Class = Address_Class))

    adr_type = Class \
        ( db, ''"adr_type"
        , code                = String    ()
        , description         = String    ()
        , typecat             = Link      ("adr_type_cat")
        )
    adr_type.setkey ("code")

    adr_type_cat = Class \
        ( db, ''"adr_type_cat"
        , code                = String    ()
        , description         = String    ()
        , type_valid          = Boolean   ()
        )
    adr_type_cat.setkey (''"code")

    class Letter_Class (Min_Issue_Class) :
        """ Create letter class with default attributes, may be
            extended by other definitions.
            The file types are either PDF (from old imported data) or an
            OpenOffice.org document which is cusomized using info
            pointed to with invoice and/or address.
        """
        def __init__ (self, db, classname, ** properties) :
            self.update_properties \
                ( subject             = String    ()
                , address             = Link      ("address")
                , date                = Date      ()
                )
            self.__super.__init__ (db, classname, ** properties)
            self.setlabelprop ('subject')
        # end def __init__
    # end class Letter_Class
    export.update (dict (Letter_Class = Letter_Class))

    tmplate_status = Class \
        ( db, ''"tmplate_status"
        , name                = String    ()
        , order               = Number    ()
        , description         = String    ()
        , use_for_invoice     = Boolean   ()
        , use_for_letter      = Boolean   ()
        )
    tmplate_status.setkey (''"name")

    tmplate = Class \
        ( db, ''"tmplate"
        , name                = String    ()
        # version control, use latest:
        , files               = Multilink ("file", do_journal='no')
        , tmplate_status      = Link      ("tmplate_status")
        )
    tmplate.setkey (''"name")

    # Define codes for (in)valid addresses, e.g., "verstorben"
    valid = Class \
        ( db, ''"valid"
        , name                = String    ()
        , description         = String    ()
        )
    valid.setkey (''"name")

    class Contact_Class (Ext_Class) :
        """ Create contact class with default attributes, may be
            extended by other definitions.
        """
        def __init__ (self, db, classname, ** properties) :
            self.update_properties \
                ( contact             = String    ()
                , description         = String    ()
                , contact_type        = Link      ("contact_type")
                )
            self.__super.__init__ (db, classname, ** properties)
            self.setlabelprop ('contact')
        # end def __init__
    # end class Contact_Class
    export.update (dict (Contact_Class = Contact_Class))

    class Contact_Type_Class (Ext_Class) :
        """ Create contact_type class with default attributes, may be
            extended by other definitions.
        """
        def __init__ (self, db, classname, ** properties) :
            self.update_properties \
                ( name                = String    ()
                , description         = String    ()
                , url_template        = String    ()
                , order               = Number    ()
                )
            self.__super.__init__ (db, classname, ** properties)
            self.setkey (''"name")
        # end def __init__
    # end class Contact_Type_Class
    export.update (dict (Contact_Type_Class = Contact_Type_Class))

    contact_type = Contact_Type_Class (db, ''"contact_type")

    contact = Contact_Class \
        ( db, ''"contact"
        , address             = Link      ("address")
        )

    return export
# end def init

def security (db, ** kw) :
    roles = \
        [ ("Type"          , "Allowed to add/change type codes")
        , ("Letter"        , "Allowed to add/change templates and letters")
        , ("Contact"       , "Allowed to add/change address data")
        ]

    classes = \
        [ ("adr_type"          , ["User"],    ["Type"])
        , ("adr_type_cat"      , ["User"],    ["Type"])
        , ("tmplate"           , ["User"],    ["Letter"])
        , ("valid"             , ["User"],    [])
        , ("contact_type"      , ["User"],    [])
        , ("contact"           , ["User"],    ["Contact"])
        , ("tmplate_status"    , ["User"],    [])
        ]

    schemadef.register_roles             (db, roles)
    schemadef.register_class_permissions (db, classes, [])
# end def security
