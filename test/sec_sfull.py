security = """
New Web users get the Roles "User,Nosy"
New Email users get the Role "User"
Role "admin":
 User may access the web interface (Web Access)
 User may create everything (Create)
 User may edit everything (Edit)
 User may manipulate user Roles through the web (Web Roles)
 User may restore everything (Restore)
 User may retire everything (Retire)
 User may use the email interface (Email Access)
 User may view everything (View)
Role "adr_readonly":
 User is allowed to access adr_type (View for "adr_type" only)
 User is allowed to access adr_type_cat (View for "adr_type_cat" only)
 User is allowed to access contact (View for "contact" only)
 User is allowed to access contact_type (View for "contact_type" only)
 User is allowed to access valid (View for "valid" only)
 User may access the web interface (Web Access)
Role "anonymous":
 User may access the web interface (Web Access)
Role "contact":
 User is allowed to create contact (Create for "contact" only)
 User is allowed to edit contact (Edit for "contact" only)
Role "controlling":
 User is allowed Edit on (Edit for "daily_record": ('status', 'time_record') only)
 User is allowed Edit on (Edit for "time_wp": ('project',) only)
 User is allowed View on (View for "user": ('roles',) only)
 User is allowed to access contract_type (View for "contract_type" only)
 User is allowed to access daily_record (View for "daily_record" only)
 User is allowed to access daily_record_freeze (View for "daily_record_freeze" only)
 User is allowed to access leave_submission (View for "leave_submission" only)
 User is allowed to access overtime_correction (View for "overtime_correction" only)
 User is allowed to access query (View for "query" only)
 User is allowed to access time_project (View for "time_project" only)
 User is allowed to access time_record (View for "time_record" only)
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
Role "facility":
 User is allowed Edit on (Edit for "user": ('room',) only)
 User is allowed to create room (Create for "room" only)
 User is allowed to edit room (Edit for "room" only)
Role "hr":
  (Edit for "overtime_period": ('name', 'order') only)
 User is allowed Edit on (Edit for "daily_record": ('required_overtime', 'weekend_allowed') only)
 User is allowed Edit on (Edit for "daily_record": ('status', 'time_record') only)
 User is allowed Edit on (Edit for "time_project": ('approval_hr', 'approval_required', 'is_public_holiday', 'is_special_leave', 'is_vacation', 'no_overtime', 'no_overtime_day', 'overtime_reduction') only)
 User is allowed Edit on (Edit for "user": ('address', 'alternate_addresses', 'nickname', 'password', 'timezone', 'username') only)
 User is allowed Edit on (Edit for "user": ('clearance_by', 'firstname', 'job_description', 'lastname', 'lunch_duration', 'lunch_start', 'pictures', 'position', 'realname', 'room', 'sex', 'status', 'subst_active', 'substitute', 'supervisor', 'title', 'roles', 'tt_lines') only)
 User is allowed to access contract_type (View for "contract_type" only)
 User is allowed to access daily_record (View for "daily_record" only)
 User is allowed to access daily_record_freeze (View for "daily_record_freeze" only)
 User is allowed to access leave_submission (View for "leave_submission" only)
 User is allowed to access overtime_correction (View for "overtime_correction" only)
 User is allowed to access time_record (View for "time_record" only)
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
Role "issue_admin":
 User is allowed Edit on msg if msg is linked from an item with Edit permission (Edit for "msg" only)
 User is allowed to access issue (View for "issue" only)
 User is allowed to create area (Create for "area" only)
 User is allowed to create category (Create for "category" only)
 User is allowed to create doc_issue_status (Create for "doc_issue_status" only)
 User is allowed to create ext_tracker (Create for "ext_tracker" only)
 User is allowed to create issue (Create for "issue" only)
 User is allowed to create keyword (Create for "keyword" only)
 User is allowed to create kind (Create for "kind" only)
 User is allowed to create msg_keyword (Create for "msg_keyword" only)
 User is allowed to create safety_level (Create for "safety_level" only)
 User is allowed to create severity (Create for "severity" only)
 User is allowed to create status (Create for "status" only)
 User is allowed to create status_transition (Create for "status_transition" only)
 User is allowed to create test_level (Create for "test_level" only)
 User is allowed to edit area (Edit for "area" only)
 User is allowed to edit category (Edit for "category" only)
 User is allowed to edit doc_issue_status (Edit for "doc_issue_status" only)
 User is allowed to edit ext_tracker (Edit for "ext_tracker" only)
 User is allowed to edit issue (Edit for "issue" only)
 User is allowed to edit keyword (Edit for "keyword" only)
 User is allowed to edit kind (Edit for "kind" only)
 User is allowed to edit msg_keyword (Edit for "msg_keyword" only)
 User is allowed to edit safety_level (Edit for "safety_level" only)
 User is allowed to edit severity (Edit for "severity" only)
 User is allowed to edit status (Edit for "status" only)
 User is allowed to edit status_transition (Edit for "status_transition" only)
 User is allowed to edit test_level (Edit for "test_level" only)
Role "it":
 User is allowed Edit on (Edit for "file": ('name', 'type') only)
 User is allowed Edit on (Edit for "location": ('domain_part',) only)
 User is allowed Edit on (Edit for "org_location": ('smb_domain', 'dhcp_server', 'domino_dn') only)
 User is allowed Edit on (Edit for "organisation": ('domain_part',) only)
 User is allowed Edit on (Edit for "user": ('address', 'alternate_addresses', 'nickname', 'password', 'timezone', 'username', 'is_lotus_user', 'sync_with_ldap', 'group', 'secondary_groups', 'uid', 'home_directory', 'login_shell', 'samba_home_drive', 'samba_home_path', 'samba_kickoff_time', 'samba_lm_password', 'samba_logon_script', 'samba_nt_password', 'samba_profile_path', 'samba_pwd_can_change', 'samba_pwd_last_set', 'samba_pwd_must_change', 'user_password', 'shadow_last_change', 'shadow_min', 'shadow_max', 'shadow_warning', 'shadow_inactive', 'shadow_expire', 'shadow_used') only)
 User is allowed Edit on (Edit for "user": ('address', 'alternate_addresses', 'nickname', 'password', 'timezone', 'username') only)
 User is allowed Edit on (Edit for "user": ('is_lotus_user', 'sync_with_ldap', 'group', 'secondary_groups', 'uid', 'home_directory', 'login_shell', 'samba_home_drive', 'samba_home_path', 'samba_kickoff_time', 'samba_lm_password', 'samba_logon_script', 'samba_nt_password', 'samba_profile_path', 'samba_pwd_can_change', 'samba_pwd_last_set', 'samba_pwd_must_change', 'user_password', 'shadow_last_change', 'shadow_min', 'shadow_max', 'shadow_warning', 'shadow_inactive', 'shadow_expire', 'shadow_used') only)
 User is allowed Edit on file if file is linked from an item with Edit permission (Edit for "file" only)
 User is allowed Edit on msg if msg is linked from an item with Edit permission (Edit for "msg" only)
 User is allowed View on file if file is linked from an item with View permission (View for "file" only)
 User is allowed to access it_int_prio (View for "it_int_prio" only)
 User is allowed to access it_issue (View for "it_issue" only)
 User is allowed to access it_project (View for "it_project" only)
 User is allowed to create it_category (Create for "it_category" only)
 User is allowed to create it_int_prio (Create for "it_int_prio" only)
 User is allowed to create it_issue (Create for "it_issue" only)
 User is allowed to create it_project (Create for "it_project" only)
 User is allowed to create it_request_type (Create for "it_request_type" only)
 User is allowed to create mailgroup (Create for "mailgroup" only)
 User is allowed to edit it_category (Edit for "it_category" only)
 User is allowed to edit it_int_prio (Edit for "it_int_prio" only)
 User is allowed to edit it_issue (Edit for "it_issue" only)
 User is allowed to edit it_project (Edit for "it_project" only)
 User is allowed to edit it_request_type (Edit for "it_request_type" only)
 User is allowed to edit mailgroup (Edit for "mailgroup" only)
 User may manipulate user Roles through the web (Web Roles)
Role "itview":
 User is allowed to access it_int_prio (View for "it_int_prio" only)
 User is allowed to access it_issue (View for "it_issue" only)
 User is allowed to access it_project (View for "it_project" only)
Role "msgedit":
  (Search for "msg": ('date', 'id') only)
 User is allowed Edit on (Edit for "msg": ('author', 'date', 'id', 'keywords', 'subject', 'summary') only)
 User is allowed to access ext_msg (View for "ext_msg" only)
 User is allowed to access ext_tracker_state (View for "ext_tracker_state" only)
 User is allowed to access ext_tracker_type (View for "ext_tracker_type" only)
Role "msgsync":
  (Search for "msg": ('date', 'id') only)
 User is allowed Edit on (Edit for "msg": ('author', 'date', 'id', 'keywords', 'subject', 'summary') only)
 User is allowed to access ext_msg (View for "ext_msg" only)
 User is allowed to access ext_tracker_state (View for "ext_tracker_state" only)
 User is allowed to access ext_tracker_type (View for "ext_tracker_type" only)
 User is allowed to create ext_msg (Create for "ext_msg" only)
 User is allowed to create ext_tracker_state (Create for "ext_tracker_state" only)
 User is allowed to edit ext_msg (Edit for "ext_msg" only)
 User is allowed to edit ext_tracker_state (Edit for "ext_tracker_state" only)
Role "nosy":
 User may get nosy messages for doc (Nosy for "doc" only)
 User may get nosy messages for issue (Nosy for "issue" only)
 User may get nosy messages for it_issue (Nosy for "it_issue" only)
 User may get nosy messages for it_project (Nosy for "it_project" only)
 User may get nosy messages for support (Nosy for "support" only)
Role "office":
 User is allowed Edit on (Edit for "user": ('title', 'room', 'position') only)
 User is allowed to create absence (Create for "absence" only)
 User is allowed to create absence_type (Create for "absence_type" only)
 User is allowed to create room (Create for "room" only)
 User is allowed to edit absence (Edit for "absence" only)
 User is allowed to edit absence_type (Edit for "absence_type" only)
 User is allowed to edit room (Edit for "room" only)
Role "procurement":
  (View for "sap_cc" only)
  (View for "time_project" only)
 User is allowed Edit on (Edit for "sap_cc": ('purchasing_agents',) only)
 User is allowed Edit on (Edit for "time_project": ('purchasing_agents',) only)
Role "project":
 User is allowed Edit on (Edit for "time_project": ('cost_center', 'department', 'deputy', 'description', 'name', 'nosy', 'organisation', 'responsible', 'status') only)
 User is allowed Edit on (Edit for "time_project": ('max_hours', 'op_project', 'planned_effort', 'product_family', 'project_type', 'reporting_group', 'work_location') only)
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
Role "sec-incident-nosy":
 User is allowed to access it_int_prio (View for "it_int_prio" only)
 User is allowed to access it_issue (View for "it_issue" only)
 User is allowed to access it_project (View for "it_project" only)
Role "sec-incident-responsible":
 User is allowed to access it_int_prio (View for "it_int_prio" only)
 User is allowed to access it_issue (View for "it_issue" only)
 User is allowed to access it_project (View for "it_project" only)
Role "staff-report":
Role "summary_view":
Role "supportadmin":
 User is allowed to access adr_type (View for "adr_type" only)
 User is allowed to access adr_type_cat (View for "adr_type_cat" only)
 User is allowed to access analysis_result (View for "analysis_result" only)
 User is allowed to access contact (View for "contact" only)
 User is allowed to access customer (View for "customer" only)
 User is allowed to access customer_agreement (View for "customer_agreement" only)
 User is allowed to access mailgroup (View for "mailgroup" only)
 User is allowed to access return_type (View for "return_type" only)
 User is allowed to access sup_classification (View for "sup_classification" only)
 User is allowed to access support (View for "support" only)
 User is allowed to create adr_type (Create for "adr_type" only)
 User is allowed to create adr_type_cat (Create for "adr_type_cat" only)
 User is allowed to create analysis_result (Create for "analysis_result" only)
 User is allowed to create contact (Create for "contact" only)
 User is allowed to create customer (Create for "customer" only)
 User is allowed to create customer_agreement (Create for "customer_agreement" only)
 User is allowed to create mailgroup (Create for "mailgroup" only)
 User is allowed to create return_type (Create for "return_type" only)
 User is allowed to create sup_classification (Create for "sup_classification" only)
 User is allowed to create support (Create for "support" only)
 User is allowed to edit adr_type (Edit for "adr_type" only)
 User is allowed to edit adr_type_cat (Edit for "adr_type_cat" only)
 User is allowed to edit analysis_result (Edit for "analysis_result" only)
 User is allowed to edit contact (Edit for "contact" only)
 User is allowed to edit customer (Edit for "customer" only)
 User is allowed to edit customer_agreement (Edit for "customer_agreement" only)
 User is allowed to edit mailgroup (Edit for "mailgroup" only)
 User is allowed to edit return_type (Edit for "return_type" only)
 User is allowed to edit sup_classification (Edit for "sup_classification" only)
 User is allowed to edit support (Edit for "support" only)
Role "type":
 User is allowed to create adr_type (Create for "adr_type" only)
 User is allowed to create adr_type_cat (Create for "adr_type_cat" only)
 User is allowed to edit adr_type (Edit for "adr_type" only)
 User is allowed to edit adr_type_cat (Edit for "adr_type_cat" only)
Role "user":
  (Search for "time_project": ('activity', 'actor', 'cost_center', 'creation', 'creator', 'deputy', 'description', 'id', 'is_public_holiday', 'is_special_leave', 'is_vacation', 'name', 'op_project', 'organisation', 'overtime_reduction', 'product_family', 'project_type', 'reporting_group', 'responsible', 'status', 'work_location') only)
  (Search for "time_wp": ('activity', 'actor', 'cost_center', 'creation', 'creator', 'description', 'durations_allowed', 'has_expiration_date', 'id', 'name', 'project', 'responsible', 'time_end', 'time_start', 'time_wp_summary_no', 'travel', 'wp_no') only)
 User is allowed Edit on (Edit for "msg": ('keywords',) only)
 User is allowed Edit on file if file is linked from an item with Edit permission (Edit for "file" only)
 User is allowed Edit on issue if issue is non-confidential or user is on nosy list (Edit for "issue" only)
 User is allowed Edit on it_issue if it_issue is non-confidential or user is on nosy list (Edit for "it_issue": ('messages', 'files', 'nosy') only)
 User is allowed Edit on it_project if it_project is non-confidential or user is on nosy list (Edit for "it_project": ('messages', 'files', 'nosy') only)
 User is allowed Edit on support if support is non-confidential or user is on nosy list (Edit for "support": ('analysis_end', 'analysis_result', 'analysis_start', 'bcc', 'business_unit', 'category', 'cc', 'cc_emails', 'classification', 'closed', 'confidential', 'customer', 'emails', 'execution', 'external_ref', 'files', 'goods_received', 'goods_sent', 'lot', 'messages', 'nosy', 'number_effected', 'numeric_effort', 'prio', 'prodcat', 'product', 'related_issues', 'related_support', 'release', 'responsible', 'return_type', 'sap_ref', 'send_to_customer', 'serial_number', 'set_first_reply', 'status', 'superseder', 'title', 'type', 'warranty') only)
 User is allowed View on (View for "user": ('activity', 'actor', 'address', 'alternate_addresses', 'clearance_by', 'creation', 'creator', 'department', 'firstname', 'home_directory', 'id', 'job_description', 'lastname', 'login_shell', 'lunch_duration', 'lunch_start', 'nickname', 'pictures', 'position', 'queries', 'realname', 'room', 'samba_home_drive', 'samba_home_path', 'sex', 'status', 'subst_active', 'subst_until', 'substitute', 'supervisor', 'timezone', 'title', 'username') only)
 User is allowed View on (View for "user": ('activity', 'actor', 'address', 'alternate_addresses', 'clearance_by', 'creation', 'creator', 'department', 'firstname', 'home_directory', 'id', 'job_description', 'lastname', 'login_shell', 'lunch_duration', 'lunch_start', 'nickname', 'pictures', 'position', 'queries', 'realname', 'room', 'samba_home_drive', 'samba_home_path', 'sex', 'status', 'subst_active', 'substitute', 'supervisor', 'timezone', 'title', 'tt_lines', 'username') only)
 User is allowed View on file if file is linked from an item with View permission (View for "file" only)
 User is allowed View on issue if issue is non-confidential or user is on nosy list (View for "issue" only)
 User is allowed View on it_issue if it_issue is non-confidential or user is on nosy list (View for "it_issue" only)
 User is allowed View on it_project if it_project is non-confidential or user is on nosy list (View for "it_project" only)
 User is allowed View on msg if msg is linked from an item with View permission (View for "msg" only)
 User is allowed View on support if support is non-confidential or user is on nosy list (View for "support" only)
 User is allowed to access absence (View for "absence" only)
 User is allowed to access absence_type (View for "absence_type" only)
 User is allowed to access adr_type (View for "adr_type" only)
 User is allowed to access adr_type_cat (View for "adr_type_cat" only)
 User is allowed to access analysis_result (View for "analysis_result" only)
 User is allowed to access area (View for "area" only)
 User is allowed to access artefact (View for "artefact" only)
 User is allowed to access business_unit (View for "business_unit" only)
 User is allowed to access category (View for "category" only)
 User is allowed to access contact (View for "contact" only)
 User is allowed to access contact_type (View for "contact_type" only)
 User is allowed to access cost_center (View for "cost_center" only)
 User is allowed to access cost_center_group (View for "cost_center_group" only)
 User is allowed to access cost_center_status (View for "cost_center_status" only)
 User is allowed to access customer (View for "customer" only)
 User is allowed to access customer_agreement (View for "customer_agreement" only)
 User is allowed to access daily record if he is owner or supervisor (Edit for "daily_record": ('status', 'time_record') only)
 User is allowed to access daily record if he is owner or supervisor (View for "daily_record" only)
 User is allowed to access daily_record_status (View for "daily_record_status" only)
 User is allowed to access department (View for "department" only)
 User is allowed to access doc (View for "doc" only)
 User is allowed to access doc_issue_status (View for "doc_issue_status" only)
 User is allowed to access doc_status (View for "doc_status" only)
 User is allowed to access ext_tracker (View for "ext_tracker" only)
 User is allowed to access ext_tracker_state (View for "ext_tracker_state" only)
 User is allowed to access ext_tracker_type (View for "ext_tracker_type" only)
 User is allowed to access it_category (View for "it_category" only)
 User is allowed to access it_issue_status (View for "it_issue_status" only)
 User is allowed to access it_prio (View for "it_prio" only)
 User is allowed to access it_project_status (View for "it_project_status" only)
 User is allowed to access it_request_type (View for "it_request_type" only)
 User is allowed to access keyword (View for "keyword" only)
 User is allowed to access kind (View for "kind" only)
 User is allowed to access leave_status (View for "leave_status" only)
 User is allowed to access location (View for "location" only)
 User is allowed to access mailgroup (View for "mailgroup" only)
 User is allowed to access msg_keyword (View for "msg_keyword" only)
 User is allowed to access org_location (View for "org_location" only)
 User is allowed to access organisation (View for "organisation" only)
 User is allowed to access overtime_period (View for "overtime_period" only)
 User is allowed to access position (View for "position" only)
 User is allowed to access prodcat (View for "prodcat" only)
 User is allowed to access product (View for "product" only)
 User is allowed to access product_family (View for "product_family" only)
 User is allowed to access product_type (View for "product_type" only)
 User is allowed to access project_type (View for "project_type" only)
 User is allowed to access public_holiday (View for "public_holiday" only)
 User is allowed to access reference (View for "reference" only)
 User is allowed to access reporting_group (View for "reporting_group" only)
 User is allowed to access return_type (View for "return_type" only)
 User is allowed to access room (View for "room" only)
 User is allowed to access safety_level (View for "safety_level" only)
 User is allowed to access sap_cc (View for "sap_cc" only)
 User is allowed to access severity (View for "severity" only)
 User is allowed to access sex (View for "sex" only)
 User is allowed to access status (View for "status" only)
 User is allowed to access status_transition (View for "status_transition" only)
 User is allowed to access summary_report (View for "summary_report" only)
 User is allowed to access summary_type (View for "summary_type" only)
 User is allowed to access sup_classification (View for "sup_classification" only)
 User is allowed to access sup_execution (View for "sup_execution" only)
 User is allowed to access sup_prio (View for "sup_prio" only)
 User is allowed to access sup_status (View for "sup_status" only)
 User is allowed to access sup_type (View for "sup_type" only)
 User is allowed to access sup_warranty (View for "sup_warranty" only)
 User is allowed to access test_level (View for "test_level" only)
 User is allowed to access time_activity (View for "time_activity" only)
 User is allowed to access time_project_status (View for "time_project_status" only)
 User is allowed to access time_wp_group (View for "time_wp_group" only)
 User is allowed to access time_wp_summary_no (View for "time_wp_summary_no" only)
 User is allowed to access timesheet (View for "timesheet" only)
 User is allowed to access user_status (View for "user_status" only)
 User is allowed to access vacation_report (View for "vacation_report" only)
 User is allowed to access valid (View for "valid" only)
 User is allowed to access work_location (View for "work_location" only)
 User is allowed to create daily_record (Create for "daily_record" only)
 User is allowed to create doc (Create for "doc" only)
 User is allowed to create ext_tracker_state (Create for "ext_tracker_state" only)
 User is allowed to create file (Create for "file" only)
 User is allowed to create issue (Create for "issue" only)
 User is allowed to create it_issue (Create for "it_issue" only)
 User is allowed to create leave_submission (Create for "leave_submission" only)
 User is allowed to create msg (Create for "msg" only)
 User is allowed to create queries (Create for "query" only)
 User is allowed to create support (Create for "support" only)
 User is allowed to create time_record (Create for "time_record" only)
 User is allowed to create time_wp (Create for "time_wp" only)
 User is allowed to edit (some of) their own user details (Edit for "user": ('lunch_duration', 'lunch_start', 'password', 'queries', 'realname', 'room', 'subst_active', 'substitute', 'timezone', 'title', 'tt_lines') only)
 User is allowed to edit category if he is responsible for it (Edit for "category": ('nosy', 'default_part_of') only)
 User is allowed to edit doc (Edit for "doc" only)
 User is allowed to edit ext_tracker_state (Edit for "ext_tracker_state" only)
 User is allowed to edit several fields if he is Responsible for an it_issue (Edit for "it_issue": ('responsible',) only)
 User is allowed to edit several fields if he is Stakeholder/Responsible for an it_issue (Edit for "it_issue": ('deadline', 'status', 'title') only)
 User is allowed to edit their queries (Edit for "query" only)
 User is allowed to edit time category if the status is "Open" and he is responsible for the time category (Edit for "time_project": ('deputy', 'planned_effort', 'nosy') only)
 User is allowed to edit workpackage if he is time category owner (Edit for "time_wp": ('cost_center', 'is_public', 'name', 'responsible', 'time_wp_summary_no', 'wp_no') only)
 User is allowed to retire their queries (Retire for "query" only)
 User is allowed to search daily_record (Search for "daily_record" only)
 User is allowed to search for their own files (Search for "file" only)
 User is allowed to search for their own messages (Search for "msg" only)
 User is allowed to search for their queries (Search for "query" only)
 User is allowed to search issue (Search for "issue" only)
 User is allowed to search it_issue (Search for "it_issue" only)
 User is allowed to search it_project (Search for "it_project" only)
 User is allowed to search leave_submission (Search for "leave_submission" only)
 User is allowed to search support (Search for "support" only)
 User is allowed to search time_record (Search for "time_record" only)
 User is allowed to search time_wp (Search for "time_wp": ('activity', 'actor', 'cost_center', 'creation', 'creator', 'description', 'durations_allowed', 'has_expiration_date', 'id', 'name', 'project', 'responsible', 'time_end', 'time_start', 'time_wp_summary_no', 'travel', 'wp_no') only)
 User is allowed to see time record if he is allowed to see all details on work package or User may view a daily_record (and time_records that are attached to that daily_record) if the user owns the daily_record or has role 'HR' or 'Controlling', or the user is supervisor or substitute supervisor of the owner of the daily record (the supervisor relationship is transitive) or the user is the department manager of the owner of the daily record. If user has role HR-Org-Location and is in the same Org-Location as the record, it may also be seen (View for "time_record" only)
 User is allowed to view leave submission if he is the supervisor or the person to whom approvals are delegated (Edit for "leave_submission": ('status',) only)
 User is allowed to view leave submission if he is the supervisor or the person to whom approvals are delegated (View for "leave_submission" only)
 User is allowed to view selected fields if booking is allowed for at least one work package for this user (View for "time_project": ('activity', 'actor', 'cost_center', 'creation', 'creator', 'deputy', 'description', 'id', 'is_public_holiday', 'is_special_leave', 'is_vacation', 'name', 'op_project', 'organisation', 'overtime_reduction', 'product_family', 'project_type', 'reporting_group', 'responsible', 'status', 'work_location') only)
 User is allowed to view selected fields in work package if booking is allowed for this user (View for "time_wp": ('activity', 'actor', 'cost_center', 'creation', 'creator', 'description', 'durations_allowed', 'has_expiration_date', 'id', 'name', 'project', 'responsible', 'time_end', 'time_start', 'time_wp_summary_no', 'travel', 'wp_no') only)
 User is allowed to view their own files (View for "file" only)
 User is allowed to view their own messages (View for "msg" only)
 User is allowed to view their own overtime information (View for "overtime_correction" only)
 User is allowed to view time record if he is the supervisor or the person to whom approvals are delegated (View for "time_record" only)
 User is allowed to view work package and time category names if he/she is department manager or supervisor or has role HR or HR-Org-Location (View for "time_project": ('name', 'project') only)
 User is allowed to view work package and time category names if he/she is department manager or supervisor or has role HR or HR-Org-Location (View for "time_wp": ('name', 'project') only)
 User is allowed to view/edit workpackage if he is owner or project responsible/deputy (Edit for "time_wp": ('bookers', 'description', 'planned_effort', 'time_end', 'time_start', 'time_wp_summary_no') only)
 User may access the web interface (Web Access)
 User may edit own leave submissions (Edit for "leave_submission": ('comment', 'comment_cancel', 'first_day', 'last_day', 'status', 'time_wp', 'user') only)
 User may edit own leave submissions (View for "leave_submission": ('comment', 'comment_cancel', 'first_day', 'last_day', 'status', 'time_wp', 'user') only)
 User may edit own time_records (Edit for "time_record" only)
 User may edit own time_records (View for "time_record" only)
 User may use the email interface (Email Access)
 User may view a daily_record (and time_records that are attached to that daily_record) if the user owns the daily_record or has role 'HR' or 'Controlling', or the user is supervisor or substitute supervisor of the owner of the daily record (the supervisor relationship is transitive) or the user is the department manager of the owner of the daily record. If user has role HR-Org-Location and is in the same Org-Location as the record, it may also be seen (View for "daily_record" only)
 User may view time category if user is owner or deputy of time category or on nosy list of time category or if user is department manager of time category (View for "time_project" only)
 User may view work package if responsible for it, if user is owner or deputy of time category or on nosy list of time category or if user is department manager of time category (View for "time_wp" only)
 Users are allowed to view their own and public queries for classes where they have search permission (View for "query" only)
 Users may see daily record if they may see one of the time_records for that day (View for "daily_record" only)
""".strip ()
