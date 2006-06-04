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

from roundup.cgi.TranslationService import get_translation
from roundup.date                   import Date, Range
try :
    from happydoc.StructuredText import StructuredText
except ImportError :
    StructuredText = None

_ = None

if StructuredText :
    date_help  = StructuredText (Date.__doc__,  level = 1, header = 0)
    range_help = StructuredText (Range.__doc__, level = 1, header = 0)
else :
    date_help  = Date.__doc__ 
    range_help = Range.__doc__

daily_hours = \
    ""'''Expected daily work-time for %(Classname)s for each day of
         the week. If nothing is specified, the average of Weekly
         hours is taken. The field is mainly needed for part-time
         employees with irregular work time.
      '''
date_text = "<br><br>Ranges are used for searching dates: A range ".join \
    ((date_help, range_help))
deadline = \
    ""'''Planned time by which this %(Classname)s should be done.'''
durations = \
    ""'''Flag if booking of durations is allowed for this %(Classname)s.'''
leave_empty = \
    ""'''Leave this field empty if unsure.'''
keywords = \
    ""'''Some %(Property)s for tagging your issue -- can be useful
         for querying.
      '''
miss_text = \
    ""'''If you miss an %(Property)s here, feel free to vote for it with
         an IT-Issue in category roundup.
      '''
multiple_allowed = \
    ""'''Multiple %(Classname)s entries are allowed.'''
priority = \
    ""'''Priority for this %(Classname)s.'''
range_description = \
    ""'''as a comma-separated list of ranges (a special case of a range
         is just one number), e.g., 1-100,300-500
      '''
superseder = \
    ""'''This %(Classname)s has been closed as a duplicate against
         another %(Classname)s.
      '''
travel = \
    ""'''Flag to indicate travel. In the Time mask no lunchbreak will
         be computed. Even if enabled, no maximum work hours will be
         enforced for this %(Classname)s.
      '''
work_loc = \
    ""'''Location where you worked.'''

