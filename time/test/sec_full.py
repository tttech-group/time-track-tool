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
Role "contact":
 User is allowed to create contact (Create for "contact" only)
 User is allowed to edit contact (Edit for "contact" only)
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
Role "external":
 External users are allowed to access issue if they are on the list of allowed external users or there is a transitive permission via containers (Edit for "issue": ['activity', 'actor', 'area', 'category', 'closed', 'composed_of', 'creation', 'creator', 'cur_est_begin', 'cur_est_end', 'deadline', 'depends', 'doc_issue_status', 'earliest_start', 'effective_prio', 'files', 'files_affected', 'fixed_in', 'id', 'keywords', 'kind', 'maturity_index', 'messages', 'needs', 'nosy', 'numeric_effort', 'part_of', 'planned_begin', 'planned_end', 'priority', 'release', 'responsible', 'severity', 'status', 'superseder', 'title'] only)
 External users are allowed to access issue if they are on the list of allowed external users or there is a transitive permission via containers (View for "issue": ['activity', 'actor', 'area', 'category', 'closed', 'composed_of', 'creation', 'creator', 'cur_est_begin', 'cur_est_end', 'deadline', 'depends', 'doc_issue_status', 'earliest_start', 'effective_prio', 'files', 'files_affected', 'fixed_in', 'id', 'keywords', 'kind', 'maturity_index', 'messages', 'needs', 'nosy', 'numeric_effort', 'part_of', 'planned_begin', 'planned_end', 'priority', 'release', 'responsible', 'severity', 'status', 'superseder', 'title'] only)
 User is allowed Edit on file if file is linked from an item with Edit permission (Edit for "file" only)
 User is allowed View on (View for "category": ('name',) only)
 User is allowed View on (View for "user": ('nickname', 'username') only)
 User is allowed View on (View for "user_status": ('name',) only)
 User is allowed View on file if file is linked from an item with View permission (View for "file" only)
 User is allowed View on msg if msg is linked from an item with View permission (View for "msg" only)
 User is allowed to access area (View for "area" only)
 User is allowed to access doc_issue_status (View for "doc_issue_status" only)
 User is allowed to access keyword (View for "keyword" only)
 User is allowed to access kind (View for "kind" only)
 User is allowed to access msg_keyword (View for "msg_keyword" only)
 User is allowed to access severity (View for "severity" only)
 User is allowed to access status (View for "status" only)
 User is allowed to access status_transition (View for "status_transition" only)
 User is allowed to create file (Create for "file" only)
 User is allowed to create issue (Create for "issue" only)
 User is allowed to create msg (Create for "msg" only)
 User is allowed to create query (Create for "query" only)
 User is allowed to edit their queries (Edit for "query" only)
 User is allowed to retire their queries (Retire for "query" only)
 User is allowed to search for their own files (Search for "file" only)
 User is allowed to search for their own messages (Search for "msg" only)
 User is allowed to search for their queries (Search for "query" only)
 User is allowed to view their own files (View for "file" only)
 User may access the web interface (Web Access)
 User may use the email interface (Email Access)
 Users are allowed to edit some of their details (Edit for "user": ('csv_delimiter', 'password', 'timezone') only)
 Users are allowed to view some of their details (View for "user": ('activity', 'actor', 'creation', 'creator', 'firstname', 'lastname', 'realname', 'username') only)
 Users are allowed to view their own and public queries for classes where they have search permission (View for "query" only)
 search issue (Search for "issue" only)
Role "hr":
  (Edit for "overtime_period": ('name', 'order') only)
 Create (Create for "user_contact" only)
 User is allowed Edit on (Edit for "daily_record": ('required_overtime', 'weekend_allowed') only)
 User is allowed Edit on (Edit for "daily_record": ('status', 'time_record') only)
 User is allowed Edit on (Edit for "time_project": ('is_public_holiday', 'no_overtime', 'overtime_reduction') only)
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
Role "hr-org-location":
  (Search for "daily_record_freeze" only)
  (Search for "overtime_correction" only)
  (Search for "time_record" only)
  (Search for "user_dynamic" only)
 User is allowed to view dynamic user data if he/she is in group HR-Org-Location and in the same Org-Location as the given user (View for "user_dynamic" only)
 User is allowed to view freeze information if he/she is in group HR-Org-Location and in the same Org-Location as the given user (View for "daily_record_freeze" only)
 User is allowed to view overtime information if he/she is in group HR-Org-Location and in the same Org-Location as the given user (View for "overtime_correction" only)
 User is allowed to view time record data if he/she is in group HR-Org-Location and in the same Org-Location as the given user (View for "time_record" only)
