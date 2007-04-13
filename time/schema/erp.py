#! /usr/bin/python
# -*- coding: iso-8859-1 -*-
# Copyright (C) 2007 Dr. Ralf Schlatterbeck Open Source Consulting.
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
#    erp
#
# Purpose
#    Schema definitions for ERP

from roundup.hyperdb import Class
import schemadef

def init \
    ( db
    , Class
    , Ext_Class
    , String
    , Date
    , Link
    , Multilink
    , Boolean
    , Number
    , Msg_Class
    , Address_Class
    , Letter_Class
    , ** kw
    ) :

    do_index = "no"
    export   = {}

    bank_account = Class \
        ( db, ''"bank_account"
        , bank                  = String    ()
        , account_number        = String    ()
        , bank_code             = String    ()
        , iban                  = String    ()
        , bic                   = String    ()
        , customer              = Link      ("customer")
        )

    customer = Msg_Class \
        ( db, ''"customer"
        , name                  = String    ()
        , description           = String    ()
        , shipping_address      = Link      ("address")
        , invoice_address       = Link      ("address")
        , contact_person        = Multilink ("contact_person")
        , tax_id                = String    ()
        , status                = Link      ("customer_status")
        , customer_group        = Link      ("customer_group")
        , attendant             = Link      ("user")
        , credit_limit          = Number    ()
        , credit_limit_cur      = Link      ("currency")
        , invoice_dispatch      = Link      ("invoice_dispatch")
        , pharma_ref            = Link      ("pharma_ref")
        , group_discounts       = Multilink ("group_discount")
        , overall_discount      = Multilink ("overall_discount")
        , invoice_text          = String    ()
        , bank_account          = Link      ("bank_account")
        , sales_conditions      = Link      ("sales_conditions")
        )
    customer.setkey (''"name")

    customer_group = Class \
        ( db, ''"customer_group"
        , name                  = String    ()
        , description           = String    ()
        )
    customer_group.setkey ("name")

    customer_status = Class \
        ( db, ''"customer_status"
        , name                  = String    ()
        , description           = String    ()
        , order                 = Number    ()
        )
    customer_status.setkey ("name")

    dispatch_type = Class \
        ( db, ''"dispatch_type"
        , name                  = String    ()
        , description           = String    ()
        )
    dispatch_type.setkey ("name")

    group_discount = Class \
        ( db, ''"group_discount"
        , name                  = String    ()
        , product_group         = Link      ("product_group")
        , discount              = Number    ()
        )
    group_discount.setkey ("name")

    invoice_dispatch = Class \
        ( db, ''"invoice_dispatch"
        , name                  = String    ()
        , description           = String    ()
        )
    invoice_dispatch.setkey ("name")

    overall_discount = Class \
        ( db, ''"overall_discount"
        , name                  = String    ()
        , price                 = Number    ()
        , discount              = Number    ()
        )
    overall_discount.setkey ("name")

    # Pharmareferenzbezirk
    pharma_ref = Class \
        ( db, ''"pharma_ref"
        , name                  = String    ()
        , description           = String    ()
        )
    pharma_ref.setkey ("name")

    product_group = Class \
        ( db, ''"product_group"
        , name                  = String    ()
        , description           = String    ()
        )
    product_group.setkey ("name")

    sales_conditions = Class \
        ( db, ''"sales_conditions"
        , name                  = String    ()
        , description           = String    ()
        , dispatch_type         = Link      ("dispatch_type")
        , discount_percent      = Number    ()
        , discount_days         = Number    ()
        , payment_days          = Number    ()
        )
    sales_conditions.setkey ("name")

    Address_Class \
        ( db, ''"address"
        )

    Letter_Class \
        ( db, ''"letter"
        )

    return export
# end def init


def security (db, ** kw) :
    roles = \
        [ ("Contact"       , "Allowed to add/change customer contact data")
        , ("Discount"      , "Allowed to add/change discounts")
        , ("Letter"        , "Allowed to add/change templates and letters")
        , ("Product"       , "Allowed to add/change product data")
        ]

    classes = \
        [ ("address"           , ["User"],    ["Contact"])
        , ("bank_account"      , ["User"],    ["Contact"])
        , ("customer"          , ["User"],    ["Contact"])
        , ("customer_group"    , ["User"],    ["Admin"])
        , ("customer_status"   , ["User"],    ["Admin"])
        , ("dispatch_type"     , ["User"],    ["Admin"])
        , ("group_discount"    , ["User"],    ["Discount"])
        , ("invoice_dispatch"  , ["User"],    ["Admin"])
        , ("letter"            , ["User"],    ["Letter"])
        , ("pharma_ref"        , ["User"],    ["Admin"])
        , ("product_group"     , ["User"],    ["Product"])
        , ("sales_conditions"  , ["User"],    ["Admin"])
        ]

    schemadef.register_roles             (db, roles)
    schemadef.register_class_permissions (db, classes, [])
# end def security