_helptext = \
    { ""'active'                     :
      [""'''Set if this %(Classname)s is active.''']
    , ""'area'                       :
      [""'''Where this issue belongs to.'''
      , miss_text
      ]
    , ""'time_project_status.active' :
      [ ""'''Set if this %(Classname)s is active. This determines if new
             work packages may be created for a project with this activity
             status. If a status is marked active, new work packages may
             be created for a project with this status.
          '''
      ]
    , ""'activity'                   :
      [""'''Date of last change''']
    , ""'actor'                      :
      [""'''Person who has done the last change''']
    , ""'alias'                      :
      [""'''Email alias''']
    , ""'alias_to_alias'             :
      [""'''Other aliases this %(Classname)s maps to''']
    , ""'alias_to_user'              :
      [""'''List of users this %(Classname)s maps to''']
    , ""'alternate_addresses'        :
      [""'''Alternate email addresses for this user, one per line''']
    , ""'announcements'              :
      [""'''Announcements for this %(Classname)s''']
    , ""'add_announcement'           :
      [""'''Mail out an announcement for another review step''']
    , ""'author'                     :
      [""'''Author of this %(Classname)s''']
    , ""'authors'                    :
      [""'''Authors of the artefact of this %(Classname)s''']
    , ""'bookers'                    :
      [ ""'''Users who may book on this %(Classname)s. If nothing is
             selected here, all users may book on this %(Classname)s (e.g.,
             jour fixe).
          '''
      ]
    , ""'booking_allowed'            :
      [ ""'''User is allowed to book time records during the validity span
             of the given %(Classname)s
          '''
      ]
    , ""'card_type'                  :
      [""'''Type of this %(Classname)s''']
    , ""'category'                   :
      [ ""'''Category of %(Classname)s. Where this %(Classname)s belongs
             to. Each category has a Category-Responsible who is
             responsible directly after creation if not specified
             otherwise.
          '''
      , miss_text
      , leave_empty
      ]
    , ""'clearance_by'               :
      [ ""'''Usually the supervisor of a person approves
             time records. This can be delegated using this attribute. It
             specifies the person who approves time records for
             all people whose supervisor this is.
          '''
      ]
    , ""'closed'                    :
      [""'''When this %(Classname)s was closed. Automatically set by
            Roundup.
         '''
      ]
    , ""'company'                    :
      [""'''Company for %(Classname)s''']
    , ""'composed_of'                :
      [""'''Set automagically by roundup on %(Classname)ss being Part of
            another %(Classname)s.
         '''
      ]
    , ""'confirm'                    :
      [ ""'''Confirm the password here: first password and this entry
             must match.
          '''
      ]
    , ""'content'                    :
      [""'''Content of %(Classname)s''']
    , ""'cost_center_group_id'       :
      [ ""'''ID of this record, automatically generated by the system.
             Cannot be changed by the user.
          '''
      ]
    , ""'cost_center_status'         :
      [""'''Specifies the Phase the Cost Center is in''']
    , ""'creation'                   :
      [""'''Record creation date''']
    , ""'creator'                    :
      [""'''Person who created this record''']
    , ""'cut_off_date'               :
      [ ""'''Date until when this %(Classname)s must be finished.'''
      , date_text
      ]
    , ""'date'                       :
      [ ""'''Date of this %(Classname)s.<br>'''
      , date_text
      ]
    , ""'daily_hours'                : [daily_hours]
    , ""'daily_worktime'             :
      [""'''Maximum time a person may book for a single day.''']
    , ""'defect.superseder'          :
      [superseder]
    , ""'deadline'                   :
      [deadline]
    , ""'default_lease_time'         :
      [""'''Default DHCP lease time for %(Classname)s''']
    , ""'department'                 :
      [""'''Department in which the %(Classname)s is based, e.g., SW, Sales.''']
    , ""'depends'                    :
      [""'''A comma seperated list of %(Classname)s IDs this
            %(Classname)s depends on. This information is used for the
            planning process and should only contain the IDs of the
            issues this issue needs in order to be worked on, e.g., we
            actually need a specification before we can start to work on
            it. If you have some dependencies here, the depending
            %(Classname)ss are hyperlinked.
         '''
      ]
    , ""'deputy'                     :
      [""'''Substitute for the responsible Person of %(Classname)s''']
    , ""'description'                :
      [""'''Verbose description of %(Classname)s''']
    , ""'dhcp_range'                 :
      [""'''Range of dynamic IP addresses for %(Classname)s -- used
            when generating DHCP configuration. Format: Two IP addresses in
            dot notation separated by a dot. Example:
            10.100.99.20&nbsp;10.100.99.250
         '''
      ]
    , ""'dhcp_server'                :
      [""'''DHCP Server for this %(Classname)s''']
    , ""'dist'                       :
      [ ""'''Distribute: In a first step you can enter Start and End time
             for each day or the hours you worked during the day. In a
             second step you can distribute these hours to the different
             work packages you worked on during the week by entering the
             work package and the number of hours into the "Distr." field.
             The remaining hours will be distributed to your time records
             which don\'t have a work package associated.
             This mechanism works after you press "Save" and will split a
             single time record into two if necessary.
          '''
      ]
    , ""'dns_record_type'            :
      [ ""'''Type of DNS record generated. If the $(Classname)s points to
             another %(Classname)s a CNAME is generated, otherwise an
             A-record is assumed. If no DNS information should be
             generated, this field should be set to "invalid".
             This field is auto-generated if left empty.
          '''
      ]
    , ""'dns_servers'                :
      [ ""'''DNS Servers for this %(Classname)s, used when generating
             the DHCP configuration.
          '''
      ]
    , ""'do_reverse_mapping'         :
      [ ""'''Flag if a reverse DNS entry should be created for this
             %(Classname)s -- should usually be enabled. If a
             %(Classname)s has multiple A-Records (which is bad style to
             say the least) this flag must be set for only one of the
             multiple A-Records. The flag is ignored for CNAME records.
          '''
      ]
    , ""'domain_part'                :
      [ ""'''Part of a domain name. The domain name is built by
             concatenation the names of the Organisation and the Location.
          '''
      ]
    , ""'domino_dn'                  :
      [ ""'''Distinguished name for Domino users -- needed for alias
             generation.
          '''
      ]
    , ""'duration'                   :
      [ ""'''Work duration in hours, e.g. 7.25 -- only quarter hours
             allowed, e.g., 7.10 is not allowed. The duration is created
             automatically by the system when you specify "Start" and
             "End". Attention: If you specify both, "Start" and "Duration"
             with a duration of more than six hours, the system will
             consult your user preferences and add the lunch break, e.g.
             specifying "Start" 10:00 and "Duration" 8 will result in an
             "End" time of 18:30.
          '''
      ]
    , ""'earliest_start'             :
      [""'''When this %(Classname)s can be started to work on. Used to
            specify external dependencies (e.g., availability of
            hardware). 
         '''
      ]
    , ""'effort'                     :
      [ ""'''The estimated effort this work package has. This should be
             a fair estimation done by the Responsible of the
             %(Classname)s. Be sure to set it for Change-Requests
             because otherwise one (1!) day will be used as a rough
             guess for the planning procedure -- which -- in most
             circumstances -- will NOT be sufficient. The format is
             checked and should be *a number* followed by either *P* or
             *M* which stands for *People* or *Man*, directly followed
             by *D*, *W*, or *M* for *Day*, *Week*, or *Month*,
             respectively. Optionally the person who estimated can be
             specified in parenthesis, e.g, *15 PD (priesch)* means: 15
             PeopleDays estimated by priesch.
          '''
      ]
    , ""'email'                      :
      [""'''Email address for this %(Classname)s''']
    , ""'end'                        :
      [ ""'''Format xx:xx  (e.g. 17:00), is created automatically by the
             system when you specify "Start" and "Duration". Attention: If
             you specify both, "Start" and "End", with more than six hours
             in between, the system will consult your user preferences and
             subtract the lunch break, e.g. specifying "Start" 10:00 and
             "End" 18:00 will result in a duration of 7.5 hours (because
             half an hour lunch break was subtracted).
          '''
      ]
    , ""'external_phone'             :
      [ ""'''Short mobile or external phone number, e.g., 6142.
             Can be concatenated with
             the company prefix stored in "Organisation" to form a valid
             external phone number.
          '''
      ]
    , ""'add_file'                   :
      [""'''Add an new file for %(Classname)s''']
    , ""'files'                      :
      [""'''Files for %(Classname)s''']
    , ""'files_affected'             :
      [""'''The %(Property)s entry field is used to identify which
            file(s) has/have been changed during the modifications
            requested by the current issue, containing the unique
            filename and path and the new version. The CVS output from
            the command *VCFiltered_Commit* shall be used to fill in
            this field!

            Example: Consider changed files *os_start.c*, *os_start.h*,
            and *os_version.c* in *projects/SW/external/ttpos/src/os*,
            resulting in *TTP-OS Version 4.5.23*. The entry to
            %(Property)s shall look like::

             VCupdate -r1.45 projects/SW/external/ttpos/src/os/os_start.c
             VCupdate -r1.23 projects/SW/external/ttpos/src/os/os_start.h
             VCupdate -r1.213 projects/SW/external/ttpos/src/os/os_version.c
         '''
      ]
    , ""'final_meeting_date'         :
      [ ""'''Date of final meeting for this %(Classname)s.'''
      , date_text
      ]
    , ""'firstname'                  :
      [""'''First name for this user, e.g., Ralf''']
    , ""'fixed_in'                   :
      [""'''Provide the version number where you fixed it. Is needed
            when you change the status to testing.
            The %(Property)s field contains the build version of the
            complete artefact. In the Example from Files affected the
            entry for %(Property)s shall look like::
      
              TTP-OS 4.5.23
         '''
      ]
    , ""'gid'                        :
      [""'''Numeric group ID''']
    , ""'gid_range'                  :
      [ ""'''Allowed range of group ids'''
      , range_description
      ]
    , ""'group'                      :
      [""'''UNIX Group for this %(Classname)s''']
    , ""'home_directory'             :
      [""'''UNIX home directory for %(Classname)s''']
    , ""'hours_mon'                  : [daily_hours]
    , ""'hours_tue'                  : [daily_hours]
    , ""'hours_wed'                  : [daily_hours]
    , ""'hours_thu'                  : [daily_hours]
    , ""'hours_fri'                  : [daily_hours]
    , ""'hours_sat'                  : [daily_hours]
    , ""'hours_sun'                  : [daily_hours]
    , ""'id'                         :
      [ ""'''ID of this record, automatically generated by the system.
             Cannot be changed by the user.
          '''
      ]
    , ""'initial'                    :
      [""'''Initials of this %(Classname)s''']
    , ""'inreplyto'                  :
      [""'''In Reply To field if this %(Classname)s was received by email''']
    , ""'inventory_no'               :
      [ ""'''Unique number or name for this %(Classname)s, preferrably the
             inventory number for asset tracking
          '''
      ]
    , ""'ip'                         :
      [""'''Internet protocol address of this %(Classname)s''']
    , ""'ip_subnet'                  :
      [""'''Internet protocol subnet''']
    , ""'is_alias'                   :
      [""'''No real user but only an email alias''']
    , ""'is_lotus_user'              :
      [""'''Enable this if the %(Classname)s uses Lotus Notes for mail''']
    , ""'issue.deadline'             :
      [ deadline
      , ""'''Should only be entered on Top-Level workpackages which are
             either one single task of work or composed of one or more
             subpackages. It should definitely NOT be used to force
             dependencies of work packages (e.g. start b after a has
             finished on a given date)!!! -- This is done automatically
             by the planning tool via the Depends and Part Of fields.
          '''
      ]
    , ""'it_issue.superseder'        :
      [superseder, multiple_allowed]
    , ""'it_prio'                    :
      [ priority
      , leave_empty
      ]
    , ""'it_project'                 :
      [""'''Optional IT Project to which this %(Classname)s belongs''']
    , ""'keywords'                   :
      [keywords]
    , ""'kind'                       :
      [""'''What this issue actually is. Be sure to exactly distinguish
            between what is actually a Bug (it is not working as
            expected) and a Change-Request!
         '''
      ]
    , ""'klass'                      :
      [""'''Class for this query''']
    , ""'last_gid'                   :
      [""'''Last used gid in this %(Classname)s''']
    , ""'last_machine_uid'           :
      [""'''Last used machine uid in this %(Classname)s''']
    , ""'last_uid'                   :
      [""'''Last used uid in this %(Classname)s''']
    , ""'lastname'                   :
      [""'''Last name for this user, e.g., Schlatterbeck''']
    , ""'link_field'                 :
      [ ""'''Auxiliary field for use with other software, e.g., asset
             tracking
          '''
      ]
    , ""'location'                   :
      [""'''Location of %(Classname)s, e.g., Vienna HQ.''']
    , ""'login_shell'                :
      [""'''UNIX login shell for %(Classname)s''']
    , ""'lunch_duration'             :
      [""'''Preference for time tracking, duration of lunch break in hours''']
    , ""'lunch_start'                :
      [""'''Preference for time tracking, start of lunch break''']
    , ""'mac'                        :
      [ ""'''MAC Address (medium access control layer) e.g. ethernet
             hardware address. Should be six hex-numbers separated by
             colons, e.g. "10:0:0:0:0:0".
          '''
      ]
    , ""'machine'                    :
      [ ""'''A machine connected to the network to which this
             %(Classname)s belongs
          '''
      ]
    , ""'machine_group'              :
      [""'''Group for pseudo-accounts for machines (used for Samba)''']
    , ""'machine_name'               :
      [""'''Link to another %(Classname)s -- converted to a CNAME.''']
    , ""'machine_uid'                :
      [""'''Numeric user id for this samba machine.''']
    , ""'machine_uid_range'          :
      [ ""'''Allowed range of user ids for machines'''
      , range_description
      ]
    , ""'manager'                    :
      [""'''Responsible person of the %(Classname)s''']
    , ""'max_hours'                  :
      [ ""'''If given for a %(Classname)s restricts the number of hours
             you can book on this %(Classname)s for a single day.
          '''
      ]
    , ""'max_lease_time'             :
      [""'''Maximum DHCP lease time for %(Classname)s''']
    , ""'messageid'                  :
      [""'''Message-ID if this message was received via email''']
    , ""'messages'                   :
      [""'''List of messages for %(Classname)s''']
    , ""'msg'                        :
      [""'''New message or notice for %(Classname)s''']
    , ""'msg_keywords'               :
      [keywords]
    , ""'name'                       :
      [""'''Unique %(Classname)s name''']
    , ""'name_version'               :
      [ ""'''Unique name of this %(Classname)s, including the version
             number
          '''
      ]
    , ""'netbios_dd'                 :
      [ ""'''Netbios datagram distribution server (NBDD) option for DHCP
             config. Specifies list of servers in order of preference.
          '''
      ]
    , ""'netbios_ns'                 :
      [ ""'''Netbios name server (NBNS) option for DHCP config. Specifies
             list of servers in order of preference. Netbios name service
             is more commonly referred to as WINS.
          '''
      ]
    , ""'netbios_nodetype'           :
      [ ""'''The Netbios node type option allows NetBIOS over TCP/IP
             clients which are configurable to be configured as described
             in RFC 1001/1002. The value is specified as a single octet
             which identifies the client type. Possible types are:
             1: B-node: Broadcast - no WINS, 2: P-node: Peer - WINS only,
             4: M-node: Mixed - broadcast, then WINS, 8: H-node: Hybrid -
             WINS, then broadcast. (taken from dhcp-options manual page)
          '''
      ]
    , ""'netmask'                    :
      [""'''IP net mask for this %(Classname)s, a number (e.g., 16).''']
    , ""'network_address'            :
      [ ""'''Address in the network, including but not limited to IP
             address
          '''
      ]
    , ""'network_interface'          :
      [ ""'''Hardware unit to connect to the network. Can be part of the
             motherboard or can be a separate unit
          '''
      ]
    , ""'nickname'                   :
      [""'''Nickname (or short name) for this %(Classname)s, e.g., rsc''']
    , ""'nosy'                       :
      [""'''People receiving announcements (messages) for %(Classname)s''']
    , ""'op_project'                 :
      [ ""'''Flag if this %(Classname)s is a real project or just used for
             time tracking.
          '''
      ]
    , ""'opt_reviewers'              :
      [""'''Optional reviewers for this %(Classname)s''']
    , ""'order'                      :
      [""'''Items are ordered by this property in drop-down boxes etc.''']
    , ""'organisation'               :
      [""'''Organisation in which the %(Classname)s is based, e.g., TTTech.''']
    , ""'org_location'               :
      [ ""'''Organisation and location of this %(Classname)s, cartesian
             product of organisation and location -- only the combinations
             that really exist are stored in the database of course.
          '''
      ]
    , ""'organisation_id'            :
      [ ""'''ID of this record, automatically generated by the system.
             Cannot be changed by the user.
          '''
      ]
    , ""'owner'                      :
      [""'''User/Owner of this %(Classname)s''']
    , ""'operating_system'           :
      [""'''Operating System running on this %(Classname)s''']
    , ""'part_of'                    :
      [""'''If you have a Top-Level work package which consists of other
            work packages, you should enter the parent work package
            here. This information is needed for the planning process in
            order to define what %(Classname)ss compose a larger
            project, e.g., Define one Top-Level work package Some New
            Feature which is composed of Design, Build Hardware, Write
            Software, Put all parts together, and Test.
         '''
      ]
    , ""'password'                   :
      [""'''Password for this %(Classname)s''']
    , ""'peer_reviewers'             :
      [""'''Peer reviewers for this %(Classname)s''']
    , ""'phone'                      :
      [ ""'''Short phone number (suffix) only, e.g., 42.
             Can be concatenated with
             the company prefix stored in "Organisation" to form a valid
             external phone number.
          '''
      ]
    , ""'planned_effort'             :
      [ ""'''Effort for %(Classname)s in person-hours; as it is stated
             in the Project Evaluation Sheet. Warning: This used to be in
             person days, so you have to convert old values to hours!
          '''
      ]
    , ""'priority'                   :
      [ priority
      , ""'''Should be set between 0 and 100. For the planning process
             only issues above a specified priority level are taken into
             account. On creation of a new issue, the priority is
             automatically set to 100.
          '''
      ]
    , ""'private_for'                :
      [""'''Flag if this is a private %(Classname)s''']
    , ""'private_gid_range'          :
      [ ""'''Allowed range of group ids for users'''
      , range_description
      ]
    , ""'private_phone'              :
      [ ""'''Privat phone number. Always as a full number valid on the
             PSTN.
          '''
      ]
    , ""'project'                    :
      [ ""'''%(Classname)s is part of a Time Category. With the Time
             Category name a
             %(Classname)s can be clearly  identified
          '''
      ]
    , ""'qa_representative'          :
      [""'''Representative from the QA department for this %(Classname)s''']
    , ""'queries'                    :
      [""'''Queries for this %(Classname)s''']
    , ""'recorder'                   :
      [""'''Person responsible for recording findings''']
    , ""'realname'                   :
      [ ''"""Real name for this %(Classname)s -- automatically generated
             by the system from first and last name. Needed by roundup
             internally. (More specifically by roundupdp.py\'s send_message
             -- which is used e.g. by the nosyreactor)
          """
      ]
    , ""'recipients'                 :
      [""'''Only set if message was received via email.''']
    , ""'release'                    :
      [ ""'''The %(Property)s this %(Classname)s belongs to -- if
             available (e.g. 4.3.72 for TTP-Plan).
          '''
      ]
    , ""'remove'                     :
      [ ""'''Remove attached item. Will not remove item from the database,
             it can usually still be downloaded via the History button.
          '''
      ]
    , ""'responsible'                :
      [""'''Person who is responsible for the %(Classname)s''']
    , ""'review.responsible'         :
      [ ""'''Moderator for %(Classname)s -- Note: If you do not specify
             the moderator, you will get an indication that the field
             "Responsible" must be filled in -- the moderator is reponsible for
             %(Classname)s.
          '''
      ]
    , ""'roles'                      :
      [ ""'''Roles for this %(Classname)s -- to give the user more than
             one role, enter a comma,separated,list
          '''
      ]
    , ""'room'                       :
      [""'''Room number''']
    , ""'routers'                    :
      [""'''Routers for this %(Classname)s, used in DHCP configuration.''']
    , ""'samba_home_drive'           :
      [""'''Home drive for %(Classname)s in Windows''']
    , ""'samba_home_path'            :
      [""'''Path to %(Classname)ss home directory''']
    , ""'samba_kickoff_time'         :
      [""'''Windows time that user will automatically logged out''']
    , ""'samba_lm_password'          :
      [ ""'''Samba LAN Manager password -- automatically computed when a
             new password is entered
          '''
      ]
    , ""'samba_logon_script'         :
      [""'''Logon script for %(Classname)s''']
    , ""'samba_nt_password'          :
      [ ""'''Samba NT password -- automatically computed when a
             new password is entered
          '''
      ]
    , ""'samba_profile_path'         :
      [""'''Path to profile for %(Classname)s''']
    , ""'samba_pwd_can_change'       :
      [ ""'''Earliest time the user may change the password next time.
             set by the system to pwd_last_set if nothing else is enabled.
          '''
      ]
    , ""'samba_pwd_last_set'         :
      [ ""'''Time-stamp the password was last changed, automatically
             computed by the system
          '''
      ]
    , ""'samba_pwd_must_change'      :
      [ ""'''Latest time the user must change the password next time.
             set by the system to end of the epoch if nothing else is enabled.
          '''
      ]
    , ""'secondary_groups'           :
      [""'''secondary UNIX Groups for this %(Classname)s''']
    , ""'shadow_last_change'         :
      [ ""'''Time-stamp the shadow password was last changed,
             automatically computed by the system
          '''
      ]
    , ""'shadow_expire'              :
      [ ""'''Date at which the users\'s account expires and will no longer
             be accessible.
          '''
      ]
    , ""'shadow_inactive'            :
      [ ""'''Number of days of inactivity after a password has expired
             before the account is locked. Note that when the password has
             expired the user is required to change it before login is
             possible. If no login occurs for a certain time, the account
             can be disabled with this setting.
          '''
      ]
    , ""'shadow_max'                 :
      [ ""'''Maximum days after last change when the shadow password must
             be changed again.
          '''
      ]
    , ""'shadow_min'                 :
      [ ""'''Minimum days after last change when the shadow password may
             be changed again.
          '''
      ]
    , ""'shadow_used'                :
      [ ""'''Flag if shadow information should be generated, will be
             translated to LDAP shadowFlag.
          '''
      ]
    , ""'shadow_warning'             :
      [ ""'''Early warning in days before the user is required to change
             the password.
          '''
      ]
    , ""'sid'                        :
      [ ""'''Samba unique ID but without the last part used for user id or
             group id information
          '''
      ]
    , ""'smb_domain'                 :
      [""'''Samba domain for this %(Classname)s''']
    , ""'smb_name'                   :
      [""'''Samba name for this %(Classname)s in the samba domain''']
    , ""'stakeholder'                :
      [ ""'''Person by/for whom this %(Classname)s was raised. Usually
             defaults to the creator of the %(Classname)s, but can be
             overridden (e.g. when the IT-Department documents an issue
             that came in via telephone).
          '''
      , leave_empty
      ]
    , ""'start'                      :
      [ ""'''Format xx:xx (e.g. 09:00), defines your start of work. Has to
             be specified except for absences like e.g. holidays or sick
             leave.
          '''
      ]
    , ""'status'                     :
      [""'''Status of this %(Classname)s. Automatically set on a new
            %(Classname)s if not set. There are constraints on status
            transitions.
         '''
      ]
    , ""'subject'                    :
      [""'''Short identification of this message''']
    , ""'substitute'                 :
      [ ""'''Person who can substitute %(Classname)s for approving time
             records.
          '''
      ]
    , ""'subst_active'               :
      [ ""'''This field is set to "yes" for enabling the field
             "Substitute" for delegating time record approval.
          '''
      ]
    , ""'summary'                    :
      [""'''Short summary of this message (usually first line)''']
    , ""'superior'                   :
      [""'''Supervisor for %(Classname)s''']
    , ""'supp_weekly_hours'          :
      [ ""'''Weekly hours including the agreed supplementary hours (e.g.
             45h), Format: xx.xx. Please round to whole quarters of an hour
             (e.g. 0.5 means a half-hour).
          '''
      ]
    , ""'sync_with_ldap'             :
      [ ""'''Enabled if this %(Classname)s should be synched with ldap --
             when the user changes PW via PAM, the pw in roundup will be
             changed, too (if the daemon is running)
          '''
      ]
    , ""'team_members'               :
      [ ""'''Persons who are assigned to the project and are allowed
             to book their effort on this project
          '''
      ]
    , ""'time_activity'              :
      [""'''Specifies the kind of work you did (e.g. meeting, ...)''']
    , ""'time_start'                 :
      [""'''Date when %(Classname)s officially starts''']
    , ""'time_end'                   :
      [""'''Date when %(Classname)s is officially closed''']
    , ""'time_project.status'        :
      [ ""'''Status of this %(Classname)s. Note that this status is only
             used for determining if new work packages may be created for
             this %(Classname)s -- it is not used during time recording
             for determining if the user may book on a work package.
          '''
      ]
    , ""'timezone'                   :
      [""'''Time zone of this %(Classname)s -- this is a numeric hour offset''']
    , ""'title'                      :
      [""'''Title of this %(Classname)s -- an intuitive one-line
            description of %(Classname)s
         '''
      ]
    , ""'travel'                     : [travel]
    , ""'time_wp.travel'             : 
      [ travel
      , ""''' In addition in reports the times booked will be halved (if
             exceeding the expected work hours and the person is not
             marked "travel_full" in the dynamic user data)
          '''
      ]  
    , ""'transitions'                :
      [""'''Allowed transitions to other states''']
    , ""'tr_duration'                :
      [ ""'''Work duration in minutes including special travel computation:
             travel times will be halved if exceeding the maximum work
             hours.
          '''
      ]
    , ""'type'                       :
      [""'''Mime type of this file''']
    , ""'uid'                        :
      [""'''Numeric user ID''']
    , ""'uid_range'                  :
      [ ""'''Allowed range of user ids'''
      , range_description
      ]
    , ""'url'                        :
      [""'''Web-Link for this %(Classname)s''']
    , ""'use_dhcp'                   :
      [ ""'''Flag if this %(Classname)s should be served by the DHCP
             server.
          '''
      ]
    , ""'use_in_ln'                  :
      [ ""'''This %(Classname)s should be used with Lotus Notes (e.g.,
             no delivery to a program, etc. that is only possible with
             a real MTA)
          '''
      ]
    , ""'user_dynamic.durations_allowed' : [durations]
    , ""'user_password'              :
      [ ""'''UNIX user password, automatically set by the system when a
             new password is entered.
          '''
      ]
    , ""'user.address'               :
      [""'''Primary email address for this user''']
    , ""'user.title'                 :
      [""'''Academic title of %(Classname)s, e.g., Dipl. Ing.''']
    , ""'username'                   :
      [""'''Login-name for this %(Classname)s, e.g., schlatterbeck''']
    , ""'vacation_remaining'         :
      [ ""'''Remaining vacation for this user at the start of a dynamic
             user data record.
          '''
      ]
    , ""'vacation_yearly'            :
      [ ""'''Yearly vacation for this user: This is the amount of vacation
             that is added for each year.
          '''
      ]
    , ""'valid_from'                 :
      [ ""'''Creation date, or date since when this %(Classname)s can be
             booked at 
          '''
      , date_text
      ]
    , ""'valid_to'                   :
      [ ""'''Expiration date for %(Classname)s. Note that the date given
             here is *not* itself part of the validity time.
          '''
      , date_text
      ]
    , ""'week'                       :
      [ ""'''Week for time tracking, this is an alternative for specifying
             a date range: just enter the week number here (for the
             current year) or YYYY/WW where YYYY is the year and WW the
             week number for that year.
          '''
      ]
    , ""'weekend_allowed'            :
      [""'''Flag if booking on weekends is allowed for this %(Classname)s.''']
    , ""'weekly_hours'               :
      [""'''Expected weekly work-time for %(Classname)s.''']
    , ""'wp'                         :
      [ ""'''Only work packages where you have permission to register show
             here. If you miss one, please contact the responsible project
             manager
          '''
      ]
    , ""'wp_no'                      :
      [ ""'''Work package number in the project. Number must be unique for
             the project and cannot be changed after assignment.
          '''
      ]
    , ""'wp.durations_allowed'       :
      [ durations
      , ""'''This is mainly used for special %(Classname)ss, like,
             e.g., vacation.
          '''
      ]
    , ""'wps'                        :
      [ ""'''For a better handling of the work load of a project it is
             split in to work packages. This field defines a list of work
             packages for this %(Classname)s
          '''
      ]
    , ""'work_location'              : [work_loc]
    , ""'time_project.work_location' :
      [ work_loc
      , ""''' If a value is given here, the work location will be
             corrected for all time records booked on work packages of
             this project.
          '''
      ]
    }