Role "issue_admin":
 User is allowed Edit on msg if msg is linked from an item with Edit permission (Edit for "msg" only)
 User is allowed to access issue (View for "issue" only)
 User is allowed to create area (Create for "area" only)
 User is allowed to create category (Create for "category" only)
 User is allowed to create doc_issue_status (Create for "doc_issue_status" only)
 User is allowed to create issue (Create for "issue" only)
 User is allowed to create keyword (Create for "keyword" only)
 User is allowed to create kind (Create for "kind" only)
 User is allowed to create msg_keyword (Create for "msg_keyword" only)
 User is allowed to create prodcat (Create for "prodcat" only)
 User is allowed to create severity (Create for "severity" only)
 User is allowed to create status (Create for "status" only)
 User is allowed to create status_transition (Create for "status_transition" only)
 User is allowed to edit area (Edit for "area" only)
 User is allowed to edit category (Edit for "category" only)
 User is allowed to edit doc_issue_status (Edit for "doc_issue_status" only)
 User is allowed to edit issue (Edit for "issue" only)
 User is allowed to edit keyword (Edit for "keyword" only)
 User is allowed to edit kind (Edit for "kind" only)
 User is allowed to edit msg_keyword (Edit for "msg_keyword" only)
 User is allowed to edit prodcat (Edit for "prodcat" only)
 User is allowed to edit severity (Edit for "severity" only)
 User is allowed to edit status (Edit for "status" only)
 User is allowed to edit status_transition (Edit for "status_transition" only)
Role "it":
 Create (Create for "user_contact" only)
 User is allowed Edit on (Edit for "location": ('domain_part',) only)
 User is allowed Edit on (Edit for "org_location": ('smb_domain', 'dhcp_server', 'domino_dn') only)
 User is allowed Edit on (Edit for "organisation": ('domain_part',) only)
 User is allowed Edit on (Edit for "user": ('address', 'alternate_addresses', 'nickname', 'password', 'timezone', 'username', 'is_lotus_user', 'sync_with_ldap', 'group', 'secondary_groups', 'uid', 'home_directory', 'login_shell', 'samba_home_drive', 'samba_home_path', 'samba_kickoff_time', 'samba_lm_password', 'samba_logon_script', 'samba_nt_password', 'samba_profile_path', 'samba_pwd_can_change', 'samba_pwd_last_set', 'samba_pwd_must_change', 'user_password', 'shadow_last_change', 'shadow_min', 'shadow_max', 'shadow_warning', 'shadow_inactive', 'shadow_expire', 'shadow_used') only)
 User is allowed Edit on (Edit for "user": ('address', 'alternate_addresses', 'nickname', 'password', 'timezone', 'username') only)
 User is allowed Edit on (Edit for "user": ('contacts',) only)
 User is allowed Edit on (Edit for "user": ('is_lotus_user', 'sync_with_ldap', 'group', 'pictures', 'secondary_groups', 'uid', 'home_directory', 'login_shell', 'samba_home_drive', 'samba_home_path', 'samba_kickoff_time', 'samba_lm_password', 'samba_logon_script', 'samba_nt_password', 'samba_profile_path', 'samba_pwd_can_change', 'samba_pwd_last_set', 'samba_pwd_must_change', 'user_password', 'shadow_last_change', 'shadow_min', 'shadow_max', 'shadow_warning', 'shadow_inactive', 'shadow_expire', 'shadow_used') only)
 User is allowed Edit on (Edit for "user_contact": ('contact', 'contact_type', 'description', 'order', 'user') only)
 User is allowed Edit on msg if msg is linked from an item with Edit permission (Edit for "msg" only)
 User is allowed to access it_issue (View for "it_issue" only)
 User is allowed to access it_project (View for "it_project" only)
 User is allowed to create it_category (Create for "it_category" only)
 User is allowed to create it_issue (Create for "it_issue" only)
 User is allowed to create it_project (Create for "it_project" only)
 User is allowed to create mailgroup (Create for "mailgroup" only)
 User is allowed to edit it_category (Edit for "it_category" only)
 User is allowed to edit it_issue (Edit for "it_issue" only)
 User is allowed to edit it_project (Edit for "it_project" only)
 User is allowed to edit mailgroup (Edit for "mailgroup" only)
 User may manipulate user Roles through the web (Web Roles)
Role "itview":
 User is allowed to access it_issue (View for "it_issue" only)
 User is allowed to access it_project (View for "it_project" only)
