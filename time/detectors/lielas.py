# -*- coding: iso-8859-1 -*-
# Copyright (C) 2010 Ralf Schlatterbeck. All rights reserved
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
from common                         import reject_attributes

_ = lambda x : x


def deny_adr (db, cl, nodeid, new_values) :
    reject_attributes (_, new_values, 'adr')
# end def deny_adr

def update_device_surrogate (db, cl, nodeid, new_values) :
    if 'name' in new_values :
        n = cl.getnode (nodeid)
        new_values ['surrogate'] = '-'.join ((new_values ['name'], n.adr))
# end def update_device_surrogate

def update_sensor_surrogate (db, cl, nodeid, new_values) :
    if 'name' in new_values :
        n = cl.getnode (nodeid)
        d = db.device.get (n.device, 'adr')
        new_values ['surrogate'] = '-'.join ((new_values ['name'], d, n.adr))
# end def update_sensor_surrogate

def init (db) :
    if 'measurement' not in db.classes :
        return
    global _
    _   = get_translation \
        (db.config.TRACKER_LANGUAGE, db.config.TRACKER_HOME).gettext
    db.device.audit ("set", deny_adr)
    db.device.audit ("set", update_device_surrogate)
    db.sensor.audit ("set", deny_adr)
    db.sensor.audit ("set", update_sensor_surrogate)
# end def init
