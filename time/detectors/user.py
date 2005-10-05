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
_ = lambda x : x

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
 <tal:block tal:condition="python:not context [name].is_%(permission)s_ok ()"
  tal:replace="python: context [name]"/>
 <select multiple tal:condition="python: context [name].is_%(permission)s_ok ()"
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

def audit_user_fields(db, cl, nodeid, new_values):
    ''' Make sure user properties are valid.
        - email address has no spaces in it
        - roles specified exist

        TODO:
        - email address matches TTTspec (and optionally auto-generate)
          - firstname.lastname@tttech.com
          - lastname@tttech.com
          - (fla@tttech.com) # not implemented


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
    if (new_values.has_key ("firstname") \
        or new_values.has_key ("lastname")) \
        and nodeid :
        fn = new_values.get ("firstname", cl.get (nodeid, "firstname"))
        ln = new_values.get ("lastname" , cl.get (nodeid, "lastname" ))
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
                               , "permission"  : "edit"
                               }
                )
        f.write (USER_MULTI  % { "macro_name"  : "user_multi_read"
                               , "option_list" : "\n".join (options)
                               , "permission"  : "view"
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
                               , "permission"  : "view"
                               }
                )

    f.close ()
    shutil.move (tmpname, pjoin (root, userlist))
# end def update_userlist_html

def check_retire (db, cl, nodeid, old_values) :
    raise Reject, _ ("Not allowed to retire a user")
# end def check_retire

def init (db) :
    global _
    _   = get_translation \
        (db.config.TRACKER_LANGUAGE, db.config.TRACKER_HOME).gettext
    # fire before changes are made
    db.user.audit("set"   , audit_user_fields)
    db.user.audit("create", audit_user_fields)
    db.user.react("create", update_userlist_html)
    db.user.react("set"   , update_userlist_html)
    db.user.audit("retire", check_retire)

# vim: set filetype=python ts=4 sw=4 et si
