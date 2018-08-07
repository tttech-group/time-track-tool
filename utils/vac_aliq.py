#!/usr/bin/python
import sys
import os
from roundup           import date
from roundup           import instance
from argparse          import ArgumentParser
from csv               import DictReader

class Vacation_Setup (object) :

    def __init__ (self, db, args) :
        self.db        = db
        self.args      = args
        self.vaold     = '1'
        self.vanew     = '2'
	self.startdate = date.Date (self.args.startdate)
        self.freez     = {}
    # end def __init__

    def create_vac_aliq (self) :
        for n in 'Daily', 'Monthly' :
            try :
                self.db.vac_aliq.lookup (n)
            except KeyError :
                self.db.vac_aliq.create (name = n)
        self.db.commit ()
    # end def create_vac_aliq

    def fix_olos (self) :
        """ Loop over all org_locations and set vac_aliq if unset and
            do_leave_process is set. Also set the olos from above.
        """

        db = self.db
        for id in db.org_location.getnodeids (retired = False) :
            olo = db.org_location.getnode (id)
            if id in self.args.org_location :
                if not olo.vacation_yearly :
                    db.org_location.set \
                        (id, vacation_yearly = self.args.yearly_vacation)
            if olo.vac_aliq is not None :
                continue
            if id in self.args.org_location :
                db.org_location.set \
                    (id, do_leave_process = True, vac_aliq = self.vanew)
            elif olo.do_leave_process :
                db.org_location.set (id, vac_aliq = self.vaold)
        db.commit ()
    # end def fix_olos

    def fix_old_dynuser_recs (self) :
        """ Loop over all existing absolute vacation corrections and
            set vac_aliq in respective user_dynamic records
        """
        db  = self.db
        flt = db.vacation_correction.filter
        for id in flt (None, dict (absolute = True)) :
            vc  = db.vacation_correction.getnode (id)
            dyn = user_dynamic.first_user_dynamic (db, vc.user, date = vc.date)
            if not dyn :
                print "WARN: No dyn user %s/%s" % (vc.user, vc.date)
            while dyn :
                if dyn.vac_aliq is None :
                    db.user_dynamic.set (dyn.id, vac_aliq = self.vaold)
                dyn = user_dynamic.next_user_dynamic (db, dyn)

        db.commit ()
    # end def fix_old_dynuser_recs

    def modify_users (self) :
        """ Read file as CSV and modify users """
        db = self.db
        with open (self.args.vacfile, 'r') as f :
            dr = DictReader (f, delimiter = self.args.delimiter)
            for line in dr :
                cs = self.args.charset
                uk = 'timetracker kennung'
                vk = 'noch offene Urlaubstage 2017'
                username = line [uk].decode (cs).encode ('utf-8')
                days     = line [vk].decode (cs).encode ('utf-8')
                if not username :
                    continue
                assert days, "Days is empty for %s" % username
                days = float (days)
                uid  = db.user.lookup (username)
                user = db.user.getnode (uid)
                dyn  = user_dynamic.first_user_dynamic \
                    (db, uid, date = self.startdate)
                assert dyn
                self.thaw (uid)
                # Need to create new dyn if valid_from is < startdate
                if dyn.valid_from < self.startdate :
                    d = dict \
                        ((k, dyn [k]) for k in db.user_dynamic.properties
                        if dyn [k] is not None
                        )
                    d ['valid_from']      = self.startdate
                    d ['vacation_yearly'] = self.args.yearly_vacation
                    d ['vac_aliq']        = self.vanew
                    vd = d.get ('vacation_day') 
                    vm = d.get ('vacation_month')
                    if not vd or not vm :
                        d ['vacation_month'] = d ['vacation_day'] = 1
                    # If dyn.valid_to is None, valid_to is set for the
                    # existing record, we need to set explicitly if
                    # non-empty.
                    if dyn.valid_to :
                        db.user_dynamic.set \
                            (dyn.id, valid_to = self.startdate)
                    print ("Creating user_dynamic: %s %s-%s" % \
                        (username, d ['valid_from'], d.get ('valid_to')))
                    dyn = db.user_dynamic.create (**d)
                    dyn = user_dynamic.next_user_dynamic (db, dyn)
                while dyn :
                    d = {}
                    if dyn.vacation_yearly != self.args.yearly_vacation :
                        d ['vacation_yearly'] = self.args.yearly_vacation
                    if dyn.vac_aliq != self.vanew :
                        d ['vac_aliq'] = self.vanew
                    if not dyn.vacation_month or not dyn.vacation_day :
                        d ['vacation_month'] = d ['vacation_day'] = 1
                    if d :
                        print "Modify: %s/user_dynamic%s" % (username, dyn.id)
                        db.user_dynamic.set (dyn.id, **d)
                    dyn = user_dynamic.next_user_dynamic (db, dyn)
                vc = vacation.get_vacation_correction \
                    (db, uid, date = self.startdate)
                if not vc or vc.date < self.startdate :
                    print ("Creating vacation correction for %s" % username)
                    db.vacation_correction.create \
                        ( absolute = True
                        , user     = uid
                        , date     = self.startdate
                        , days     = days
                        )
                self.freeze (uid)
        db.commit ()
    # end def modify_users

    def thaw (self, uid) :
        db  = self.db
        props = \
            ( 'date'
            , 'achieved_hours'
            , 'balance'
            , 'month_balance'
            , 'week_balance'
            )
        d   = dict \
            ( user   = uid
            , date   = '%s;' % self.startdate.pretty ('%Y-%m-%d')
            , frozen = True
            )
        frs = db.daily_record_freeze.filter (None, d, ('-', 'date'))
        assert uid not in self.freez
        self.freez [uid] = {}
        for frid in frs :
            fr = db.daily_record_freeze.getnode (frid)
            self.freez [uid][frid] = dict ((p, fr [p]) for p in props)
            self.db.daily_record_freeze.set (frid, frozen = False)
    # end def thaw

    def freeze (self, uid) :
        srt = lambda x : self.freez [uid][x]['date']
        for frid in sorted (self.freez [uid], key = srt) :
            self.db.daily_record_freeze.set (frid, frozen = True)
            fr = self.db.daily_record_freeze.getnode (frid)
            for k in self.freez [uid][frid] :
                uf = self.freez [uid][frid][k]
                if uf != fr [k] :
                    print "DIFFER: %s %s %s" % (k, uf, fr [k])
    # end def freeze

