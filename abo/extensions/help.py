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

_ = None

helptext = \
    { ""'abo'                 :
      ""'''Subscription to which this invoice belongs'''
    , ""'aboprice'            :
      ""'''Price and currency for this subscription'''
    , ""'abos'                :
      ""'''Subscriptions for this %(Classname)s'''
    , ""'abotype'             :
      ""'''Type of this subscription'''
    , ""'abo_type.adr_type'   :
      ""'''Type of Address -- this field indicates the address type to
           be used for marking addresses that should be exported for
           sending. When a new subsription is generated this type will
           be automatically added to the subscriber. When cancelling a
           subscription, this type will be deleted from the subscriber.
        '''
    , ""'activity'            :
      ""'''Date of last change'''
    , ""'actor'               :
      ""'''Person doing the last change'''
    , ""'address'             :
      ""'''Address for this letter'''
    , ""'user.address'        :
      ""'''Email address for this user'''
    , ""'adr_type'            :
      ""'''Type of Address'''
    , ""'alternate_addresses' :
      ""'''Alternate email addresses for this user, one per line'''
    , ""'amount'              :
      ""'''Amount this subscription costs'''
    , ""'author'              :
      ""'''Author of this message'''
    , ""'balance_open'        :
      ""'''Open amount not yet payed'''
    , ""'begin'               :
      ""'''Begin of period'''
    , ""'bookentry'           :
      ""'''Date when the payment was booked'''
    , ""'city'                :
      ""'''City where this person lives'''
    , ""'code'                :
      ""'''Code of this %(Classname)s'''
    , ""'confirm'                :
      ""'''Confirm the password here: first password and this entry
           must match.
        '''
    , ""'content'                :
      ""'''Content of this %(Classname)s'''
    , ""'country'             :
      ""'''Country for this address'''
    , ""'creation'            :
      ""'''Date of creation of this record'''
    , ""'creator'             :
      ""'''Person who created this record'''
    , ""'currency'            :
      ""'''Currency for this price'''
    , ""'date'                :
      ""'''Date when this %(Classname)s was sent'''
    , ""'date_payed'          :
      ""'''Date when this %(Classname)s was payed'''
    , ""'description'         :
      ""'''Verbose description of this %(Classname)s'''
    , ""'email'               :
      ""'''Email address for this %(Classname)s'''
    , ""'end'                 :
      ""'''Date when this subscription ends'''
    , ""'fax'                 :
      ""'''FAX number for this %(Classname)s'''
    , ""'files'               :
      ""'''Files for this %(Classname)s'''
    , ""'firstname'           :
      ""'''First name for this %(Classname)s'''
    , ""'function'            :
      ""'''Multiline field for this %(Classname)s, will be printed on an
           address label
        '''
    , ""'id'                  :
      ""'''ID of this record, automatically generated by the system.
           Cannot be changed by the user.
        '''
    , ""'initial'             :
      ""'''Initials of this %(Classname)s'''
    , ""'inreplyto'           :
      ""'''In Reply To field if this %(Classname)s was received by email'''
    , ""'interval'            :
      ""'''Interval for sending out an invoice in months. If the
           invoice_level is non-zero, the distance in months since the
           last invoice sent.
        '''
    , ""'invoice'             :
      ""'''Link to invoice for this %(Classname)s'''
    , ""'invoice_group'       :
      ""'''Link to invoice_group for this %(Classname)s'''
    , ""'invoice_level'       :
      ""'''When the customer has received more invoices than this number
           indicates, an invoice of this type is sent.
        '''
    , ""'invoice_no'          :
      ""'''Unique number for this invoice, generated by the system'''
    , ""'invoice_template'    :
      ""'''An OpenOffice file used as a template for this type of invoice'''
    , ""'invoices'            :
      ""'''List of invoices for this %(Classname)s'''
    , ""'klass'               :
      ""'''Class for this query'''
    , ""'last_sent'           :
      ""'''Date when an invoice was last sent'''
    , ""'lastname'            :
      ""'''Last name of this %(Classname)s'''
    , ""'letter'             :
      ""'''Download of letter -- usually this will open the letter in
           OpenOffice
        '''
    , ""'letters'             :
      ""'''List of letters for this %(Classname)s'''
    , ""'lettertitle'         :
      ""'''Title of this person used in a letter'''
    , ""'messageid'           :
      ""'''Message-ID if this message was received via email'''
    , ""'messages'            :
      ""'''List of messages for this %(Classname)s'''
    , ""'msg'            :
      ""'''Field for messages for %(Classname)s'''
    , ""'n_sent'              :
      ""'''Number of times this invoice was sent'''
    , ""'name'                :
      ""'''Unique name for this %(Classname)s'''
    , ""'nickname'            :
      ""'''Nickname (or short name) for this %(Classname)s'''
    , ""'open'                :
      ""'''Indicates if this invoice is still open. Automatically
           maintained by the system
        '''
    , ""'order'               :
      ""'''Items are ordered by this property in drop-down boxes etc.'''
    , ""'password'            :
      ""'''Password for this %(Classname)s'''
    , ""'payed_abos'          :
      ""'''Subscriptions for which this %(Classname)s is paying'''
    , ""'payer'               :
      ""'''Address which is paying for this subscription'''
    , ""'payment'             :
      ""'''Amount of payment received for this invoice'''
    , ""'period'              :
      ""'''Subscription period in months.'''
    , ""'period_end'          :
      ""'''Date when this invoice period ends'''
    , ""'period_start'        :
      ""'''Date when this invoice period starts'''
    , ""'phone'               :
      ""'''Phone number(s) '''
    , ""'postalcode'          :
      ""'''Postal code for this %(Classname)s '''
    , ""'private_for'         :
      ""'''Flag if this is a private %(Classname)s'''
    , ""'queries'             :
      ""'''Queries for this %(Classname)s'''
    , ""'realname'            :
      ""'''Real name for this %(Classname)s'''
    , ""'receipt_no'          :
      ""'''Unique identification of this payment'''
    , ""'recipients'          :
      ""'''Only set if message was received via email.'''
    , ""'roles'               :
      ""'''Roles for this %(Classname)s'''
    , ""'salutation'          :
      ""'''Salutation used for printing an address'''
    , ""'send_it'             :
      ""'''Flag indicating if this invoice should be sent. If not set,
           this invoice will disappear from the current list of invoices. It
           is not sent when generating invoices and is not marked when sent
           invoices are marked.
        '''
    , ""'street'              :
      ""'''Street for this %(Classname)s'''
    , ""'subject'             :
      ""'''Short identification of this message'''
    , ""'subscriber'          :
      ""'''Subscriber of this subscription'''
    , ""'summary'             :
      ""'''Short summary of this message (usually first line)'''
    , ""'timezone'            :
      ""'''Time zone of this %(Classname)s'''
    , ""'title'               :
      ""'''Title of the person belonging to this %(Classname)s'''
    , ""'tmplate'             :
      ""'''Used for writing letters (and invoices if selected as an
           invoice template)
        '''
    , ""'type'                :
      ""'''Mime type of this file'''
    , ""'typecat'             :
      ""'''Category of this %(Classname)s'''
    , ""'url'                 :
      ""'''Web-Link for this %(Classname)s'''
    , ""'username'            :
      ""'''Login-name'''
    , ""'valid'               :
      ""'''Status of this address'''
    }

def combined_name (cls, attr) :
    pname = '%s.%s' % (cls, attr)
    if pname in helptext :
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
    if klass.classname == 'letter' :
        p.append ('letter')
    if klass.classname == 'user' :
        p.append ('confirm')
    for i in properties.iterkeys () :
        pname = combined_name (klass.classname, i)
        if pname in helptext :
            p.append (pname)
    p = [(_ (i).decode ('utf-8'), i) for i in p]
    p.sort ()
    return [i [1] for i in p]
# end def help_properties

def fieldname (cls, name, fieldname = None) :
    if not fieldname : fieldname = name
    prop = combined_name (cls, fieldname)
    if not prop in helptext :
        return "%s&nbsp;" % _ (prop)
    return "<a href=\"javascript:help_window" \
           "('%s?:template=property_help#%s', '500', '400')\">" \
           "%s&nbsp; </a>" \
           % (cls, prop, _ (prop))

# end def fieldname

def init (instance) :
    global _
    _   = get_translation \
        (instance.config.TRACKER_LANGUAGE, instance.tracker_home).gettext
    instance.registerUtil ('helptext',        helptext)
    instance.registerUtil ('help_properties', help_properties)
    instance.registerUtil ('fieldname',       fieldname)
# end def init
