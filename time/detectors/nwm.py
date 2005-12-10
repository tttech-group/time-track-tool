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
#    nwm
#
# Purpose
#    Detectors for classes needed for network management
#

from roundup.exceptions             import Reject
from roundup.cgi.TranslationService import get_translation
from operator                       import or_

_      = lambda x : x
common = None

def reject_invalid_ip (ip) :
    octets = ip.split ('.')
    if len (octets) != 4 :
        raise Reject, _ ('Invalid IP "%(ip)s": must contain 4 octets') \
            % locals ()
    for o in octets :
        on = None
        try :
            on = int (o)
        except ValueError :
            pass
        if on is None or on < 0 or on > 255 :
            raise Reject, _ ('Invalid IP "%(ip)s": invalid octet "%(o)s"') \
                % locals ()
# end def reject_invalid_ip

def check_ip_olo (db, ip, olo) :
    reject_invalid_ip (ip)
    sn = db.ip_subnet.find (org_location = olo)
    for sn_id in sn :
        subnet = db.ip_subnet.getnode (sn_id)
        if common.ip_in_subnet (ip, subnet.ip, subnet.netmask) :
            return
    olo_name = db.org_location.get (olo, 'name')
    ip_sn    = _ ('ip_subnet')
    raise Reject, _ ("IP %(ip)s does not match any %(ip_sn)s of %(olo_name)s") \
        % locals ()
# end def check_ip_olo

def check_network_address (db, cl, nodeid, new_values) :
    for i in 'ip', 'org_location' :
        if i in new_values and not new_values [i] :
            raise Reject, "%(attr)s may not be undefined" % {'attr' : _ (i)}
    ip  = new_values.get ('ip',           cl.get (nodeid, 'ip'))
    olo = new_values.get ('org_location', cl.get (nodeid, 'org_location'))
    check_ip_olo (db, ip, olo)
# end def check_network_address

def new_network_address (db, cl, nodeid, new_values) :
    for i in 'ip', 'org_location' :
        if i not in new_values :
            raise Reject, "%(attr)s must be specified" % {'attr' : _ (i)}
    check_ip_olo (db, new_values ['ip'], new_values ['org_location'])
# end def new_network_address

def reject_invalid_mac (mac) :
    octets = mac.split (':')
    if len (octets) != 6 :
        raise Reject, _ ('Invalid MAC "%(mac)s": must contain 6 octets') \
            % locals ()
    for o in octets :
        on = None
        try :
            on = int (o, 16)
        except ValueError :
            pass
        if on is None or on < 0 or on > 255 :
            raise Reject, _ ('Invalid MAC "%(mac)s": invalid octet "%(o)s"') \
                % locals ()
# end def reject_invalid_mac

def check_network_interface (db, cl, nodeid, new_values) :
    for i in 'mac', :
        if i in new_values and not new_values [i] :
            raise Reject, "%(attr)s may not be undefined" % {'attr' : _ (i)}
    mac = new_values.get ('mac', cl.get (nodeid, 'mac'))
    reject_invalid_mac (mac)
# end def check_network_interface

def new_network_interface (db, cl, nodeid, new_values) :
    for i in 'mac', :
        if i not in new_values :
            raise Reject, "%(attr)s must be specified" % {'attr' : _ (i)}
    reject_invalid_mac (new_values ['mac'])
# end def new_network_interface

def check_machine_alias (db, mn) :
    olos = {}
    if not mn :
        return
    for id in mn :
        m = db.machine_name.getnode (id)
        if  (  m.dns_record_type == db.dns_record_type.lookup ('CNAME')
            or m.machine_name
            ) :
            raise Reject, _ ("Machine names may not point to other CNAMEs")
        for na_id in m.network_address :
            na = db.network_address.getnode (na_id)
            if na.org_location in olos :
                olon = _ ('org_location')
                polo = db.org_location.get (na.org_location, 'name')
                ip   = na.ip
                raise Reject, _ ("Duplicate %(olon)s %(polo)s in %(ip)s") \
                    % locals ()
            olos [na.org_location] = na.ip