# end class Vacation_Setup


def main () :
    olos = ['4', '5', '6', '35']
    cmd = ArgumentParser ()
    cmd.add_argument \
        ( 'vacfile'
        , help   = 'vacation file'
        )
    cmd.add_argument \
        ( "-C", "--charset"
        , help    = "Character set of vacation file, default: %(default)s"
        , default = 'utf-8'
        )
    cmd.add_argument \
        ( "-D", "--delimiter"
        , help    = "CSV Delimiter, default: %(default)s"
        , default = ';'
        )
    cmd.add_argument \
        ( "-d", "--dir"
        , help    = "Directory of roundup tracker, default: %(default)s"
        , default = os.getcwd ()
        )
    cmd.add_argument \
        ( "-s", "--startdate"
        , help    = "Start date of vacation for given Org/Location, "
                    "default: %(default)s"
        , default = '2018-01-01'
        )
    cmd.add_argument \
        ( "-o", "--org-location"
        , help    = "Org/Location(s) to change, default: %s" % ','.join (olos)
        , action  = 'append'
        )
    cmd.add_argument \
        ( "-y", "--yearly-vacation"
        , help    = "Yearly vac. for users and Org/Loc, default: %(default)s"
        , default = 30
        , type    = int
        )
    args = cmd.parse_args ()
    if not args.org_location :
        args.org_location = olos

    tracker = instance.open (args.dir)
    db      = tracker.open ('admin')

    sys.path.insert (1, os.path.join (args.dir, 'lib'))
    global user_dynamic
    import user_dynamic
    global vacation
    import vacation

    vs = Vacation_Setup (db, args)
    vs.create_vac_aliq ()
    vs.fix_olos ()
    vs.fix_old_dynuser_recs ()
    vs.modify_users ()
# end def main

if __name__ == '__main__' :
    main ()
