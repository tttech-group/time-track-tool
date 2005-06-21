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
from roundup.date                   import Date, Interval
from roundup.cgi.TranslationService import get_translation

_ = lambda x : x

def new_letter (db, cl, nodeid, new_values) :
    for i in ('address', ) :
        if not i in new_values :
            raise Reject, _ ('"%(attr)s" must be filled in') % {'attr' : _ (i)}
    if 'date' not in new_values :
        new_values ['date'] = Date ('.')
# end def new_letter

def check_letter (db, cl, nodeid, new_values) :
    for i in ('address', 'invoice') :
        if i in new_values :
            raise Reject, _ ('"%(attr)s" may not be changed') % {'attr' : _ (i)}
    for i in ('subject', 'date') :
        x = new_values.get (i, cl.get (nodeid, i))
        if x is None :
            raise Reject, _ ('"%(attr)s" may not be deleted') % {'attr' : _ (i)}
# end def check_letter

def init (db) :
    global _
    _   = get_translation \
        (db.config.TRACKER_LANGUAGE, db.config.TRACKER_HOME).gettext
    db.letter.audit ("create", new_letter)
    db.letter.audit ("set",    check_letter)
# end def init
