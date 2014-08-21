security = """
New Web users get the Roles "User,Nosy"
New Email users get the Role "User"
Role "admin":
 User may access the web interface (Web Access)
 User may create everthing (Create)
 User may edit everthing (Edit)
 User may manipulate user Roles through the web (Web Roles)
 User may retire everthing (Retire)
 User may use the email interface (Email Access)
 User may view everthing (View)
Role "anonymous":
 User may access the web interface (Web Access)
Role "controlling":
 User is allowed Edit on (Edit for "daily_record": ('status', 'time_record') only)
 User is allowed Edit on (Edit for "time_wp": ('project',) only)
 User is allowed View on (View for "user": ('roles',) only)
 User is allowed to access daily_record_freeze (View for "daily_record_freeze" only)
 User is allowed to access overtime_correction (View for "overtime_correction" only)
 User is allowed to access query (View for "query" only)
 User is allowed to access time_project (View for "time_project" only)
 User is allowed to access time_record (View for "time_record" only)
 User is allowed to access time_wp (View for "time_wp" only)
 User is allowed to access vacation_correction (View for "vacation_correction" only)
 User is allowed to access vacation_submission (View for "vacation_submission" only)
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
Role "hr":
  (Edit for "overtime_period": ('name', 'order') only)
 Create (Create for "user_contact" only)
 User is allowed Edit on (Edit for "daily_record": ('required_overtime', 'weekend_allowed') only)
 User is allowed Edit on (Edit for "daily_record": ('status', 'time_record') only)
 User is allowed Edit on (Edit for "time_project": ('approval_hr', 'approval_required', 'is_public_holiday', 'no_overtime', 'overtime_reduction') only)
 User is allowed Edit on (Edit for "user": ('address', 'alternate_addresses', 'nickname', 'password', 'timezone', 'username') only)
 User is allowed Edit on (Edit for "user": ('clearance_by', 'firstname', 'job_description', 'lastname', 'lunch_duration', 'lunch_start', 'pictures', 'position', 'realname', 'room', 'sex', 'status', 'subst_active', 'substitute', 'supervisor', 'title', 'roles', 'tt_lines') only)
 User is allowed Edit on (Edit for "user": ('contacts',) only)
 User is allowed Edit on (Edit for "user_contact": ('contact', 'contact_type', 'description', 'order', 'user') only)
 User is allowed View on (View for "user": ('contacts',) only)
 User is allowed to access daily_record_freeze (View for "daily_record_freeze" only)
 User is allowed to access overtime_correction (View for "overtime_correction" only)
 User is allowed to access time_record (View for "time_record" only)
 User is allowed to access user_contact (View for "user_contact" only)
 User is allowed to access user_dynamic (View for "user_dynamic" only)
 User is allowed to access vacation_correction (View for "vacation_correction" only)
 User is allowed to access vacation_submission (View for "vacation_submission" only)
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
 User is allowed to edit time_record (Edit for "time_record" only)
 User is allowed to edit uc_type (Edit for "uc_type" only)
 User may manipulate user Roles through the web (Web Roles)
Role "hr-leave-approval":
 User is allowed to access vacation_correction (View for "vacation_correction" only)
 User is allowed to access vacation_submission (View for "vacation_submission" only)
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
 User is allowed to access vacation_correction (View for "vacation_correction" only)
 User is allowed to access vacation_submission (View for "vacation_submission" only)
 User is allowed to create vacation_correction (Create for "vacation_correction" only)
 User is allowed to create vacation_submission (Create for "vacation_submission" only)
 User is allowed to edit vacation_correction (Edit for "vacation_correction" only)
 User is allowed to edit vacation_submission (Edit for "vacation_submission" only)
 User may edit own vacation submissions (Edit for "vacation_submission": ('first_day', 'last_day', 'status', 'time_wp') only)
 User may edit own vacation submissions (View for "vacation_submission": ('first_day', 'last_day', 'status', 'time_wp') only)
Role "nosy":
 User may get nosy messages for doc (Nosy for "doc" only)
Role "office":
 Create (Create for "user_contact" only)
 User is allowed Edit on (Edit for "user": ('contacts',) only)
 User is allowed Edit on (Edit for "user": ('title', 'room', 'position') only)
 User is allowed Edit on (Edit for "user_contact": ('contact', 'contact_type', 'description', 'order', 'user') only)
 User is allowed View on (View for "user": ('contacts',) only)
 User is allowed to access user_contact (View for "user_contact" only)
 User is allowed to create room (Create for "room" only)
 User is allowed to create uc_type (Create for "uc_type" only)
 User is allowed to edit room (Edit for "room" only)
 User is allowed to edit uc_type (Edit for "uc_type" only)
Role "pgp":
Role "project":
 User is allowed Edit on (Edit for "time_project": ('cost_center', 'department', 'deputy', 'description', 'max_hours', 'name', 'nosy', 'op_project', 'organisation', 'planned_effort', 'product_family', 'project_type', 'reporting_group', 'responsible', 'status') only)
 User is allowed to access time_project (View for "time_project" only)
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
 User is allowed to access time_wp (View for "time_wp" only)
Role "staff-report":
Role "user":
  (Search for "time_project": ('activity', 'actor', 'cost_center', 'creation', 'creator', 'deputy', 'description', 'id', 'is_public_holiday', 'name', 'op_project', 'organisation', 'overtime_reduction', 'product_family', 'project_type', 'reporting_group', 'responsible', 'status', 'work_location') only)
  (Search for "time_wp": ('activity', 'actor', 'cost_center', 'creation', 'creator', 'description', 'durations_allowed', 'id', 'name', 'project', 'responsible', 'time_end', 'time_start', 'travel', 'wp_no') only)
 Search (Search for "user_contact" only)
 User is allowed Edit on file if file is linked from an item with Edit permission (Edit for "file" only)
 User is allowed View on (View for "user": ('activity', 'actor', 'address', 'alternate_addresses', 'clearance_by', 'creation', 'creator', 'department', 'firstname', 'job_description', 'lastname', 'id', 'lunch_duration', 'lunch_start', 'nickname', 'pictures', 'position', 'queries', 'realname', 'room', 'sex', 'status', 'subst_active', 'substitute', 'supervisor', 'timezone', 'title', 'username', 'home_directory', 'login_shell', 'samba_home_drive', 'samba_home_path', 'tt_lines') only)
 User is allowed View on (View for "user": ('contacts',) only)
 User is allowed View on file if file is linked from an item with View permission (View for "file" only)
 User is allowed View on msg if msg is linked from an item with View permission (View for "msg" only)
 User is allowed to access artefact (View for "artefact" only)
 User is allowed to access cost_center (View for "cost_center" only)
 User is allowed to access cost_center_group (View for "cost_center_group" only)
 User is allowed to access cost_center_status (View for "cost_center_status" only)
 User is allowed to access daily_record (View for "daily_record" only)
 User is allowed to access daily_record_status (View for "daily_record_status" only)
 User is allowed to access department (View for "department" only)
 User is allowed to access doc (View for "doc" only)
 User is allowed to access doc_status (View for "doc_status" only)
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
 User is allowed to access sex (View for "sex" only)
 User is allowed to access summary_report (View for "summary_report" only)
 User is allowed to access summary_type (View for "summary_type" only)
 User is allowed to access time_activity (View for "time_activity" only)
 User is allowed to access time_project_status (View for "time_project_status" only)
 User is allowed to access time_wp_group (View for "time_wp_group" only)
 User is allowed to access uc_type (View for "uc_type" only)
 User is allowed to access user_status (View for "user_status" only)
 User is allowed to access vacation_report (View for "vacation_report" only)
 User is allowed to access vacation_status (View for "vacation_status" only)
 User is allowed to access work_location (View for "work_location" only)
 User is allowed to create daily_record (Create for "daily_record" only)
 User is allowed to create doc (Create for "doc" only)
 User is allowed to create file (Create for "file" only)
 User is allowed to create msg (Create for "msg" only)
 User is allowed to create queries (Create for "query" only)
 User is allowed to create time_record (Create for "time_record" only)
 User is allowed to create time_wp (Create for "time_wp" only)
 User is allowed to create vacation_submission (Create for "vacation_submission" only)
 User is allowed to edit (some of) their own user details (Edit for "user": ('csv_delimiter', 'lunch_duration', 'lunch_start', 'password', 'queries', 'realname', 'room', 'subst_active', 'substitute', 'timezone', 'title', 'tt_lines') only)
 User is allowed to edit daily record if he is owner or supervisor (Edit for "daily_record": ('status', 'time_record') only)
 User is allowed to edit daily record if he is owner or supervisor (View for "daily_record": ('status', 'time_record') only)
 User is allowed to edit doc (Edit for "doc" only)
 User is allowed to edit if he's the owner of the contact (Edit for "user_contact": ('visible',) only)
 User is allowed to edit their queries (Edit for "query" only)
 User is allowed to edit time category if the status is "Open" and he is responsible for the time category (Edit for "time_project": ('deputy', 'planned_effort', 'nosy') only)
 User is allowed to edit workpackage if he is time category owner (Edit for "time_wp": ('name', 'responsible', 'wp_no', 'cost_center') only)
 User is allowed to retire their queries (Retire for "query" only)
 User is allowed to search for their own files (Search for "file" only)
 User is allowed to search for their own messages (Search for "msg" only)
 User is allowed to search for their queries (Search for "query" only)
 User is allowed to see time record if he is allowed to see all details on work package or User may view a daily_record (and time_records that are attached to that daily_record) if the user owns the daily_record or has role 'HR' or 'Controlling', or the user is supervisor or substitute supervisor of the owner of the daily record (the supervisor relationship is transitive) or the user is the department manager of the owner of the daily record. If user has role HR-Org-Location and is in the same Org-Location as the record, it may also be seen (View for "time_record" only)
 User is allowed to view contact if he's the owner of the contact or the contact is marked visible (View for "user_contact" only)
 User is allowed to view selected fields if booking is allowed for at least one work package for this user (View for "time_project": ('activity', 'actor', 'cost_center', 'creation', 'creator', 'deputy', 'description', 'id', 'is_public_holiday', 'name', 'op_project', 'organisation', 'overtime_reduction', 'product_family', 'project_type', 'reporting_group', 'responsible', 'status', 'work_location') only)
 User is allowed to view selected fields in work package if booking is allowed for this user (View for "time_wp": ('name', 'wp_no', 'description', 'responsible', 'project', 'time_start', 'time_end', 'durations_allowed', 'travel', 'cost_center', 'creation', 'creator', 'activity', 'actor', 'id') only)
 User is allowed to view their own files (View for "file" only)
 User is allowed to view their own messages (View for "msg" only)
 User is allowed to view time record if he is the supervisor or the person to whom approvals are delegated (View for "time_record" only)
 User is allowed to view work package and time category names if he/she is department manager or supervisor or has role HR or HR-Org-Location (View for "time_project": ('name', 'project') only)
 User is allowed to view work package and time category names if he/she is department manager or supervisor or has role HR or HR-Org-Location (View for "time_wp": ('name', 'project') only)
 User is allowed to view/edit workpackage if he is owner or project responsible/deputy (Edit for "time_wp": ('description', 'time_start', 'time_end', 'bookers', 'planned_effort') only)
 User may access the web interface (Web Access)
 User may edit own time_records (Edit for "time_record" only)
 User may edit own time_records (View for "time_record" only)
 User may edit own vacation submissions (Edit for "vacation_submission": ('first_day', 'last_day', 'status', 'time_wp') only)
 User may edit own vacation submissions (View for "vacation_submission": ('first_day', 'last_day', 'status', 'time_wp') only)
 User may use the email interface (Email Access)
 User may view time category if user is owner or deputy of time category or on nosy list of time category or if user is department manager of time category (View for "time_project" only)
 User may view work package if responsible for it, if user is owner or deputy of time category or on nosy list of time category or if user is department manager of time category (View for "time_wp" only)
 Users are allowed to view their own and public queries for classes where they have search permission (View for "query" only)
 search time_record (Search for "time_record" only)
 search time_wp (Search for "time_wp": ('activity', 'actor', 'cost_center', 'creation', 'creator', 'description', 'durations_allowed', 'id', 'name', 'project', 'responsible', 'time_end', 'time_start', 'travel', 'wp_no') only)
""".strip ()
