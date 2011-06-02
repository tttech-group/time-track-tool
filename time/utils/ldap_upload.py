#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import sys
import os

from optparse         import OptionParser
from roundup          import instance

def main () :
    # most ldap info is now fetched from extensions/config.ini
    parser  = OptionParser ()
    parser.add_option \
        ( "-d", "--database-directory"
        , dest    = "database_directory"
        , help    = "Directory of the roundup installation"
        , default = '.'
        )
    parser.add_option \
        ( "-u", "--update"
        , help    = "Update the LDAP directory with info from roundup"
        , default = False
        , action  = 'store_true'
        )
    opt, args = parser.parse_args ()
    if len (args) :
        parser.error ('No arguments please')
        exit (23)

    sys.path.insert (1, os.path.join (opt.database_directory, 'extensions'))
    from ldap_rup_sync import LDAP_Roundup_Sync
    tracker = instance.open (opt.database_directory)
    db      = tracker.open ('admin')

    lds = LDAP_Roundup_Sync (db)
    lds.sync_all_users_to_ldap (update = opt.update)
# end def main


if __name__ == '__main__' :
    main ()
