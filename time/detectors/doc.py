# -*- coding: iso-8859-1 -*-
# Copyright (C) 2007 Philipp Gortan <gortan@tttech.com>
# Copyright (C) 2009 Dr. Ralf Schlatterbeck Open Source Consulting.
# Reichergasse 131, A-3411 Weidling.
# Web: http://www.runtux.com Email: office@runtux.com
# All rights reserved
# ****************************************************************************
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301 USA
# ****************************************************************************
#
#++
# Name
#    doc
#
# Purpose
#    Detectors for document class
#--

from   roundup.exceptions             import Reject
from   roundup.cgi.TranslationService import get_translation
import common
import re

name_txt  = "[0-9a-zA-Z/]+"
ref_txt   = "[-0-9a-zA-Z/]+" # allow '-' for reference name
ref_re    = re.compile ("^%s$" % ref_txt)
name_re   = re.compile ("^%s$" % name_txt)
doc_nr_re = re.compile ("^(%s-)+? (?P<suffix> [0-9]+ )$" % name_txt, re.X)

def check_document_required (db, cl, nodeid, newvalues) :
    req = ['product_type', 'reference', 'artefact', 'department', 'title']
    if nodeid :
        req.append ('document_nr')
        req.append ('responsible')
    common.require_attributes (_, cl, nodeid, newvalues, * req)
# end def check_document_required

def check_document_frozen (db, cl, nodeid, newvalues) :
    if common.user_has_role (db, db.getuid (), 'Doc_Admin') :
        return

    if nodeid :
        attr_lst = ('product_type', 'reference', 'artefact', 'department')
        action   = _ ('modify')
    else :
        attr_lst = ('document_nr',)
        action   = _ ('specify')

    attrs = ", ".join (_ (a) for a in attr_lst if a in newvalues)
    if attrs :
        raise Reject, _ \
            ('You are not allowed to %(action)s: %(attrs)s'
            % locals ()
            )
# end def check_document_frozen

def check_document_nr (db, cl, nodeid, newvalues) :
    """Check or calculate document number."""
    doc_nr = newvalues.get ('document_nr')
    if doc_nr :
        if not doc_nr_re.match (doc_nr) :
            raise Reject (_ ('Document number is not valid: "%s"') % doc_nr)
    elif not nodeid :
        ### Creation where no `document_nr` is given
        dept_doc_num = db.department.get (newvalues ['department'], 'doc_num')
        prefix  = "-".join \
            ( ( db.product_type.get (newvalues ['product_type'], 'name')
              , db.reference.get    (newvalues ['reference']   , 'name')
              , db.artefact.get     (newvalues ['artefact']    , 'name')
              , _dept_doc_nr (db, cl, nodeid, newvalues)
              , "" # for the trailing dash
              )
            )
        next_nr                   = _next_document_nr (db, cl, prefix)
        newvalues ['document_nr'] = "%s%03d" % (prefix, next_nr)
# end def check_document_nr

def _check_for_description (db, cl, nodeid, newvalues) :
    """Checks that `description` is given and unique."""
    common.require_attributes (_, cl, nodeid, newvalues, 'description')
    if 'description' in newvalues :
        desc = newvalues ['description']
        common.check_unique (_, cl, nodeid, description = desc)
# end def _check_for_description

check_product_type = _check_for_description
check_reference    = _check_for_description

def defaults (db, cl, nodeid, newvalues) :
    if not newvalues.get ('responsible', None) :
        newvalues ['responsible'] = db.getuid ()
    # new doc item: always set status to work in progress
    newvalues ['status'] = db.doc_status.lookup ('work in progress')
    newvalues ['state_changed_by'] = db.getuid ()
# end def defaults

def _dept_doc_nr (db, cl, nodeid, newvalues) :
    """Return the selected department's `doc_num`, or reject, if it is not set.
    """
    res = db.department.get (newvalues ['department'], 'doc_num')
    if not res :
        raise Reject, _ ('Selected department has no document number')
    return res
# end def _dept_doc_nr

def _next_document_nr (db, cl, prefix) :
    filterspec = dict (document_nr = prefix)
    res = db.doc.filter (None, filterspec, sort = ('-', 'document_nr'))
    if res :
        doc_nr = cl.get (res [0], "document_nr")
        nr     = int (doc_nr_re.match (doc_nr).group ("suffix"), 10)
        return nr + 1
    else :
        return 1
# end def _next_document_nr

def check_name \
    (db, cl, nodeid, newvalues, name = 'name', regex = name_re, txt = name_txt) :
    if name not in newvalues or not newvalues [name] :
        return
    if not regex.match (newvalues [name]) :
        raise Reject, _ ('Malformed %s: Only %s allowed') % (_ (name), txt)
# end def check_name

def check_department (db, cl, nodeid, newvalues) :
    return check_name (db, cl, nodeid, newvalues, name = 'doc_num')
# end def check_department

def check_reference (db, cl, nodeid, newvalues) :
    return check_name (db, cl, nodeid, newvalues, regex = ref_re, txt = ref_txt)
# end def check_reference

def check_statechange (db, cl, nodeid, newvalues) :
    """ Things to do for a state change:
        Add doc admins to nosy for certain state changes
        State-change to released by different person that last
        state-change
    """
    if 'status' not in newvalues :
        return
    oldstate = cl.get (nodeid, 'status')
    newstate = newvalues ['status']
    wip = db.doc_status.lookup ('work in progress')
    if newstate != oldstate and oldstate != wip :
        nosy = newvalues.get ('nosy', cl.get (nodeid, 'nosy'))
        if not nosy :
            nosy = [db.getuid ()]
        nosy = dict.fromkeys (nosy)
        for u in db.user.getnodeids () :
            if common.user_has_role (db, u, 'Doc_Admin') :
                nosy [u] = True
        newvalues ['nosy'] = nosy.keys ()
        if newstate == db.doc_status.lookup ('released') :
            if db.getuid () == cl.get (nodeid, 'state_changed_by') :
                raise Reject, _ \
                    ('Change to "released": user must be different from'
                     ' change to "draft"'
                    )
    if newstate != oldstate :
        newvalues ['state_changed_by'] = db.getuid ()
# end def check_statechange

def init (db) :
    if 'doc' not in db.classes :
        return
    global _
    _   = get_translation \
        (db.config.TRACKER_LANGUAGE, db.config.TRACKER_HOME).gettext

    for action in ('create', 'set') :
        db.doc.audit          (action, check_document_required, priority = 110)
        db.doc.audit          (action, check_document_frozen,   priority = 120)
        db.doc.audit          (action, check_document_nr,       priority = 130)
        db.product_type.audit (action, check_product_type)
        db.reference.audit    (action, check_reference)
        for cl in (db.product_type, db.artefact) :
            cl.audit          (action, check_name)
        db.reference.audit    (action, check_reference)
        db.department.audit   (action, check_department)

    db.doc.audit ('create', defaults, 140)
    db.doc.audit ('set',    check_statechange)

### __END__ doc
