# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004 TTTech Computertechnik AG. All rights reserved
# Schönbrunnerstraße 7, A--1040 Wien, Austria. office@tttech.com
#
#++
# Name
#    user
#
# Purpose
#    Detectors for user class
#
# Revision Dates
#    14-Oct-2004 (MPH) Creation
#     9-Nov-2004 (MPH) Renamed to user.py
#     1-Dec-2004 (MPH) Added `update_userlist_html`
#     5-Apr-2005 (MPH) Changed `tmpnam` to `mkstemp`, fire
#                      `update_userlist_html` on user.create also, removed
#                      `None` from `is_alias` filterspec
#     6-Apr-2005 (MPH) Fixed use of mkstemp
#    27-Jul-2005 (RSC) is_alias -> status
#    ««revision-date»»···
#--
#
import os
import shutil
pjoin = os.path.join
from roundup.cgi.TranslationService import get_translation
from tempfile                       import mkstemp
from roundup.date                   import Date
from roundup.exceptions             import Reject
_      = lambda x : x
common = None

USER_SINGLE = """
<tal:block metal:define-macro="%(macro_name)s">
 <tal:block tal:condition="python:not context [name].is_edit_ok ()"
  tal:replace="python: context [name]"/>
 <select tal:attributes="name name"
  tal:condition="python: context [name].is_edit_ok ()">
  <option value=""
          tal:content="dont_care"></option>
  <!-- autogenerated -->
%(option_list)s
  <!-- autogenerated -->
</select>
<script language="javascript"
        tal:content="structure string:
<!--
select_box = document.${form}.${name};
for (i = 0; i < select_box.length; i++)
  {
    if (select_box.options [i].value == ${selected})
      select_box.options [i].selected = true;
    else
      select_box.options [i].selected = false;
  }
-->
"></script>
</tal:block>
"""

USER_MULTI = """
<tal:block metal:define-macro="%(macro_name)s">
 <tal:block tal:condition="python:not %(condition)s"
  tal:replace="python: context [name]"/>
 <select multiple tal:condition="python: %(condition)s"
         tal:attributes="size size;
                         name name">
  <option value=""
          tal:content="dont_care"></option>
  <!-- autogenerated -->
%(option_list)s
  <!-- autogenerated -->
</select>
<script language="javascript"
        tal:content="structure string:
<!--
select_box = document.${form}.${name};
selected   = new Array (${selected});
for (i = 0; i < select_box.length; i++)
  {
    for (j = 0; j < selected.length; j++)
      {
        if (select_box.options [i].value == selected [j])
          select_box.options [i].selected = true;
      }
  }
-->
"></script>
</tal:block>
"""

OPTION_FMT = """  <option value="%s">%s</option>"""

def common_user_checks (db, cl, nodeid, new_values) :
    ''' Make sure user properties are valid.
        - email address has no spaces in it
        - roles specified exist
    '''
    if new_values.has_key('address') and ' ' in new_values['address']:
        raise ValueError, 'Email address must not contain spaces'
    if new_values.has_key('roles'):
        roles = new_values ['roles'].strip ()
        if roles :
            roles = [x.lower().strip() for x in roles.split(',')]
            for rolename in roles:
                if not db.security.role.has_key(rolename):
                    raise ValueError, 'Role "%s" does not exist'%rolename
    # automatic setting of realname
    n = 'firstname'
    fn = new_values.get (n, None) or cl.get (nodeid, n) or ''
    n = 'lastname'
    ln = new_values.get (n, None) or cl.get (nodeid, n) or ''
    if  (   (  new_values.has_key ("firstname")
            or new_values.has_key ("lastname")
            )
        and nodeid
        ) :
        realname = " ".join ((fn, ln))
        new_values ["realname"] = realname
    if 'lunch_duration' in new_values :
        ld = new_values ['lunch_duration']
        if ld * 3600 % 900 :
            raise Reject, _ ("Times must be given in quarters of an hour")
        new_values ['lunch_duration'] = int (ld * 4) / 4.
        if ld > 8 :
            raise Reject, _ ("Lunchbreak of more than 8 hours? Sure?")
        if ld < .5 :
            raise Reject, _ ("Lunchbreak must be at least half an hour.")
    if 'lunch_start' in new_values :
        ls = new_values ['lunch_start']
        ls = Date (ls) # trigger date-spec error if this fails.
    if 'supervisor' in new_values :
        common.check_loop \
            (_, cl, nodeid, 'supervisor', new_values ['supervisor'])
    for a in 'uid', 'nickname' :
        if a in new_values :
            v = new_values [a]
            common.check_unique (_, cl, nodeid, ** dict (a, v))
            if a == 'nickname' :
                common.check_unique (_, cl, nodeid, username = v)
    if 'username' in new_values :
        common.check_unique (_, cl, nodeid, nickname = new_values ['username'])
    status = new_values.get ('status', None) or cl.get (nodeid, 'status')
    valid  = db.user_status.lookup ('valid')
    if 'uid' in new_values :
        uid     = new_values ['uid']
        uidname = _ ('uid')
        if status != valid :
            raise Reject, 'May not change %(uidname)s for invalid user' \
                % locals ()
        olo = new_values ['org_location'] or db.cl.get (nodeid, 'org_location')
        sd  = db.smb_domain.getnode (db.org_location.get (olo, 'smb_domain'))
        if not common.uid_or_gid_in_range (uid, sd.uid_range) :
            raise Reject, _("Invalid %(uidname)s: %(uid)s") % locals ()
        db.smb_domain.set (sd.id, last_uid = max (uid, sd.last_uid))
# end def common_user_checks

