#! /usr/bin/python
# -*- coding: iso-8859-1 -*-
# Copyright (c) 2007 Ralf Schlatterbeck (rsc@runtux.com)
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
#   The above copyright notice and this permission notice shall be included in
#   all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from cgi    import parse_qs
from urllib import urlencode, unquote_plus

def fix_url_and_template (new_values, url) :
    tmplate = new_values.get ('tmplate')
    deleted = False
    #print "url before:", url
    if url :
        urldict = parse_qs (url)
        #print urldict
        for k in '@:' :
            key = k + 'template'
            if key in urldict :
                tmplate = tmplate or urldict [key][0]
                del urldict [key]
                deleted = True
        if deleted :
            for k, v in urldict.iteritems () :
                urldict [k] = ','.join (v)
            new_values ['url'] = unquote_plus (urlencode (urldict))
            #print "url after:", new_values ['url']
    #print "tmplate:", tmplate or 'index'
    return tmplate or 'index'
# end def fix_url_and_template

def new_query (db, cl, nodeid, new_values) :
    url = new_values.get ('url')
    new_values ['tmplate'] = fix_url_and_template (new_values, url)
# end def new_query

def check_query (db, cl, nodeid, new_values) :
    url     = new_values.get       ('url', cl.get (nodeid, 'url'))
    tmplate = fix_url_and_template (new_values, url)
    if 'tmplate' in new_values and not new_values ['tmplate'] :
        new_values ['tmplate'] = tmplate
# end def check_query

def init (db) :
    db.query.audit ("create", new_query)
    db.query.audit ("set",    check_query)
# end def init