# end def check_machine_alias

def check_nw_adr_location (db, id, adr, mn, drt, new_values) :
    na       = _ ('network_address')
    olo      = _ ('org_location')
    mnn      = _ ('machine_name')
    drtn     = _ ('dns_record_type')
    invalid  = db.dns_record_type.lookup ('invalid')
    a_rec    = db.dns_record_type.lookup ('A')
    cname    = db.dns_record_type.lookup ('CNAME')
    if adr and mn :
        raise Reject, _ ("Only one of %(na)s and %(mnn)s may be given") \
            % locals ()
    locations = {}
    for a in adr :
        l = db.network_address.get (a, 'org_location')
        if l in locations :
            olo_name = db.org_location.get (l, 'name')
            raise Reject, _ ("Duplicate %(olo)s for %(na)s: %(olo_name)s") \
                % locals ()
        locations [l] = True
    check_machine_alias (db, mn)
    if id :
        for alias in db.machine_name.find (machine_name = id) :
            check_machine_alias (db, alias)
    if  (   ('network_address' in new_values or 'machine_name' in new_values)
        and not 'dns_record_type' in new_values
        and drt != invalid
        ) :
        drt =  [a_rec, cname]['machine_name' in new_values]
        new_values ['dns_record_type'] = drt
    if drt != invalid :
        if mn and drt != cname :
            raise Reject, _ ("For %(mnn)s, %(drtn)s must be CNAME") % locals ()
        if adr and drt != a_rec :
            raise Reject, _ ("For %(na)s, %(drtn)s must be CNAME")  % locals ()
# end def check_nw_adr_location

def check_machine_name (db, cl, nodeid, new_values) :
    for i in 'name', :
        if i in new_values and not new_values [i] :
            raise Reject, "%(attr)s may not be undefined" % {'attr' : _ (i)}
    adr = new_values.get ('network_address', cl.get (nodeid, 'network_address'))
    mn  = new_values.get ('machine_name',    cl.get (nodeid, 'machine_name'))
    drt = new_values.get ('dns_record_type', cl.get (nodeid, 'dns_record_type'))
    check_nw_adr_location (db, nodeid, adr, mn, drt, new_values)
# end def check_machine_name

def new_machine_name (db, cl, nodeid, new_values) :
    for i in 'name', :
        if i not in new_values :
            raise Reject, "%(attr)s must be specified" % {'attr' : _ (i)}
    adr = new_values.get ('network_address', [])
    mn  = new_values.get ('machine_name',    None)
    drt = new_values.get ('dns_record_type', None)
    check_nw_adr_location (db, nodeid, adr, mn, drt, new_values)
# end def new_machine_name

def check_netmask (mask) :
    if mask < 0 or mask > 32 or mask - int (mask) :
        raise Reject, _ ("Invalid netmask: %(mask)s") % locals ()
# end def check_netmask

def check_duplicate_ip_subnet (cl, nodeid, ip, mask) :
    for sn_id in cl.getnodeids () :
        if sn_id == nodeid : continue
        n      = _ ('ip_subnet')
        ips    = cl.getnode (sn_id)
        o_ip   = ips.ip
        o_mask = ips.netmask
        if  (common.subnets_overlap (ip, mask, o_ip, o_mask)) :
            raise Reject, \
                ( ("%(n)s %(ip)s %(mask)s overlaps with %(o_ip)s %(o_mask)s")
                % locals ()
                )
# end def check_duplicate_ip_subnet

def check_ip_subnet (db, cl, nodeid, new_values) :
    for i in 'ip', 'netmask', 'org_location' :
        if i in new_values and not new_values [i] :
            raise Reject, "%(attr)s may not be undefined" % {'attr' : _ (i)}
    ip   = new_values.get     ('ip',      cl.get (nodeid, 'ip'))
    mask = new_values.get     ('netmask', cl.get (nodeid, 'netmask'))
    reject_invalid_ip         (ip)
    check_netmask             (mask)
    check_duplicate_ip_subnet (cl, nodeid, ip, mask)
