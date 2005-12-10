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
#    Roundup_Access classes
#
# Purpose
#    Classes encapsulating roundup objects. With access functions and
#    export to LDIF. All classes live in a Roundup_Access object.
#

import os
import sys
import ldif
import textwrap

from cStringIO        import StringIO
from roundup.date     import Date
from roundup          import instance
from roundup.hyperdb  import Link, Multilink

class Roundup_Access (object) :
    """ Wrapper class that gets a handle to the roundup instance and
        includes code and classes from there.
    """

    def __init__ (self, path, basedn, user = 'admin') :
        global ymd, get_user_dynamic, common
        self.tracker = instance.open (path)
        self.db      = self.tracker.open (user)
        self.basedn  = basedn
        sys.path.insert (1, os.path.join (path, 'lib'))
        from user_dynamic import get_user_dynamic
        import common
        ymd = common.ymd
        self.common  = common
        del sys.path [1]
        for rupname in self.db.getclasses () :
            classname = self._classname (rupname)
            if not hasattr (self, classname) :
                # create a derived class dynamically
                setattr (self, classname, type (classname, (self.Roundup,), {}))
            cls = getattr (self, classname)
            setattr (cls, 'db',     self.db)
            setattr (cls, 'cl',     self.db.getclass (rupname))
            setattr (cls, 'basedn', self.basedn)
            setattr (cls, 'master', self)
    # end def __init__

    def _classname (self, rupname) :
        return rupname [0].upper () + rupname [1:]
    # end def _classname

    def class_from_rupname (self, rupname) :
        return getattr (self, self._classname (rupname))
    # end def class_from_rupname

    class Roundup (object) :
        """
            Base class to encapsulate a roundup Class. With access functions
            for roundup and ldif export.
        """

        def __init__ (self, id) :
            self.node   = self.cl.getnode (id)
            self.id     = id
        # end def __init__

        def __getattr__ (self, name) :
            try :
                value = self.node [name]
            except KeyError, cause :
                raise AttributeError, "%s%s: %s" \
                    % (self.node.cl.classname, self.id, cause)
            if value is None : return value
            prop = self.node.cl.properties [name]
            if prop.__class__ == Link :
                value = self.master.class_from_rupname (prop.classname) (value)
                setattr (self, name, value)
            elif prop.__class__ == Multilink :
                newval = []
                cls    = self.master.class_from_rupname (prop.classname)
                for v in value :
                    newval.append (cls (v))
                value = newval
            return value
        # end def __getattr__

        def as_ldif (self) :
            strio  = StringIO ()
            entry  = { 'objectClass' : self.object_class }
            writer = ldif.LDIFWriter (strio)
            for ldn, name in self.ldif_map :
                try :
                    attr = getattr (self, name)
                except AttributeError, cause :
                    attr = None
                if isinstance (attr, Date) :
                    attr = attr.timestamp ()
                if isinstance (attr, float) :
                    attr = long (attr)
                if isinstance (attr, list) :
                    entry [ldn] = attr
                elif attr is not None :
                    entry [ldn] = [str (attr)]
            writer.unparse (self.dn (), entry)
            return strio.getvalue ()
        # end def as_ldif

        zero       = 0
        endofepoch = 0x7FFFFFFF

        def dn (self) :
            op     = self.org_location.orgpath
            org_dn = ["ou=%s" % p for p in op [:-1]]
            org_dn.append ("o=%s" % op [-1])
            label  = getattr (self, self.cl.labelprop ())
            ou     = ''
            if self.ou :
                ou = ",ou=%s" % self.ou
            return "%s=%s%s,%s,%s" \
                % (self.dnname, label, ou, ','.join (org_dn), self.basedn)
        # end def dn

    # end class Roundup

    class Alias (Roundup) :
        """
            Encapsulate the roundup alias class. Includes LDIF export.
            cn=root,ou=MailGroups,ou=vie,ou=at,ou=company,o=org,BASEDN
        """

        ldif_map = \
            [ ('cn',                   'name')
            , ('mailLocalAddress',     'name')
            , ('description',          'description')
            #, ('mailHost',             'tttech.com')
            #, ('mailRoutingAddress',   'name@domino01.vie.at.tttech.ttt')
            ]

        object_class = \
            [ 'organizationalRole'
            , 'inetLocalMailRecipient'
            ]
        ou     = 'MailGroups'
        dnname = 'cn'

    # end class Alias

    class Group (Roundup) :
        """
            Encapsulate the roundup group class. Includes LDIF export.
            cn=..,ou=Groups,ou=vie,ou=at,ou=company,o=org,BASEDN
        """

        ldif_map = \
            [ ('cn',                   'name')
            , ('description',          'description')
            , ('displayName',          'name')
            , ('gidNumber',            'gid')
            , ('memberUid',            'members')
            , ('sambaGroupType',       'samba_group_type')
            , ('sambaSID',             'sid')
            ]

        object_class = \
            [ 'posixGroup'
            , 'sambaGroupMapping'
            ]

        ou     = 'Groups'
        dnname = 'cn'

        def _sid (self) :
            return ''.join \
                (( self.org_location.smb_domain.sid
                 , '-'
                 , str (int (self.gid * 2 + 1001))
                ))
        # end def _sid
        sid = property (_sid)

        samba_group_type = 2

        def _members (self) :
            users = dict \
                ([(i, 1) for i in self.db.user.find (group = self.id)])
            aux = self.db.user.find (secondary_groups = self.id)
            if aux :
                users.update ([(i, 1) for i in aux])
            return [self.db.user.get (u, 'username') for u in users.iterkeys ()]
        # end def _members
        members = property (_members)

    # end class Group

    class Smb_domain (Roundup) :
        """
            Encapsulate the roundup smb_domain class. Includes LDIF export.
            sambaDomainName=..,ou=vie,ou=at,ou=company,o=org,BASEDN
        """
        ldif_map = \
            [ ('sambaDomainName',         'name')
            , ('sambaSID',                'sid')
            , ('sambaAlgorithmicRidBase', 'rid_base')
            ]

        object_class = ['sambaDomain']
        rid_base     = 1000
        ou           = None
        dnname       = 'sambaDomainName'

    # end class Smb_domain

    class User (Roundup) :
        """
            Encapsulate the roundup user class. Includes LDIF export.
            uid=..,ou=Users,ou=vie,ou=at,ou=company,o=org,BASEDN
        """

        ldif_map = \
            [ ('cn',                   'username')
            , ('sn',                   'realname')
            , ('telephoneNumber',      'phone')
            , ('description',          'realname')
            , ('displayName',          'realname')
            , ('initials',             'nickname')
            , ('mail',                 'address')
            , ('uid',                  'username')
            , ('uidNumber',            'uid')
            , ('gidNumber',            'gid')
            , ('homeDirectory',        'home_directory')
            , ('loginShell',           'login_shell')
            , ('gecos',                'gecos')
            , ('mailLocalAddress',     'mail_addresses')
            , ('sambaAcctFlags',       'samba_acct_flags')
            , ('sambaHomeDrive',       'samba_home_drive')
            , ('sambaHomePath',        'samba_home_path')
            , ('sambaKickoffTime',     'samba_kickoff_time')
            , ('sambaLMPassword',      'samba_lm_password')
            , ('sambaLogoffTime',      'endofepoch')
            , ('sambaLogonScript',     'samba_logon_script')
            , ('sambaLogonTime',       'zero')
            , ('sambaNTPassword',      'samba_nt_password')
            , ('sambaPrimaryGroupSID', 'group_sid')
            , ('sambaProfilePath',     'samba_profile_path')
            , ('sambaPwdCanChange',    'samba_pwd_can_change')
            , ('sambaPwdLastSet',      'samba_pwd_last_set')
            , ('sambaPwdMustChange',   'samba_pwd_must_change')
            , ('sambaSID',             'sid')
            , ('shadowExpire',         'shadow_expire')
            , ('shadowFlag',           'shadow_used')
            , ('shadowInactive',       'shadow_inactive')
            , ('shadowLastChange',     'shadow_last_change')
            , ('shadowMax',            'shadow_max')
            , ('shadowMin',            'shadow_min')
            , ('shadowWarning',        'shadow_warning')
            ]

        samba_acct_flags = '[U]'

        object_class = \
            [ 'top'
            , 'inetOrgPerson'
            , 'posixAccount'
            , 'inetLocalMailRecipient'
            , 'sambaSamAccount'
            , 'shadowAccount'
            ]

        ou           = 'Users'
        dnname       = 'uid'

        def _gecos (self) :
            return ','.join ((self.realname, self.phone))
        # end def _gecos
        gecos = property (_gecos)

        def _gid (self) :
            return int (self.group.gid)
        # end def _gid
        gid = property (_gid)

        def _mail_addresses (self) :
            return [self.username, self.nickname]
        # end def _mail_addresses
        mail_addresses = property (_mail_addresses)

        def _sid (self) :
            return ''.join \
                (( self.user_dynamic.org_location.smb_domain.sid
                 , '-'
                 , str (int (self.uid * 2 + 1000))
                ))
        # end def _sid
        sid = property (_sid)

        def _group_sid (self) :
            return self.group.sid
        # end def _group_sid
        group_sid = property (_group_sid)

        _cache_ud = None

        def _user_dynamic (self) :
            if self._cache_ud : return self._cache_ud
            date = '.'
            dyn  = get_user_dynamic (self.db, self.id, date)
            if not dyn :
                raise AttributeError, "No valid dynamic user record for %s %s" \
                    % (self.username, date.pretty (ymd))
            self._cache_ud = self.master.User_dynamic (dyn.id)
            return self._cache_ud
        # end def _user_dynamic
        user_dynamic = property (_user_dynamic)

        def _org_location (self) :
            return self.user_dynamic.org_location
        # end def _org_location
        org_location = property (_org_location)

    # end class User

    class Org_location (Roundup) :
        """
            Encapsulate the roundup org_location class.
            Include dn orgpath computation needed for dn computation in
            other classes.
        """

        def _orgpath (self) :
            return sum \
                ( [x.domain_part.split ('.') for x in
                    (self.location, self.organisation)
                  ]
                , []
                )
        # end def _orgpath
        orgpath = property (_orgpath)

        def _ip_subnet (self) :
            sn = self.db.ip_subnet.find (org_location = self.id)
            sn = [self.master.Ip_subnet (i) for i in sn]
            return sn
        # end def _ip_subnet
        ip_subnet = property (_ip_subnet)

        def _domain (self) :
            return '.'.join (self.orgpath)
        # end def _domain
        domain = property (_domain)

        def dhcp_header (self) :
            return textwrap.dedent \
                (("""
                     #####################################################
                     # dhcpd.conf created: %s
                     # Configuration file for ISC dhcpd
                     # THIS FILE WAS AUTOMATICALLY GENERATED - DO NOT EDIT
                     #####################################################
                     
                     authoritative;
                     option domain-name "%s";
                     server-name "%s.%s";
                     
                  """)
                % ( Date ('.').pretty ('%Y-%m-%d %H:%M:%S')
                  , self.domain
                  , self.dhcp_server.name
                  , self.domain
                  )
                )
        # end def dhcp_header

        def as_dhcp (self) :
            dhcp = [self.dhcp_header ()]
            for sn in self.ip_subnet :
                dhcp.append (sn.as_dhcp ())
            return '\n'.join (dhcp)
        # end def as_dhcp

    # end class Org_location

    class Ip_subnet (Roundup) :

        def _ip_netmask (self) :
            return common.subnet_mask (self.netmask)
        # end def _ip_netmask
        ip_netmask = property (_ip_netmask)

        def _ip_broadcast (self) :
            return common.broadcast_address (self.ip, self.netmask)
        # end def _ip_broadcast
        ip_broadcast = property (_ip_broadcast)

        def _ip_subnet (self) :
            num_ip = common.ip_as_number (self.ip, self.netmask)
            return common.numeric_ip_to_string (num_ip)
        # end def _ip_subnet
        ip_subnet = property (_ip_subnet)

        def _domain (self) :
            return '.'.join (self.org_location.orgpath)
        # end def _domain
        domain = property (_domain)

        def _samba_name_servers (self) :
            sd  = self.org_location.smb_domain
            if sd :
                r = []
                for n in sd.netbios_ns :
                    r.append ('.'.join ((n.name, self.domain)))
            return []
        # end def _samba_name_servers
        samba_name_servers = property (_samba_name_servers)

        def _samba_dd_server (self) :
            sd  = self.org_location.smb_domain
            if sd :
                n = sd.netbios_dd
                if n :
                    return '.'.join ((n.name, self.domain))
            return None
        # end def _samba_dd_server
        samba_dd_server = property (_samba_dd_server)

        def ip_addresses (self) :
            ips = self.db.network_address.find \
                (org_location = self.org_location.id)
            ips = (self.master.Network_address (i) for i in ips)
            return \
                (i for i in ips
                 if common.ip_in_subnet (i.ip, self.ip, self.netmask)
                )

        # end def ip_addresses

        dhcp_options = \
            [ ('subnet-mask',          'ip_subnet')
            , ('broadcast-address',    'ip_broadcast')
            , ('routers',              'routers')
            , ('domain-name-servers',  'dns_servers')
            , ('netbios-name-servers', 'samba_name_servers')
            , ('netbios-dd-server',    'samba_dd_server')
            ]

        def as_dhcp (self) :
            dhcp = []
            dhcp.append \
                ('subnet %s netmask %s' % (self.ip_subnet, self.ip_netmask))
            dhcp.append ('{')
            if self.default_lease_time :
                dhcp.append \
                    ('    default-lease-time %d;' % self.default_lease_time)
            if self.max_lease_time :
                dhcp.append ('    max-lease-time %d;' % self.max_lease_time)
            for opt in self.dhcp_options :
                attr = getattr (self, opt [1])
                if attr :
                    arg = attr
                    if isinstance (attr, list) :
                        arg = ', '.join (attr)
                    dhcp.append ('    option %s %s;' % (opt [0], arg))
            if self.dhcp_range :
                dhcp.append ('    range %s;' % self.dhcp_range)
            dhcp.append ('')
            for na in self.ip_addresses () :
                ni   = na.network_interface
                mn   = na.machine_name
                name = mn.name or na.ip
                if not na.use_dhcp or not ni :
                    continue
                dhcp.append ('    # %s' % ni.description)
                dhcp.append ('    %s' % name)
                dhcp.append ('    {')
                dhcp.append ('        hardware ethernet %s;' % ni.mac)
                if mn :
                    dhcp.append \
                        ('        fixed-address %s.%s;'
                        % (mn.name, self.org_location.domain)
                        )
                    dhcp.append ('        option host-name "%s";' % mn.name)
                else :
                    dhcp.append ('        fixed-address %s;' % na.ip)
                dhcp.append ('    }')
                dhcp.append ('')
            dhcp.append ('}')
            return '\n'.join (dhcp)
        # end def as_dhcp

    # end class Ip_subnet

    class Network_address (Roundup) :
        """
            Encapsulate the roundup network_address class.
        """

        def _machine_name (self) :
            machines = self.db.machine_name.filter \
                ( None
                , dict (network_address = self.id, do_reverse_mapping = True)
                )
            if machines : return self.master.Machine_name (machines [0])
            return None
        # end def _machine_name
        machine_name = property (_machine_name)

    # end class Network_address
# end class Roundup_Access