Role "nosy":
 User may get nosy messages for doc (Nosy for "doc" only)
 User may get nosy messages for issue (Nosy for "issue" only)
 User may get nosy messages for it_issue (Nosy for "it_issue" only)
 User may get nosy messages for it_project (Nosy for "it_project" only)
 User may get nosy messages for support (Nosy for "support" only)
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
 User is allowed Edit on (Edit for "time_project": ('cost_center', 'department', 'deputy', 'description', 'max_hours', 'name', 'nosy', 'op_project', 'organisation', 'planned_effort', 'responsible', 'status') only)
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
Role "supportadmin":
 User is allowed to access contact (View for "contact" only)
 User is allowed to access customer (View for "customer" only)
 User is allowed to access mailgroup (View for "mailgroup" only)
 User is allowed to access sup_classification (View for "sup_classification" only)
 User is allowed to access support (View for "support" only)
 User is allowed to create contact (Create for "contact" only)
 User is allowed to create customer (Create for "customer" only)
 User is allowed to create mailgroup (Create for "mailgroup" only)
 User is allowed to create sup_classification (Create for "sup_classification" only)
 User is allowed to create support (Create for "support" only)
 User is allowed to edit contact (Edit for "contact" only)
 User is allowed to edit customer (Edit for "customer" only)
 User is allowed to edit mailgroup (Edit for "mailgroup" only)
 User is allowed to edit sup_classification (Edit for "sup_classification" only)
 User is allowed to edit support (Edit for "support" only)
