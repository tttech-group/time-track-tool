from roundup import date

def import_data_14 (db, user, dep, olo) :
     otp = None
     ud = db.user_dynamic.create \
         ( hours_fri          = 7.5
         , hours_sun          = 0.0
         , hours_wed          = 7.75
         , daily_worktime     = 0.0
         , vacation_yearly    = 25.0
         , all_in             = 1
         , booking_allowed    = 1
         , durations_allowed  = 0
         , hours_tue          = 7.75
         , weekend_allowed    = 0
         , hours_mon          = 7.75
         , hours_thu          = 7.75
         , vacation_day       = 1.0
         , valid_from         = date.Date ("2015-01-01")
         , weekly_hours       = 38.5
         , travel_full        = 0
         , vacation_month     = 1.0
         , hours_sat          = 0.0
         , department         = dep
         , org_location       = olo
         , overtime_period    = otp
         , user               = user
         , max_flexitime      = 5
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-02-02')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , duration      = 7.75
         , work_location = '5'
         , wp            = '44'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-02-03')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , duration      = 7.75
         , work_location = '5'
         , wp            = '44'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-02-04')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , duration      = 7.75
         , work_location = '5'
         , wp            = '44'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-02-05')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , duration      = 7.75
         , work_location = '5'
         , wp            = '44'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-02-06')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , duration      = 7.5
         , work_location = '5'
         , wp            = '44'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-05-26')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , duration      = 7.75
         , work_location = '5'
         , wp            = '44'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-01-02')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , duration      = 7.5
         , work_location = '5'
         , wp            = '44'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-01-03')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-01-04')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-01-05')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , duration      = 7.75
         , work_location = '5'
         , wp            = '44'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-08-07')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-08-08')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-08-09')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-08-10')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-08-11')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-08-12')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-08-13')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-08-14')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-08-15')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-08-16')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-08-17')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-08-18')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-08-19')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-08-20')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-08-21')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-01-01')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , duration      = 7.75
         , work_location = '5'
         , wp            = '1'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-01-06')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , duration      = 7.75
         , work_location = '5'
         , wp            = '1'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-01-07')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '17:00'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:15'
         , end           = '12:00'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-01-08')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '17:00'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:15'
         , end           = '12:00'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-01-09')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '14:30'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:00'
         , end           = '12:00'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-01-10')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-01-11')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-01-12')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '17:00'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:00'
         , end           = '12:00'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-01-13')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '17:15'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:15'
         , end           = '12:00'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-01-14')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '17:30'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '07:30'
         , end           = '12:00'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '18:30'
         , end           = '21:00'
         , time_activity = '1'
         , work_location = '6'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-01-15')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '16:30'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:00'
         , end           = '12:00'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-01-16')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '16:30'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:00'
         , end           = '12:00'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-01-17')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-01-18')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-01-23')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , duration      = 7.5
         , work_location = '5'
         , wp            = '44'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-01-19')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '17:00'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:00'
         , end           = '12:00'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-01-20')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '16:30'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:15'
         , end           = '12:00'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-01-21')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '17:00'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '09:00'
         , end           = '12:00'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-01-22')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '18:00'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:30'
         , end           = '12:00'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-01-24')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-01-25')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-01-26')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '17:00'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:15'
         , end           = '12:00'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-01-27')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '07:30'
         , end           = '08:30'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '18:00'
         , work_location = '1'
         , wp            = '5'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:30'
         , end           = '12:00'
         , work_location = '1'
         , wp            = '5'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-01-28')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '07:30'
         , end           = '08:30'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '17:00'
         , work_location = '1'
         , wp            = '5'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:30'
         , end           = '12:00'
         , work_location = '1'
         , wp            = '5'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-01-29')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '18:00'
         , work_location = '1'
         , wp            = '6'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:00'
         , end           = '12:00'
         , work_location = '1'
         , wp            = '6'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-01-30')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:00'
         , end           = '14:00'
         , work_location = '1'
         , wp            = '6'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-01-31')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-02-01')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-02-09')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '17:30'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:00'
         , end           = '12:00'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-02-10')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '17:30'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:15'
         , end           = '12:00'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-02-11')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '07:15'
         , end           = '12:00'
         , time_activity = '1'
         , work_location = '6'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '13:30'
         , time_activity = '10'
         , work_location = '3'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '13:30'
         , end           = '16:00'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-02-12')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:45'
         , end           = '17:00'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:15'
         , end           = '12:15'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-02-13')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:00'
         , end           = '12:00'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '14:15'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-02-14')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-02-15')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-02-07')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-02-08')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-02-16')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '17:30'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:00'
         , end           = '12:00'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-02-17')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '17:30'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:00'
         , end           = '12:00'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-02-18')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '17:00'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:00'
         , end           = '12:00'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-02-19')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '16:15'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:00'
         , end           = '12:00'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-02-20')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:15'
         , end           = '12:00'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '14:00'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-02-21')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-02-22')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-02-23')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '17:00'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:00'
         , end           = '12:00'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-02-24')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '06:30'
         , end           = '11:30'
         , time_activity = '1'
         , work_location = '3'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '18:30'
         , time_activity = '1'
         , work_location = '6'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '11:30'
         , end           = '12:00'
         , time_activity = '1'
         , work_location = '6'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-02-25')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '18:00'
         , time_activity = '1'
         , work_location = '6'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:30'
         , end           = '12:00'
         , time_activity = '1'
         , work_location = '6'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '18:30'
         , end           = '23:45'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-02-26')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '17:00'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:15'
         , end           = '12:00'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-02-27')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '15:00'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:15'
         , end           = '12:00'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-02-28')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-03-01')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-03-02')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '17:30'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:15'
         , end           = '12:00'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-03-03')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:00'
         , end           = '12:00'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '13:30'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '13:30'
         , end           = '14:00'
         , time_activity = '10'
         , work_location = '3'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '14:00'
         , end           = '17:00'
         , time_activity = '1'
         , work_location = '6'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-03-04')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '18:00'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:15'
         , end           = '12:00'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-03-05')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '17:00'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:30'
         , end           = '12:00'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-03-06')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:00'
         , end           = '12:00'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '14:00'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-03-07')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-03-08')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-03-09')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '16:00'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:15'
         , end           = '12:00'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-03-10')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '17:00'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:15'
         , end           = '12:00'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '17:45'
         , end           = '20:00'
         , time_activity = '1'
         , work_location = '6'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-03-11')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '05:00'
         , end           = '10:00'
         , time_activity = '11'
         , work_location = '3'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '17:00'
         , time_activity = '1'
         , work_location = '6'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '17:30'
         , end           = '23:30'
         , time_activity = '11'
         , work_location = '3'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '10:30'
         , end           = '12:00'
         , time_activity = '1'
         , work_location = '6'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-03-12')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '17:00'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:15'
         , end           = '12:00'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-03-13')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:15'
         , end           = '14:00'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-03-14')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-03-15')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-03-16')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '17:30'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:00'
         , end           = '12:00'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-03-17')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '16:00'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:00'
         , end           = '12:00'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-03-18')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '17:30'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '07:30'
         , end           = '12:00'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-03-19')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '17:00'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:00'
         , end           = '12:00'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-03-20')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '10:45'
         , end           = '12:00'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '14:15'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-03-21')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-03-22')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-03-23')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '17:30'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:00'
         , end           = '12:00'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-03-24')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '17:30'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:00'
         , end           = '12:00'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-03-25')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '18:30'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:15'
         , end           = '12:00'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '19:00'
         , end           = '19:30'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-03-26')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '18:30'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:15'
         , end           = '12:00'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-03-27')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '11:30'
         , end           = '14:30'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-03-28')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-03-29')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-03-30')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '13:30'
         , end           = '19:30'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:30'
         , end           = '13:00'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-03-31')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '16:00'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:30'
         , end           = '12:00'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '18:00'
         , end           = '19:00'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-04-01')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '04:30'
         , end           = '07:45'
         , time_activity = '10'
         , work_location = '3'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '07:45'
         , end           = '13:00'
         , time_activity = '1'
         , work_location = '6'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '13:30'
         , end           = '17:30'
         , time_activity = '1'
         , work_location = '6'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '17:30'
         , end           = '23:45'
         , time_activity = '10'
         , work_location = '3'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-04-02')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '16:00'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:30'
         , end           = '12:00'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-04-03')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:30'
         , end           = '13:30'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-04-04')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-04-05')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-04-07')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , duration      = 7.75
         , work_location = '5'
         , wp            = '44'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-04-06')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , duration      = 7.75
         , work_location = '5'
         , wp            = '1'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-04-08')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '17:00'
         , work_location = '1'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:00'
         , end           = '12:00'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-04-09')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:00'
         , end           = '12:00'
         , time_activity = '1'
         , work_location = '6'
         , wp            = '4'
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '12:30'
         , end           = '17:00'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-04-10')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.time_record.create \
         ( daily_record  = dr
         , start         = '08:00'
         , end           = '14:00'
         , work_location = '1'
         , wp            = '4'
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-04-11')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     dr = db.daily_record.create \
         ( user = user
         , date = date.Date ('2015-04-12')
         , weekend_allowed   = 0
         , required_overtime = 0
         )
     db.user_dynamic.set (ud, valid_to = date.Date ("2015-06-01"))
     db.commit ()
# end def import_data_14