def combined_name (cls, attr) :
    """ Produce a combined name of class and attribute of the class. If
        a help-text exists for the combination, return the combination,
        otherwise return only the attribute. In this way we can override
        help-texts by specifying a help-text entry with the key
        classname.attribute.
    """
    pname = '%s.%s' % (cls, attr)
    if pname in _helptext :
        return pname
    return attr
# end def combined_name

def help_properties (klass) :
    """Return all class properties plus some more for which help texts
       should be displayed (e.g., "message" which describes the message
       window). The parameter klass is a html klass.
    """
    p = []
    properties = klass._klass.getprops ()
    if 'messages' in properties :
        p.append ('msg')
    if klass.classname == 'user' :
        p.append ('confirm')
    if klass.classname == 'daily_record' :
        p.append ('week')
    if klass.classname == 'file' :
        p.append (""'remove')
    if klass.classname == 'user_dynamic' :
        p.append (""'daily_hours')
    if 'announcements' in properties :
        p.append ('add_announcement')
    if 'files' in properties :
        p.append ('add_file')
    for i in properties.iterkeys () :
        pname = combined_name (klass.classname, i)
        if pname in _helptext :
            p.append (pname)
    p = [(_ (i).decode ('utf-8'), i) for i in p]
    p.sort ()
    return [i [1] for i in p]
# end def help_properties

def fieldname (cls, name, fieldname = None, endswith = '&nbsp;') :
    if not fieldname : fieldname = name
    prop  = combined_name (cls, fieldname)
    if not prop in _helptext :
        return "%s%s" % (_ (prop), endswith)
    label = _ (prop)
    return ("""<a title="Help for %s" href="javascript:help_window"""
            """('%s?:template=property_help#%s', '500', '400')">"""
            """%s%s</a>""" \
            % (label, cls, prop, label, endswith)
           )

# end def fieldname

def helptext (key) :
    return ' '.join (_ (h) for h in _helptext [key])
# end def helptext

def init (instance) :
    global _
    _   = get_translation \
        (instance.config.TRACKER_LANGUAGE, instance.tracker_home).gettext
    instance.registerUtil ('helptext',        helptext)
    instance.registerUtil ('help_properties', help_properties)
    instance.registerUtil ('fieldname',       fieldname)
# end def init
