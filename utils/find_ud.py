#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import sys
import os
from roundup           import date
from roundup           import instance
from roundup.password  import Password, encodePassword
dir     = os.getcwd ()
tracker = instance.open (dir)
db      = tracker.open ('admin')

for ud in db.user_dynamic.getnodeids () :
    dyn = db.user_dynamic.getnode (ud)
    if dyn.all_in and dyn.overtime_period :
        u = db.user.get (dyn.user, 'username')
        d1 = dyn.valid_from.pretty ('%Y-%m-%d')
        d2 = ''
        if dyn.valid_to :
            d2 = dyn.valid_to.pretty ('%Y-%m-%d')
        print "user_dynamic%s: %s %s-%10s all_in and Overtime Period set" \
            % (ud, u, d1, d2)
