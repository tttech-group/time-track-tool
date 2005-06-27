# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004 Ralf Schlatterbeck. All rights reserved
# Reichergasse 131, A-3411 Weidling
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

from roundup.exceptions             import Reject
from roundup.cgi.TranslationService import get_translation

_ = lambda x : x

def check (db, cl, nodeid, new_values) :
    for i in 'period', 'adr_type' :
        if i in new_values :
            attr = new_values.get (i)
        elif nodeid :
            attr = cl.get (nodeid, i)
        if not attr :
            raise Reject, _ ('"%(attr)s" must be filled in') % {'attr' : _ (i)}
    period = new_values.get   ('period',   cl.get (nodeid, 'period'))
    if int (period) != period :
        raise Reject, _ ('period must be an integer')
    adr_type = new_values.get ('adr_type', cl.get (nodeid, 'adr_type'))
    cat = db.adr_type.get  (adr_type, 'typecat')
    if db.adr_type_cat.get (cat, 'code') != 'ABO' :
        raise Reject, _ \
            ('Selected address types must be in type category "ABO"')
# end def check

def init (db) :
    global _
    _   = get_translation \
        (db.config.TRACKER_LANGUAGE, db.config.TRACKER_HOME).gettext
    db.abo_type.audit ("create", check)
    db.abo_type.audit ("set",    check)
# end def init