# end def check_ip_subnet

def new_ip_subnet (db, cl, nodeid, new_values) :
    for i in 'ip', 'netmask', 'org_location' :
        if i not in new_values :
            raise Reject, "%(attr)s must be specified" % {'attr' : _ (i)}
    ip   = new_values ['ip']
    mask = new_values ['netmask']
    reject_invalid_ip         (ip)
    check_netmask             (mask)
    check_duplicate_ip_subnet (cl, nodeid, ip, mask)
# end def new_ip_subnet

def check_and_update_gid (_, db, cl, nodeid, sd, gid) :
    is_other  = common.uid_or_gid_in_range (gid, sd.gid_range)
    is_person = common.uid_or_gid_in_range (gid, sd.private_gid_range)
    if not is_other and not is_person and gid != sd.machine_group :
        gname  = _ ('gid')
        sdname = _ ('smb_domain')
        raise Reject, _("Invalid %(gname)s: %(gid)s for %(sdname)s") % locals ()
    common.check_unique (_, cl, nodeid, 'gid', gid)
    if is_other :
        db.smb_domain.set (sd.id, last_gid = max (gid, sd.last_gid))
# end def check_and_update_gid

def check_group (db, cl, nodeid, new_values) :
    for i in 'name', 'gid', 'org_location' :
        if i in new_values and not new_values [i] :
            raise Reject, "%(attr)s may not be undefined" % {'attr' : _ (i)}
    ol = new_values.get ('org_location', cl.get (nodeid, 'org_location'))
    if 'gid' in new_values :
        gid = new_values ['gid']
        sd  = db.smb_domain.getnode (db.org_location.get (ol, 'smb_domain'))
        check_and_update_gid (_, db, cl, nodeid, sd, gid)
# end def check_group

def new_group (db, cl, nodeid, new_values) :
    for i in 'name', 'org_location' :
        if i not in new_values :
            raise Reject, "%(attr)s must be specified" % {'attr' : _ (i)}
    si = db.org_location.get   (new_values ['org_location'], 'smb_domain')
    sd = db.smb_domain.getnode (si)
    if 'gid' not in new_values :
        new_values ['gid'] = common.next_uid_or_gid (sd.last_gid, sd.gid_range)
    check_and_update_gid (_, db, cl, nodeid, sd, new_values ['gid'])
# end def new_group

def check_smb_domain (db, cl, nodeid, new_values) :
    for i in 'name', 'sid' :
        if i in new_values and not new_values [i] :
            raise Reject, "%(attr)s may not be undefined" % {'attr' : _ (i)}
    if 'sid' in new_values :
        common.check_unique (_, cl, nodeid, 'sid', new_values ['sid'])
# end def check_smb_domain

def new_smb_domain (db, cl, nodeid, new_values) :
    for i in 'name', 'sid' :
        if i not in new_values :
            raise Reject, "%(attr)s must be specified" % {'attr' : _ (i)}
    common.check_unique (_, cl, nodeid, 'sid', new_values ['sid'])
# end def new_smb_domain

def check_alias (db, cl, nodeid, new_values) :
    for i in 'name', :
        if i in new_values and not new_values [i] :
            raise Reject, "%(attr)s may not be undefined" % {'attr' : _ (i)}
    name = new_values.get ('name',           cl.get (nodeid, 'name'))
    a2a  = new_values.get ('alias_to_alias', cl.get (nodeid, 'alias_to_alias'))
    a2u  = new_values.get ('alias_to_user',  cl.get (nodeid, 'alias_to_user'))
    if not (a2a or a2u) :
        raise Reject, _ ("Either %s or %s must be defined") \
            % (_ ('alias_to_alias'), _ ('alias_to_user'))
    if 'alias_to_alias' in new_values :
        new_values ['alias_to_alias'] = common.sort_uniq (a2a)
    if 'alias_to_user'  in new_values :
        new_values ['alias_to_user']  = common.sort_uniq (a2u)
    if 'name' in new_values or 'alias_to_alias' in new_values :
        common.check_loop (_, cl, nodeid, 'alias_to_alias', a2a)
