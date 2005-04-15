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
# $Id$

from roundup.rup_utils import uni

#
# INITIAL VALUES
#

# create the two default users
user = db.getclass('user')
user.create \
    ( username="admin"
    , password=adminpw
    , address=db.config.ADMIN_EMAIL
    , roles='Admin'
    )
user.create (username="anonymous", roles='Anonymous')

currency = db.getclass ('currency')
currency.create (name = 'CHF', description = 'Schweizer Franken')
currency.create (name = 'EUR', description = 'Euro')
currency.create (name = 'GBP', description = 'Britische Pfund')
currency.create (name = 'USD', description = 'US-Dollar')

valid = db.getclass ('valid')
valid.create \
    ( name = uni ('g�ltig')
    , description = uni ('G�ltige Adresse')
    )
valid.create \
    ( name = uni ('verstorben')
    , description = uni ('Verstorbener Adressat')
    )
