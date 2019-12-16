security = """
New Web users get the Roles "User,Nosy"
New Email users get the Role "User"
Role "admin":
 User may access the rest interface (Rest Access)
 User may access the web interface (Web Access)
 User may access the xmlrpc interface (Xmlrpc Access)
 User may create everything (Create)
 User may edit everything (Edit)
 User may manipulate user Roles through the web (Web Roles)
 User may restore everything (Restore)
 User may retire everything (Retire)
 User may use the email interface (Email Access)
 User may view everything (View)
Role "anonymous":
 User may access the web interface (Web Access)
Role "controlling":
 User is allowed Edit on (Edit for "daily_record": ('status', 'time_record') only)
 User is allowed Edit on (Edit for "time_wp": ('project',) only)
 User is allowed View on (View for "user": ('roles',) only)
 User is allowed View on (View for "user_dynamic": ('id', 'sap_cc', 'user', 'valid_from', 'valid_to') only)
 User is allowed to access contract_type (View for "contract_type" only)
 User is allowed to access daily_record (View for "daily_record" only)
 User is allowed to access daily_record_freeze (View for "daily_record_freeze" only)
 User is allowed to access leave_submission (View for "leave_submission" only)
 User is allowed to access overtime_correction (View for "overtime_correction" only)
 User is allowed to access query (View for "query" only)
 User is allowed to access time_project (View for "time_project" only)
 User is allowed to access time_record (View for "time_record" only)
 User is allowed to access time_report (View for "time_report" only)
 User is allowed to access time_wp (View for "time_wp" only)
 User is allowed to access vacation_correction (View for "vacation_correction" only)
 User is allowed to create cost_center (Create for "cost_center" only)
 User is allowed to create cost_center_group (Create for "cost_center_group" only)
 User is allowed to create cost_center_status (Create for "cost_center_status" only)
 User is allowed to create department (Create for "department" only)
 User is allowed to create organisation (Create for "organisation" only)
 User is allowed to create product_family (Create for "product_family" only)
 User is allowed to create project_type (Create for "project_type" only)
 User is allowed to create public_holiday (Create for "public_holiday" only)
 User is allowed to create query (Create for "query" only)
 User is allowed to create reporting_group (Create for "reporting_group" only)
 User is allowed to create sap_cc (Create for "sap_cc" only)
 User is allowed to create time_activity (Create for "time_activity" only)
 User is allowed to create time_record (Create for "time_record" only)
 User is allowed to create work_location (Create for "work_location" only)
 User is allowed to edit cost_center (Edit for "cost_center" only)
 User is allowed to edit cost_center_group (Edit for "cost_center_group" only)
 User is allowed to edit cost_center_status (Edit for "cost_center_status" only)
 User is allowed to edit department (Edit for "department" only)
 User is allowed to edit organisation (Edit for "organisation" only)
 User is allowed to edit product_family (Edit for "product_family" only)
 User is allowed to edit project_type (Edit for "project_type" only)
 User is allowed to edit public_holiday (Edit for "public_holiday" only)
 User is allowed to edit query (Edit for "query" only)
 User is allowed to edit reporting_group (Edit for "reporting_group" only)
 User is allowed to edit sap_cc (Edit for "sap_cc" only)
 User is allowed to edit time_activity (Edit for "time_activity" only)
 User is allowed to edit time_record (Edit for "time_record" only)
 User is allowed to edit work_location (Edit for "work_location" only)
Role "doc_admin":
 User is allowed Edit on (Edit for "department": ('doc_num',) only)
 User is allowed to create artefact (Create for "artefact" only)
 User is allowed to create doc (Create for "doc" only)
 User is allowed to create doc_status (Create for "doc_status" only)
 User is allowed to create product_type (Create for "product_type" only)
 User is allowed to create reference (Create for "reference" only)
 User is allowed to edit artefact (Edit for "artefact" only)
 User is allowed to edit doc (Edit for "doc" only)
 User is allowed to edit doc_status (Edit for "doc_status" only)
 User is allowed to edit product_type (Edit for "product_type" only)
 User is allowed to edit reference (Edit for "reference" only)
Role "dom-user-edit-facility":
 User is allowed Edit on (Edit for "user": ['room'] only)
Role "dom-user-edit-gtt":
 User is allowed Edit on (Edit for "user": ['contacts', 'csv_delimiter', 'firstname', 'hide_message_files', 'job_description', 'lastname', 'lunch_duration', 'lunch_start', 'nickname', 'pictures', 'position', 'room', 'sex', 'status', 'subst_active', 'substitute', 'supervisor', 'timezone', 'title', 'tt_lines', 'username'] only)
 User is allowed to create user (Create for "user" only)
 User is allowed to create user_contact (Create for "user_contact" only)
 User is allowed to create user_dynamic (Create for "user_dynamic" only)
 User is allowed to edit user_contact (Edit for "user_contact" only)
 User is allowed to edit user_dynamic (Edit for "user_dynamic" only)
Role "dom-user-edit-hr":
 User is allowed Edit on (Edit for "user": ['clearance_by', 'contacts', 'csv_delimiter', 'firstname', 'hide_message_files', 'job_description', 'lastname', 'lunch_duration', 'lunch_start', 'nickname', 'pictures', 'position', 'roles', 'room', 'sex', 'status', 'subst_active', 'substitute', 'supervisor', 'timezone', 'title', 'tt_lines'] only)
 User is allowed to create user_contact (Create for "user_contact" only)
 User is allowed to create user_dynamic (Create for "user_dynamic" only)
 User is allowed to edit user_contact (Edit for "user_contact" only)
 User is allowed to edit user_dynamic (Edit for "user_dynamic" only)
Role "dom-user-edit-office":
 User is allowed Edit on (Edit for "user": ['contacts', 'position', 'room', 'title'] only)
 User is allowed to create user_contact (Create for "user_contact" only)
 User is allowed to edit user_contact (Edit for "user_contact" only)
Role "facility":
 User is allowed to create room (Create for "room" only)
 User is allowed to edit room (Edit for "room" only)
Role "hr":
  (Edit for "overtime_period": ('name', 'order') only)
 User is allowed Edit on (Edit for "daily_record": ('required_overtime', 'weekend_allowed') only)
 User is allowed Edit on (Edit for "daily_record": ('status', 'time_record') only)
 User is allowed Edit on (Edit for "time_project": ('approval_hr', 'approval_required', 'is_public_holiday', 'is_special_leave', 'is_vacation', 'no_overtime', 'no_overtime_day', 'overtime_reduction') only)
 User is allowed View on (View for "user": ('contacts',) only)
 User is allowed to access contract_type (View for "contract_type" only)
 User is allowed to access daily_record (View for "daily_record" only)
 User is allowed to access daily_record_freeze (View for "daily_record_freeze" only)
 User is allowed to access leave_submission (View for "leave_submission" only)
 User is allowed to access overtime_correction (View for "overtime_correction" only)
 User is allowed to access time_record (View for "time_record" only)
 User is allowed to access user_contact (View for "user_contact" only)
 User is allowed to access user_dynamic (View for "user_dynamic" only)
 User is allowed to access vacation_correction (View for "vacation_correction" only)
 User is allowed to create daily_record_freeze (Create for "daily_record_freeze" only)
 User is allowed to create location (Create for "location" only)
 User is allowed to create org_location (Create for "org_location" only)
 User is allowed to create organisation (Create for "organisation" only)
 User is allowed to create overtime_correction (Create for "overtime_correction" only)
 User is allowed to create overtime_period (Create for "overtime_period" only)
 User is allowed to create position (Create for "position" only)
 User is allowed to create product_family (Create for "product_family" only)
 User is allowed to create project_type (Create for "project_type" only)
 User is allowed to create public_holiday (Create for "public_holiday" only)
 User is allowed to create reporting_group (Create for "reporting_group" only)
 User is allowed to create room (Create for "room" only)
 User is allowed to create sap_cc (Create for "sap_cc" only)
 User is allowed to create time_record (Create for "time_record" only)
 User is allowed to create uc_type (Create for "uc_type" only)
 User is allowed to create user (Create for "user" only)
 User is allowed to create user_dynamic (Create for "user_dynamic" only)
 User is allowed to edit dynamic user data if not frozen in validity span of dynamic user record (Edit for "user_dynamic" only)
 User is allowed to edit freeze record if not frozen at the given date (Edit for "daily_record_freeze": ('frozen',) only)
 User is allowed to edit location (Edit for "location" only)
 User is allowed to edit org_location (Edit for "org_location" only)
 User is allowed to edit organisation (Edit for "organisation" only)
 User is allowed to edit overtime correction if the overtime correction is not frozen (Edit for "overtime_correction" only)
 User is allowed to edit position (Edit for "position" only)
 User is allowed to edit product_family (Edit for "product_family" only)
 User is allowed to edit project_type (Edit for "project_type" only)
 User is allowed to edit public_holiday (Edit for "public_holiday" only)
 User is allowed to edit reporting_group (Edit for "reporting_group" only)
 User is allowed to edit room (Edit for "room" only)
 User is allowed to edit sap_cc (Edit for "sap_cc" only)
 User is allowed to edit time_record (Edit for "time_record" only)
 User is allowed to edit uc_type (Edit for "uc_type" only)
 User may manipulate user Roles through the web (Web Roles)
Role "hr-leave-approval":
 User is allowed Edit on (Edit for "leave_submission": ('status',) only)
 User is allowed to access contract_type (View for "contract_type" only)
 User is allowed to access leave_submission (View for "leave_submission" only)
 User is allowed to access vacation_correction (View for "vacation_correction" only)
Role "hr-org-location":
  (Search for "daily_record_freeze" only)
  (Search for "overtime_correction" only)
  (Search for "time_record" only)
  (Search for "user_dynamic" only)
 User is allowed to view dynamic user data if he/she is in group HR-Org-Location and in the same Org-Location as the given user (View for "user_dynamic" only)
 User is allowed to view freeze information if he/she is in group HR-Org-Location and in the same Org-Location as the given user (View for "daily_record_freeze" only)
 User is allowed to view overtime information if he/she is in group HR-Org-Location and in the same Org-Location as the given user (View for "overtime_correction" only)
 User is allowed to view time record data if he/she is in group HR-Org-Location and in the same Org-Location as the given user (View for "time_record" only)
Role "hr-vacation":
 User is allowed to access contract_type (View for "contract_type" only)
 User is allowed to access leave_submission (View for "leave_submission" only)
 User is allowed to access vacation_correction (View for "vacation_correction" only)
 User is allowed to create contract_type (Create for "contract_type" only)
 User is allowed to create leave_submission (Create for "leave_submission" only)
 User is allowed to create vacation_correction (Create for "vacation_correction" only)
 User is allowed to edit contract_type (Edit for "contract_type" only)
 User is allowed to edit leave_submission (Edit for "leave_submission" only)
 User is allowed to edit vacation_correction (Edit for "vacation_correction" only)
Role "it":
 User is allowed Edit on (Edit for "user": ('ad_domain', 'nickname', 'password', 'pictures', 'roles', 'timetracking_by', 'timezone', 'username') only)
 User is allowed Edit on file if file is linked from an item with Edit permission (Edit for "file" only)
 User is allowed Edit on msg if msg is linked from an item with Edit permission (Edit for "msg" only)
 User is allowed View on file if file is linked from an item with View permission (View for "file" only)
 User is allowed to access domain_permission (View for "domain_permission" only)
 User is allowed to create domain_permission (Create for "domain_permission" only)
 User is allowed to edit domain_permission (Edit for "domain_permission" only)
 User may manipulate user Roles through the web (Web Roles)
Role "nosy":
 User may get nosy messages for doc (Nosy for "doc" only)
Role "office":
 User is allowed View on (View for "user": ('contacts',) only)
 User is allowed to access user_contact (View for "user_contact" only)
 User is allowed to create absence (Create for "absence" only)
 User is allowed to create absence_type (Create for "absence_type" only)
 User is allowed to create room (Create for "room" only)
 User is allowed to create uc_type (Create for "uc_type" only)
 User is allowed to edit absence (Edit for "absence" only)
 User is allowed to edit absence_type (Edit for "absence_type" only)
 User is allowed to edit room (Edit for "room" only)
 User is allowed to edit uc_type (Edit for "uc_type" only)
Role "pgp":
Role "procurement":
  (View for "sap_cc" only)
  (View for "time_project" only)
 User is allowed Edit on (Edit for "sap_cc": ('purchasing_agents',) only)
 User is allowed Edit on (Edit for "time_project": ('purchasing_agents',) only)
Role "project":
 User is allowed Edit on (Edit for "time_project": ('cost_center', 'department', 'deputy', 'description', 'name', 'nosy', 'organisation', 'responsible', 'status') only)
 User is allowed Edit on (Edit for "time_project": ('infosec_req', 'max_hours', 'op_project', 'planned_effort', 'product_family', 'project_type', 'reporting_group', 'work_location') only)
 User is allowed to access time_project (View for "time_project" only)
 User is allowed to access time_report (View for "time_report" only)
 User is allowed to access time_wp (View for "time_wp" only)
 User is allowed to create time_project (Create for "time_project" only)
 User is allowed to create time_project_status (Create for "time_project_status" only)
 User is allowed to create time_wp (Create for "time_wp" only)
 User is allowed to create time_wp_group (Create for "time_wp_group" only)
 User is allowed to edit time_project_status (Edit for "time_project_status" only)
 User is allowed to edit time_wp (Edit for "time_wp" only)
 User is allowed to edit time_wp_group (Edit for "time_wp_group" only)
Role "project_view":
 User is allowed to access time_project (View for "time_project" only)
 User is allowed to access time_report (View for "time_report" only)
 User is allowed to access time_wp (View for "time_wp" only)
Role "staff-report":
Role "summary_view":
Role "time-report":
 User is allowed to access time_report (View for "time_report" only)
 User is allowed to create time_report (Create for "time_report" only)
 User is allowed to edit time_report (Edit for "time_report" only)
 User may edit own file (file created by user) (Edit for "file" only)
Role "user":
  (Search for "time_project": ('activity', 'actor', 'cost_center', 'creation', 'creator', 'deputy', 'description', 'id', 'is_public_holiday', 'is_special_leave', 'is_vacation', 'name', 'op_project', 'organisation', 'overtime_reduction', 'product_family', 'project_type', 'reporting_group', 'responsible', 'status', 'work_location') only)
  (Search for "time_wp": ('activity', 'actor', 'bookers', 'cost_center', 'creation', 'creator', 'description', 'durations_allowed', 'epic_key', 'has_expiration_date', 'id', 'is_public', 'name', 'project', 'responsible', 'time_end', 'time_start', 'time_wp_summary_no', 'travel', 'wp_no') only)
 Search (Search for "user_contact" only)
 User is allowed Edit on file if file is linked from an item with Edit permission (Edit for "file" only)
 User is allowed View on (View for "user": ('activity', 'actor', 'ad_domain', 'address', 'alternate_addresses', 'clearance_by', 'creation', 'creator', 'department', 'firstname', 'job_description', 'lastname', 'id', 'lunch_duration', 'lunch_start', 'nickname', 'pictures', 'position', 'queries', 'realname', 'room', 'sex', 'status', 'subst_active', 'substitute', 'supervisor', 'timezone', 'title', 'username', 'tt_lines') only)
 User is allowed View on (View for "user": ('contacts',) only)
 User is allowed View on (View for "user": ('timetracking_by',) only)
 User is allowed View on (View for "user_dynamic": ('department', 'org_location') only)
 User is allowed View on file if file is linked from an item with View permission (View for "file" only)
 User is allowed View on msg if msg is linked from an item with View permission (View for "msg" only)
 User is allowed to access absence (View for "absence" only)
 User is allowed to access absence_type (View for "absence_type" only)
 User is allowed to access artefact (View for "artefact" only)
 User is allowed to access cost_center (View for "cost_center" only)
 User is allowed to access cost_center_group (View for "cost_center_group" only)
 User is allowed to access cost_center_status (View for "cost_center_status" only)
 User is allowed to access daily record if he is owner or supervisor or timetracking-by user (Edit for "daily_record": ('status', 'time_record') only)
 User is allowed to access daily record if he is owner or supervisor or timetracking-by user (View for "daily_record" only)
 User is allowed to access daily_record_status (View for "daily_record_status" only)
 User is allowed to access department (View for "department" only)
 User is allowed to access doc (View for "doc" only)
 User is allowed to access doc_status (View for "doc_status" only)
 User is allowed to access leave_status (View for "leave_status" only)
 User is allowed to access location (View for "location" only)
 User is allowed to access org_location (View for "org_location" only)
 User is allowed to access organisation (View for "organisation" only)
 User is allowed to access overtime_period (View for "overtime_period" only)
 User is allowed to access position (View for "position" only)
 User is allowed to access product_family (View for "product_family" only)
 User is allowed to access product_type (View for "product_type" only)
 User is allowed to access project_type (View for "project_type" only)
 User is allowed to access public_holiday (View for "public_holiday" only)
 User is allowed to access reference (View for "reference" only)
 User is allowed to access reporting_group (View for "reporting_group" only)
 User is allowed to access room (View for "room" only)
 User is allowed to access sap_cc (View for "sap_cc" only)
 User is allowed to access sex (View for "sex" only)
 User is allowed to access summary_report (View for "summary_report" only)
 User is allowed to access summary_type (View for "summary_type" only)
 User is allowed to access time_activity (View for "time_activity" only)
 User is allowed to access time_project_status (View for "time_project_status" only)
 User is allowed to access time_wp_group (View for "time_wp_group" only)
 User is allowed to access time_wp_summary_no (View for "time_wp_summary_no" only)
 User is allowed to access timesheet (View for "timesheet" only)
 User is allowed to access uc_type (View for "uc_type" only)
 User is allowed to access user_status (View for "user_status" only)
 User is allowed to access vac_aliq (View for "vac_aliq" only)
 User is allowed to access vacation_report (View for "vacation_report" only)
 User is allowed to access work_location (View for "work_location" only)
 User is allowed to create daily_record (Create for "daily_record" only)
 User is allowed to create doc (Create for "doc" only)
 User is allowed to create file (Create for "file" only)
 User is allowed to create leave_submission (Create for "leave_submission" only)
 User is allowed to create msg (Create for "msg" only)
 User is allowed to create queries (Create for "query" only)
 User is allowed to create time_record (Create for "time_record" only)
 User is allowed to create time_wp (Create for "time_wp" only)
 User is allowed to edit (some of) their own user details (Edit for "user": ('csv_delimiter', 'hide_message_files', 'lunch_duration', 'lunch_start', 'password', 'queries', 'realname', 'room', 'subst_active', 'substitute', 'timezone', 'title', 'tt_lines') only)
 User is allowed to edit doc (Edit for "doc" only)
 User is allowed to edit if he's the owner of the contact (Edit for "user_contact": ('visible',) only)
 User is allowed to edit their queries (Edit for "query" only)
 User is allowed to edit time category if the status is "Open" and he is responsible for the time category (Edit for "time_project": ('deputy', 'planned_effort', 'nosy') only)
 User is allowed to edit workpackage if he is time category owner or deputy (Edit for "time_wp": ('cost_center', 'is_public', 'name', 'responsible', 'time_wp_summary_no', 'wp_no') only)
 User is allowed to retire their queries (Retire for "query" only)
 User is allowed to search daily_record (Search for "daily_record" only)
 User is allowed to search for their own files (Search for "file" only)
 User is allowed to search for their own messages (Search for "msg" only)
 User is allowed to search for their queries (Search for "query" only)
 User is allowed to search leave_submission (Search for "leave_submission" only)
 User is allowed to search time_record (Search for "time_record" only)
 User is allowed to search time_wp (Search for "time_wp": ('activity', 'actor', 'cost_center', 'creation', 'creator', 'description', 'durations_allowed', 'epic_key', 'has_expiration_date', 'id', 'is_public', 'name', 'project', 'responsible', 'time_end', 'time_start', 'time_wp_summary_no', 'travel', 'wp_no') only)
 User is allowed to see time record if he is allowed to see all details on work package or User may view a daily_record (and time_records that are attached to that daily_record) if the user owns the daily_record or has role 'HR' or 'Controlling', or the user is supervisor or substitute supervisor of the owner of the daily record (the supervisor relationship is transitive) or the user is the department manager of the owner of the daily record. If user has role HR-Org-Location and is in the same Org-Location as the record, it may also be seen (View for "time_record" only)
 User is allowed to view contact if he's the owner of the contact or the contact is marked visible (View for "user_contact" only)
 User is allowed to view leave submission if he is the supervisor or the person to whom approvals are delegated (Edit for "leave_submission": ('status',) only)
 User is allowed to view leave submission if he is the supervisor or the person to whom approvals are delegated (View for "leave_submission" only)
 User is allowed to view selected fields if booking is allowed for at least one work package for this user (View for "time_project": ('activity', 'actor', 'cost_center', 'creation', 'creator', 'deputy', 'description', 'id', 'is_public_holiday', 'is_special_leave', 'is_vacation', 'name', 'op_project', 'organisation', 'overtime_reduction', 'product_family', 'project_type', 'reporting_group', 'responsible', 'status', 'work_location') only)
 User is allowed to view selected fields in work package if booking is allowed for this user (View for "time_wp": ('activity', 'actor', 'cost_center', 'creation', 'creator', 'description', 'durations_allowed', 'epic_key', 'has_expiration_date', 'id', 'is_public', 'name', 'project', 'responsible', 'time_end', 'time_start', 'time_wp_summary_no', 'travel', 'wp_no') only)
 User is allowed to view their own files (View for "file" only)
 User is allowed to view their own messages (View for "msg" only)
 User is allowed to view their own overtime information (View for "overtime_correction" only)
 User is allowed to view time record if he is the supervisor or the person to whom approvals are delegated (View for "time_record" only)
 User is allowed to view work package and time category names if he/she is department manager or supervisor or has role HR or HR-Org-Location (View for "time_project": ('name', 'project') only)
 User is allowed to view work package and time category names if he/she is department manager or supervisor or has role HR or HR-Org-Location (View for "time_wp": ('name', 'project') only)
 User is allowed to view/edit workpackage if he is owner or project responsible/deputy (Edit for "time_wp": ('bookers', 'description', 'epic_key', 'planned_effort', 'time_end', 'time_start', 'time_wp_summary_no') only)
 User may access the rest interface (Rest Access)
 User may access the web interface (Web Access)
 User may access the xmlrpc interface (Xmlrpc Access)
 User may edit own leave submissions (Edit for "leave_submission": ('comment', 'comment_cancel', 'first_day', 'last_day', 'status', 'time_wp', 'user') only)
 User may edit own leave submissions (View for "leave_submission": ('comment', 'comment_cancel', 'first_day', 'last_day', 'status', 'time_wp', 'user') only)
 User may see time report if reponsible or deputy of time project or on nosy list of time project (View for "time_report" only)
 User may use the email interface (Email Access)
 User may view a daily_record (and time_records that are attached to that daily_record) if the user owns the daily_record or has role 'HR' or 'Controlling', or the user is supervisor or substitute supervisor of the owner of the daily record (the supervisor relationship is transitive) or the user is the department manager of the owner of the daily record. If user has role HR-Org-Location and is in the same Org-Location as the record, it may also be seen (View for "daily_record" only)
 User may view time category if user is owner or deputy of time category or on nosy list of time category or if user is department manager of time category (View for "time_project" only)
 User may view work package if responsible for it, if user is owner or deputy of time category or on nosy list of time category or if user is department manager of time category (View for "time_wp" only)
 User or Timetracking by user may edit time_records owned by user (Edit for "time_record" only)
 User or Timetracking by user may edit time_records owned by user (View for "time_record" only)
 Users are allowed to view their own and public queries for classes where they have search permission (View for "query" only)
 Users may see daily record if they may see one of the time_records for that day (View for "daily_record" only)
Role "user_view":
 User is allowed to access user (View for "user" only)
""".strip ()
