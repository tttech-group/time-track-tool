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
#    defaults
#
# Purpose
#    Auditors for 'default values'
#
# Revision Dates
#    22-Jul-2004 (MPH) Creation
#    5-Oct-2004 (MPH) Added implementation_task.create and
#                     documentation_task.create and testcase.create
#    ««revision-date»»···
#--
#
from roundup import roundupdb, hyperdb
from roundup.exceptions import Reject

def union (* lists) :
    """Compute the union of lists.
    """
    tab = {}
    for l in lists :
        map (lambda x, tab = tab : tab.update  ({x : 1}), l)
    return tab.keys ()
# end def union

def default_responsible (db, cl, nodeid, new_values) :
    if not new_values.has_key ("responsible") :
        new_values ["responsible"] = db.getuid()
# end def set_defaults

def default_defect_status (db, cl, nodeid, new_values) :
    if not new_values.has_key ("status") \
        or new_values ["status"] != "assigned" :
        new_values ["status"] = "assigned"
# end def default_defect_status

def default_defect_responsible (db, cl, nodeid, new_values) :
    """set responsible to product.responsible
    """
    if not new_values.has_key ("responsible") :
        prod_resp = db.product.get (new_values ["product"], "responsible")
        new_values ["responsible"] = prod_resp
# end def default_defect_responsible

def default_defect_nosy (db, cl, nodeid, new_values) :
    """auditor on defect

    sets the nosy list to contain creator, responsible and the product's nosy
    users.
    """
    nosy      = new_values.get ("nosy"   , []    )
    product   = new_values.get ("product"        )
    prod_nosy = db.product.get (product  , "nosy")
    creator   = new_values.get ("creator"        )
    print "blaa"
    print nosy, prod_nosy, creator, new_values ["responsible"]
    nosy      = union ( nosy
                      , prod_nosy
                      , [ creator
                        , new_values ["responsible"]
                        ]
                      )
    print nosy
    # XXX: why is the next neccesary ???
    if None in nosy :
        nosy.remove (None)
    new_values ["nosy"] = nosy
# end def default_defect_nosy

def init (db) :
    db.document.audit            ("create", default_responsible)
    db.release.audit             ("create", default_responsible)
    db.action_item.audit         ("create", default_responsible)
    db.feature.audit             ("create", default_responsible)
    db.task.audit                ("create", default_responsible)
    db.defect.audit              ("create", default_defect_responsible)
    db.defect.audit              ("create", default_defect_status)
    db.defect.audit              ("create", default_defect_nosy)
# end def init

### __END__ defaults


