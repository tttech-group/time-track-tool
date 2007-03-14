#!/usr/bin/python2.4
# -*- coding: iso-8859-1 -*-
import sys
from roundup           import date
from roundup           import instance
from roundup.password  import Password, encodePassword
tracker = instance.open ('/home/ralf/roundup/ttt')
#tracker = instance.open ('/roundup/tracker/ttt')
db      = tracker.open ('admin')

id = sys.argv [1]
journal = db.getjournal ('issue', id)
for line in journal :
    nodid, date, tag, action, params = line
    if 'nosy' in params :
        params ['nosy'] = [k for k in params ['nosy'] if k]
db.setjournal ('issue', id, journal)
db.commit ()
