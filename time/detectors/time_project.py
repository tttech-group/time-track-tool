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
#    time_project
#
# Purpose
#    Detectors for 'time_project'
#

from roundup.exceptions             import Reject
from roundup.cgi.TranslationService import get_translation

_ = lambda x : x

def check_time_project (db, cl, nodeid, new_values) :
    for i in 'wp_no', 'project' :
        if i in new_values and cl.get (nodeid, i) :
            raise Reject, "%(attr)s may not be changed" % {'attr' : _ (i)}
# end def check_time_project

def new_time_project (db, cl, nodeid, new_values) :
    for i in \
        ( 'responsible', 'deputy',        'organisation'
        , 'department',  'planned_effort'
        ) :
        if i not in new_values :
            raise Reject, "%(attr)s must be specified" % {'attr' : _ (i)}
# end def new_time_project

def init (db) :
    global _
    _   = get_translation \
        (db.config.TRACKER_LANGUAGE, db.config.TRACKER_HOME).gettext
    db.time_project.audit  ("create", new_time_project)
    db.time_project.audit  ("set",    check_time_project)
# end def init

### __END__ time_project