# end def check_alias

def new_alias (db, cl, nodeid, new_values) :
    for i in 'name', :
        if i not in new_values :
            raise Reject, "%(attr)s must be specified" % {'attr' : _ (i)}
    if not ('alias_to_alias' in new_values or 'alias_to_user' in new_values) :
        raise Reject, _ ("Either %s or %s must be defined") \
            % ('alias_to_alias', 'alias_to_user')
    if 'alias_to_alias' in new_values :
        a2a = new_values ['alias_to_alias']
        new_values ['alias_to_alias'] = common.sort_uniq (a2a)
        common.check_loop (_, cl, nodeid, 'alias_to_alias', a2a)
    if 'alias_to_user'  in new_values :
        a2u = new_values ['alias_to_user']
        new_values ['alias_to_user']  = common.sort_uniq (a2u)
# end def new_alias

smb_attributes = 'smb_name', 'machine_uid', 'smb_domain'

def reduce_or (* args) :
    return reduce (lambda a, b : a or b, args)
# end def reduce_or

def new_machine (db, cl, nodeid, new_values) :
    sd = None
    if 'smb_domain' in new_values and 'machine_uid' not in new_values :
        sd = db.smb_domain.getnode (new_values ['smb_domain'])
        new_values ['machine_uid'] = common.next_uid_or_gid \
            (sd.last_machine_uid, sd.machine_uid_range)
    if reduce_or (* (a in newvalues for a in smb_attributes)) :
        for i in smb_attributes :
            if i not in new_values :
                raise Reject, _ ("All of %s must be specified") \
                    % ', '.join (_ (i) for i in smb_attributes)
    if sd :
        db.smb_domain.set \
            ( sd.id
            , last_machine_uid = max
                (sd.last_machine_uid, new_values ['machine_uid'])
            )
# end def new_machine

def check_machine (db, cl, nodeid, new_values) :
    smb_attr_values = {}
    for a in smb_attributes :
        smb_attr_values [a] = new_values.get (a, cl.get (nodeid, a))
    if reduce_or (* (smb_attr_values [a] for a in smb_attributes)) :
        for i in smb_attributes :
            if not smb_attr_values [i] :
                raise Reject, _ ("All of %s must be specified") \
                    % ', '.join (_ (i) for i in smb_attributes)
    if 'machine_uid' in new_values :
        sd = db.smb_domain.getnode (new_values ['smb_domain'])
        db.smb_domain.set \
            ( sd.id
            , last_machine_uid = max
                (sd.last_machine_uid, new_values ['machine_uid'])
            )
# end def check_machine

def init (db) :
    import sys, os
    global common, _
    sys.path.insert (0, os.path.join (db.config.HOME, 'lib'))
    import common
    del (sys.path [0])
    _   = get_translation \
        (db.config.TRACKER_LANGUAGE, db.config.TRACKER_HOME).gettext
    db.alias.audit             ("create", new_alias)
    db.alias.audit             ("set",    check_alias)
    db.group.audit             ("create", new_group)
    db.group.audit             ("set",    check_group)
    db.ip_subnet.audit         ("create", new_ip_subnet)
    db.ip_subnet.audit         ("set",    check_ip_subnet)
    db.machine.audit           ("create", new_machine)
    db.machine.audit           ("set",    check_machine)
    db.machine_name.audit      ("create", new_machine_name)
    db.machine_name.audit      ("set",    check_machine_name)
    db.network_address.audit   ("create", new_network_address)
    db.network_address.audit   ("set",    check_network_address)
    db.network_interface.audit ("create", new_network_interface)
    db.network_interface.audit ("set",    check_network_interface)
    db.smb_domain.audit        ("create", new_smb_domain)
    db.smb_domain.audit        ("set",    check_smb_domain)
# end def init

### __END__ time_project
