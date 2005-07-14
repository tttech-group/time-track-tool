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
#    daily_record_action
#
# Purpose
#    Create daily records for given week, redirect to edit form.
#--

from roundup.cgi.actions    import Action
from roundup.cgi.exceptions import Redirect
from roundup.exceptions     import Reject
from roundup.cgi            import templating
from roundup.date           import Date, Interval, Range
from roundup                import hyperdb
from time                   import gmtime

class daily_record_action (Action) :
    name = 'daily_record'
    permissionType = 'View'

    def handle (self) :
        ''' Export the specified search query as CSV. '''
        # figure the request
        request    = templating.HTMLRequest (self.client)
        filterspec = request.filterspec
        columns    = request.columns
        assert (request.classname == 'daily_record')
        if 'date' in filterspec :
            r = Range (filterspec ['date'], Date)
            if r.to_value is None :
                start = end = r.from_value
            elif r.from_value is None or r.from_value == r.to_value :
                start = end = r.to_value
            else :
                start = r.from_value
                end   = r.to_value
        else :
            date       = Date ('.')
            date       = Date (str (date.local (self.db.getUserTimezone ())))
            wday       = gmtime (date.timestamp ())[6]
            start      = date + Interval ("%sd" % -wday)
            end        = date + Interval ("%sd" % (6 - wday))
        start.hours = start.minutes = start.seconds = 0
        end.hours   = end.minutes   = end.seconds   = 0
        max = start + Interval ('31d')
        if end > max :
            raise ValueError, "Interval may not exceed one month: %s;%s" % \
                tuple ([i.pretty ('%Y-%m-%d') for i in (start, end)])
        d = start
        while d <= end :
            try :
                print "try-create: %s" % d.pretty ('%Y-%m-%d')
                x = self.db.daily_record.create \
                    ( user = self.db.getuid ()
                    , date = d
                    )
                self.db.commit ()
            except Reject :
                pass
            d = d + Interval ('1d')

        print columns
        print filterspec

        d = '%Y-%m-%d'
        request.filterspec = \
            { 'date' : '%s;%s' % (start.pretty (d), end.pretty (d))
            , 'user' : self.db.getuid ()
            }
        url = request.indexargs_url \
            ( ''
            , { ':action'   : 'search'
              , ':template' : 'edit'
              , ':sort'     : 'date'
              , ':group'    : ''
              }
            )
        raise Redirect, url
    # end def handle

def init (instance) :
    instance.registerAction ('daily_record_action', daily_record_action)
# end def init
