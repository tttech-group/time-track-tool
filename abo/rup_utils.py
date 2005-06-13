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

import roundup.i18n
def uni (latin1) :
    return latin1.decode ('latin1').encode ('utf8')

gettext = roundup.i18n.get_translation ('de', '/home/ralf/roundup/abo').gettext

prettymap = \
{ 'confirm'           : uni('Bestätigung Passwort')
, 'countrycode'       : uni('Ländercode')
}

def pretty (name) :
    return (prettymap.get (name, gettext (name)))

def abo_max_invoice (db, abo) :
    if not len (abo ['invoices']) :
        return None
    maxinv  = db.invoice.getnode (abo ['invoices'][0])
    maxdate = maxinv ['period_end']
    for i in abo ['invoices'] :
        inv = db.invoice.getnode (i)
        d   = inv ['period_end']
        if maxdate < d :
            maxdate = d
            maxinv  = inv
    return maxinv
# end def abo_max_invoice
