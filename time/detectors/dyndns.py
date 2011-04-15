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
# Dual License:
# If you need a proprietary license that permits you to add your own
# software without the need to publish your source-code under the GNU
# General Public License above, contact
# Reder, Christian Reder, A-2560 Berndorf, Austria, christian@reder.eu

import os
from tempfile                       import mkstemp
from socket                         import socket, SOCK_SEQPACKET, AF_UNIX
from roundup.exceptions             import Reject
from roundup.cgi.TranslationService import get_translation
from common                         import require_attributes

_ = lambda x : x

def dyndns_update (db, cl, nodeid, old_values) :
    # Only generate config if at least one host is configured
    hosts = db.dyndns_host.getnodeids ()
    if not hosts :
        return
    fd, fn = mkstemp ('conf', 'ddclient', '/var/run/roundup/')
    f = os.fdopen (fd, "wb")
    print "created"
    print >> f, "# Configuration file for ddclient generated by roundup"
    print >> f, "#"
    print >> f, "# /etc/ddclient.conf"
    print >> f, ""
    print >> f, "pid=/var/run/ddclient.pid"

    dyn = db.dyndns.getnode (db.dyndns.getnodeids () [0])
    if dyn.syslog :
        print >> f, "syslog=yes"
    print >> f, ""
    if dyn.interface :
        print >> f, "use=if, if=%s" % dyn.interface
        if dyn.interface_skip :
            print >> f, "if-skip=%s" % dyn.interface
    elif dyn.web_url :
        print >> f, "use=web, web=%s" % dyn.web_url
        if dyn.web_skip :
            print >> f, "web-skip=%s" % dyn.web_skip
    elif dyn.fw_url :
        print >> f, "use=fw, fw=%s" % dyn.fw_url
        if dyn.fw_skip :
            print >> f, "fw-skip=%s" % dyn.fw_skip
        if dyn.fw_login :
            print >> f, "fw-login=%s" % dyn.fw_login
        if dyn.fw_password :
            print >> f, "fw-password=%s" % dyn.fw_password
    else :
        print >> f, "# Default config"
        print >> f, "use=web, web=dyndns"
    print >> f, ""

    for sid in db.dyndns_service.filter (None, dict (dyndns = dyn.id)) :
        service = db.dyndns_service.getnode (sid)
        proto = db.dyndns_protocol.get (service.protocol, 'name')
        print >> f, "protocol=%s" % proto
        for k in 'server', 'login', 'password' :
            print >> f, "%s=%s" % (k, service [k])
        for h in db.dyndns_host.filter (None, dict (dyndns_service = sid)) :
            host = db.dyndns_host.getnode (h)
            if host.description :
                print >> f, "#", host.description
            print >> f, host.hostname
        print >> f, ""
    f.close ()
    # Notify a daemon to move the file in place
    s = socket (AF_UNIX, SOCK_SEQPACKET)
    s.connect (db.config.detectors.UPDATE_SOCKET)
    s.send ('dyndns %s' % fn)
    s.close ()
# end def dyndns_update

def dyndns_service (db, cl, nodeid, new_values) :
    require_attributes \
        (_, cl, nodeid, new_values, 'protocol', 'login', 'password')
    a = 'server'
    if  (  not nodeid and a not in new_values
        or nodeid and new_values.get (a, cl.get (nodeid, a)) is None
        ) :
        prid  = new_values.get ('protocol')
        if not prid :
            prid = cl.get (nodeid, 'protocol')
        server = db.dyndns_protocol.get (prid, 'default_server')
        new_values [a] = server
# end def dyndns_service

def dyndns_host (db, cl, nodeid, new_values) :
    require_attributes \
        (_, cl, nodeid, new_values, 'dyndns_service')
# end def dyndns_host

def init (db) :
    global _
    _   = get_translation \
        (db.config.TRACKER_LANGUAGE, db.config.TRACKER_HOME).gettext
    if 'dyndns_host' in db.classes :
        db.dyndns.react         ("create", dyndns_update)
        db.dyndns.react         ("set",    dyndns_update)
        db.dyndns_service.react ("create", dyndns_update)
        db.dyndns_service.react ("set",    dyndns_update)
        db.dyndns_host.react    ("create", dyndns_update)
        db.dyndns_host.react    ("set",    dyndns_update)
        db.dyndns_host.audit    ("create", dyndns_host)
        db.dyndns_host.audit    ("set",    dyndns_host)
        db.dyndns_service.audit ("create", dyndns_service)
        db.dyndns_service.audit ("set",    dyndns_service)
# end def init