def create_dynuser (db, cl, nodeid, new_values) :
    db.user_dynamic.create \
        ( user         = nodeid
        , valid_from   = Date ('.')
        , org_location = cl.get (nodeid, 'org_location')
        , department   = cl.get (nodeid, 'department')
        )
# end def create_dynuser

def new_user (db, cl, nodeid, new_values) :
    for i in 'firstname', 'lastname', 'org_location', 'department' :
        if i not in new_values :
            raise Reject, "%(attr)s must be specified" % {'attr' : _ (i)}

    fn    = new_values ['firstname']
    ln    = new_values ['lastname']
    lfn   = common.tolower_ascii (fn)
    lln   = common.tolower_ascii (ln)
    id    = nodeid
    olo   = new_values ['org_location']
    valid = db.user_status.lookup ('valid')
    if 'status' not in new_values :
        new_values ['status'] = valid
    status = new_values ['status']
    if  ('nickname' not in new_values and status == valid) :
        nick = common.new_nickname (_, cl, nodeid, lfn, lln)
        if nick :
            new_values ['nickname'] = nick
    nickname   = new_values ['nickname']
    org        = db.org_location.get   (olo, 'organisation')
    maildomain = db.organisation.get   (org, 'mail_domain')
    sd         = db.smb_domain.getnode (db.org_location.get (olo, 'smb_domain'))
    username   = new_values ['username']

    # defaults:
    if new_values ['status'] == valid :
        if 'address' not in new_values :
            new_values ['address'] = \
                '@'.join (('.'.join ((lfn, lln)), maildomain))
        if 'alternate_addresses' not in new_values :
            new_values ['alternate_addresses'] = '\n'.join \
                (['@'.join ((i, maildomain)) for i in (nickname, lln) if i])
        if 'lunch_duration' not in new_values :
            new_values ['lunch_duration'] = .5
        if 'lunch_start'    not in new_values :
            new_values ['lunch_start'] = '12:00'
        if 'uid'            not in new_values :
            new_values ['uid'] = common.next_uid_or_gid \
                (sd.last_uid, sd.uid_range)
            uid = new_values ['uid']
            if 'group' not in new_values :
                new_values ['group'] = db.group.create \
                    ( name         = username
                    , gid          = uid
                    , org_location = olo
                    )
    common_user_checks (db, cl, nodeid, new_values)
# end def new_user

def audit_user_fields(db, cl, nodeid, new_values):
    for n in \
        ( 'firstname'
        , 'lastname'
        , 'lunch_duration'
        , 'lunch_start'
        , 'shadow_inactive'
        , 'shadow_max'
        , 'shadow_min'
        , 'shadow_warning'
        , 'uid'
        ) :
        if n in new_values and new_values [n] is None :
            raise Reject, "%(attr)s may not be undefined" % {'attr' : _ (n)}
    status = new_values.get ('status', cl.get (nodeid, 'status'))
    if status == db.user_status.lookup ('valid') :
        for n in \
            ( 'org_location'
            , 'department'
            ) :
            if n in new_values and new_values [n] is None :
                raise Reject, "%(attr)s may not be undefined" % {'attr' : _ (n)}
    common_user_checks (db, cl, nodeid, new_values)
# end def audit_user_fields

def update_userlist_html (db, cl, nodeid, old_values) :
    """newly create user_list.html macro page
    """
    root       = pjoin (db.config.TRACKER_HOME, "html")
    userlist   = "userlist.html"
    changed    = False
    for i in 'username', 'status', 'roles' :
        if  (  not old_values
            or i not in old_values
            or old_values [i] != cl.get (nodeid, i)
            ) :
            changed = True
    if not changed :
        return
    f, tmpname = mkstemp (".html", "userlist", root)
    f          = os.fdopen (f, "w")
    # all 'real' users
    users      = cl.filter ( None # full text search
                           , filterspec = {"status" : ['1']}
                           , sort       = ("+", "username")
                           )
    if users :
        options  = [OPTION_FMT % (id, cl.get (id, "username")) for id in users]

        f.write (USER_SINGLE % { "macro_name"  : "user"
                               , "option_list" : "\n".join (options)
                               }
                )
        f.write (USER_MULTI  % { "macro_name"  : "user_multi"
                               , "option_list" : "\n".join (options)
                               , "condition"   : "context [name].is_edit_ok ()"
                               }
                )
        f.write (USER_MULTI  % { "macro_name"  : "user_multi_read"
                               , "option_list" : "\n".join (options)
                               , "condition"   : "True"
                               }
                )

    # all users (incl. mail alias users)
    # RSC: now there are no mail alias users -- and we don't want
    # invalid users here, so use the same filterspec.
    users    = cl.filter ( None # full text search
                         , filterspec = {"status" : ['1']}
                         , sort       = ("+", "username")
                         )
    if users :
        options  = [OPTION_FMT % (id, cl.get (id, "username")) for id in users]

        f.write (USER_MULTI  % { "macro_name"  : "nosy_multi"
                               , "option_list" : "\n".join (options)
                               , "condition"   : "True"
                               }
                )

    f.close ()
    shutil.move (tmpname, pjoin (root, userlist))
# end def update_userlist_html

def check_retire (db, cl, nodeid, old_values) :
    pass
    #raise Reject, _ ("Not allowed to retire a user")
# end def check_retire

def init (db) :
    global _, common
    _   = get_translation \
        (db.config.TRACKER_LANGUAGE, db.config.TRACKER_HOME).gettext
    import common
    # fire before changes are made
    db.user.audit("set"   , audit_user_fields)
    db.user.audit("create", new_user)
    db.user.react("create", update_userlist_html)
    db.user.react("create", create_dynuser)
    db.user.react("set"   , update_userlist_html)
    db.user.audit("retire", check_retire)

# vim: set filetype=python ts=4 sw=4 et si
