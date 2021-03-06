#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import os
import sys
from roundup           import date
from roundup           import instance
from roundup.password  import Password, encodePassword
tracker = instance.open (os.getcwd ())
db      = tracker.open ('admin')

# sometimes there are "None" values in the nosy history. Fix these.
# takes the id of the issue to fix

id = sys.argv [1]
journal = db.getjournal ('issue', id)
for line in journal :
    nodid, date, tag, action, params = line
    if 'nosy' in params :
        params ['nosy'] = [k for k in params ['nosy'] if k]
db.setjournal ('issue', id, journal)
db.commit ()