Role "user":
  (Search for "time_project": ('activity', 'actor', 'cost_center', 'creation', 'creator', 'deputy', 'description', 'id', 'is_public_holiday', 'name', 'op_project', 'organisation', 'overtime_reduction', 'product_family', 'project_type', 'reporting_group', 'responsible', 'status', 'work_location') only)
  (Search for "time_wp": ('activity', 'actor', 'cost_center', 'creation', 'creator', 'description', 'durations_allowed', 'id', 'name', 'project', 'responsible', 'time_end', 'time_start', 'travel', 'wp_no') only)
 Search (Search for "user_contact" only)
 User is allowed Edit on file if file is linked from an item with Edit permission (Edit for "file" only)
 User is allowed Edit on issue if issue is non-confidential or user is on nosy list (Edit for "issue" only)
 User is allowed Edit on it_issue if it_issue is non-confidential or user is on nosy list (Edit for "it_issue": ('messages', 'files', 'nosy') only)
 User is allowed Edit on it_project if it_project is non-confidential or user is on nosy list (Edit for "it_project": ('messages', 'files', 'nosy') only)
 User is allowed Edit on support if support is non-confidential or user is on nosy list (Edit for "support" only)
 User is allowed View on (View for "user": ('activity', 'actor', 'address', 'alternate_addresses', 'clearance_by', 'creation', 'creator', 'department', 'firstname', 'job_description', 'lastname', 'id', 'lunch_duration', 'lunch_start', 'nickname', 'password', 'pictures', 'position', 'queries', 'realname', 'room', 'sex', 'status', 'subst_active', 'substitute', 'supervisor', 'timezone', 'title', 'username', 'home_directory', 'login_shell', 'samba_home_drive', 'samba_home_path', 'tt_lines') only)
 User is allowed View on (View for "user": ('activity', 'actor', 'address', 'alternate_addresses', 'clearance_by', 'creation', 'creator', 'department', 'firstname', 'id', 'job_description', 'lastname', 'lunch_duration', 'lunch_start', 'nickname', 'password', 'pictures', 'position', 'queries', 'realname', 'room', 'sex', 'status', 'subst_active', 'substitute', 'supervisor', 'timezone', 'title', 'username', 'home_directory', 'login_shell', 'samba_home_drive', 'samba_home_path') only)
 User is allowed View on (View for "user": ('contacts',) only)
 User is allowed View on file if file is linked from an item with View permission (View for "file" only)
 User is allowed View on issue if issue is non-confidential or user is on nosy list (View for "issue" only)
 User is allowed View on it_issue if it_issue is non-confidential or user is on nosy list (View for "it_issue" only)
 User is allowed View on it_project if it_project is non-confidential or user is on nosy list (View for "it_project" only)
 User is allowed View on msg if msg is linked from an item with View permission (View for "msg" only)
 User is allowed View on support if support is non-confidential or user is on nosy list (View for "support" only)
 User is allowed to access area (View for "area" only)
 User is allowed to access artefact (View for "artefact" only)
 User is allowed to access category (View for "category" only)
 User is allowed to access contact (View for "contact" only)
 User is allowed to access contact_type (View for "contact_type" only)
 User is allowed to access cost_center (View for "cost_center" only)
 User is allowed to access cost_center_group (View for "cost_center_group" only)
 User is allowed to access cost_center_status (View for "cost_center_status" only)
 User is allowed to access customer (View for "customer" only)
 User is allowed to access daily_record (View for "daily_record" only)
 User is allowed to access daily_record_status (View for "daily_record_status" only)
 User is allowed to access department (View for "department" only)
 User is allowed to access doc (View for "doc" only)
 User is allowed to access doc_issue_status (View for "doc_issue_status" only)
 User is allowed to access doc_status (View for "doc_status" only)
 User is allowed to access it_category (View for "it_category" only)
 User is allowed to access it_issue_status (View for "it_issue_status" only)
 User is allowed to access it_prio (View for "it_prio" only)
 User is allowed to access it_project_status (View for "it_project_status" only)
 User is allowed to access keyword (View for "keyword" only)
 User is allowed to access kind (View for "kind" only)
 User is allowed to access location (View for "location" only)
 User is allowed to access mailgroup (View for "mailgroup" only)
 User is allowed to access msg_keyword (View for "msg_keyword" only)
 User is allowed to access org_location (View for "org_location" only)
 User is allowed to access organisation (View for "organisation" only)
 User is allowed to access overtime_period (View for "overtime_period" only)
 User is allowed to access position (View for "position" only)
 User is allowed to access prodcat (View for "prodcat" only)
 User is allowed to access product_family (View for "product_family" only)
 User is allowed to access product_type (View for "product_type" only)
 User is allowed to access project_type (View for "project_type" only)
 User is allowed to access public_holiday (View for "public_holiday" only)
 User is allowed to access reference (View for "reference" only)
 User is allowed to access reporting_group (View for "reporting_group" only)
 User is allowed to access room (View for "room" only)
 User is allowed to access severity (View for "severity" only)
 User is allowed to access sex (View for "sex" only)
 User is allowed to access status (View for "status" only)
 User is allowed to access status_transition (View for "status_transition" only)
 User is allowed to access summary_report (View for "summary_report" only)
 User is allowed to access summary_type (View for "summary_type" only)
 User is allowed to access sup_classification (View for "sup_classification" only)
 User is allowed to access sup_prio (View for "sup_prio" only)
 User is allowed to access sup_status (View for "sup_status" only)
 User is allowed to access time_activity (View for "time_activity" only)
 User is allowed to access time_project_status (View for "time_project_status" only)
 User is allowed to access time_wp_group (View for "time_wp_group" only)
 User is allowed to access uc_type (View for "uc_type" only)
 User is allowed to access user_status (View for "user_status" only)
 User is allowed to access work_location (View for "work_location" only)
 User is allowed to create daily_record (Create for "daily_record" only)
 User is allowed to create doc (Create for "doc" only)
 User is allowed to create file (Create for "file" only)
 User is allowed to create issue (Create for "issue" only)
 User is allowed to create it_issue (Create for "it_issue" only)
 User is allowed to create msg (Create for "msg" only)
 User is allowed to create queries (Create for "query" only)
 User is allowed to create support (Create for "support" only)
 User is allowed to create time_record (Create for "time_record" only)
 User is allowed to create time_wp (Create for "time_wp" only)
 User is allowed to edit (some of) their own user details (Edit for "user": ('csv_delimiter', 'lunch_duration', 'lunch_start', 'password', 'queries', 'realname', 'room', 'subst_active', 'substitute', 'timezone', 'title', 'tt_lines') only)
 User is allowed to edit category if he is responsible for it (Edit for "category": ('nosy', 'default_part_of') only)
 User is allowed to edit daily record if he is owner or supervisor (Edit for "daily_record": ('status', 'time_record') only)
 User is allowed to edit daily record if he is owner or supervisor (View for "daily_record": ('status', 'time_record') only)
 User is allowed to edit doc (Edit for "doc" only)
 User is allowed to edit if he's the owner of the contact (Edit for "user_contact": ('visible',) only)
 User is allowed to edit several fields if he is Stakeholder/Responsible for an it_issue (Edit for "it_issue": ('deadline', 'responsible', 'status', 'title') only)
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
 User may use the email interface (Email Access)
 User may view time category if user is owner or deputy of time category or on nosy list of time category or if user is department manager of time category (View for "time_project" only)
 User may view work package if responsible for it, if user is owner or deputy of time category or on nosy list of time category or if user is department manager of time category (View for "time_wp" only)
 Users are allowed to view their own and public queries for classes where they have search permission (View for "query" only)
 search issue (Search for "issue" only)
 search it_issue (Search for "it_issue" only)
 search it_project (Search for "it_project" only)
 search support (Search for "support" only)
 search time_record (Search for "time_record" only)
 search time_wp (Search for "time_wp": ('activity', 'actor', 'cost_center', 'creation', 'creator', 'description', 'durations_allowed', 'id', 'name', 'project', 'responsible', 'time_end', 'time_start', 'travel', 'wp_no') only)
""".strip ()
