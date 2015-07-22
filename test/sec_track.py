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
Role "external":
  (Search for "user": ('id', 'nickname', 'username') only)
 External users are allowed to access issue if they are on the list of allowed external users or there is a transitive permission via containers (Edit for "issue": ['activity', 'actor', 'area', 'category', 'closed', 'composed_of', 'creation', 'creator', 'cur_est_begin', 'cur_est_end', 'deadline', 'depends', 'doc_issue_status', 'earliest_start', 'effective_prio', 'ext_attributes', 'ext_id', 'ext_status', 'ext_tracker', 'files', 'files_affected', 'fixed_in', 'id', 'keywords', 'kind', 'maturity_index', 'messages', 'needs', 'nosy', 'numeric_effort', 'part_of', 'planned_begin', 'planned_end', 'priority', 'release', 'responsible', 'severity', 'status', 'superseder', 'title'] only)
 External users are allowed to access issue if they are on the list of allowed external users or there is a transitive permission via containers (View for "issue": ['activity', 'actor', 'area', 'category', 'closed', 'composed_of', 'creation', 'creator', 'cur_est_begin', 'cur_est_end', 'deadline', 'depends', 'doc_issue_status', 'earliest_start', 'effective_prio', 'ext_attributes', 'ext_id', 'ext_status', 'ext_tracker', 'files', 'files_affected', 'fixed_in', 'id', 'keywords', 'kind', 'maturity_index', 'messages', 'needs', 'nosy', 'numeric_effort', 'part_of', 'planned_begin', 'planned_end', 'priority', 'release', 'responsible', 'severity', 'status', 'superseder', 'title'] only)
 User is allowed Edit on file if file is linked from an item with Edit permission (Edit for "file" only)
 User is allowed View on (View for "category": ('name',) only)
 User is allowed View on (View for "user": ('nickname', 'status', 'username') only)
 User is allowed View on (View for "user_status": ('name',) only)
 User is allowed View on file if file is linked from an item with View permission (View for "file" only)
 User is allowed View on msg if msg is linked from an item with View permission (View for "msg" only)
 User is allowed to access area (View for "area" only)
 User is allowed to access doc_issue_status (View for "doc_issue_status" only)
 User is allowed to access ext_tracker (View for "ext_tracker" only)
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
Role "issue_admin":
 User is allowed Edit on msg if msg is linked from an item with Edit permission (Edit for "msg" only)
 User is allowed to access issue (View for "issue" only)
 User is allowed to access query (View for "query" only)
 User is allowed to create area (Create for "area" only)
 User is allowed to create category (Create for "category" only)
 User is allowed to create doc_issue_status (Create for "doc_issue_status" only)
 User is allowed to create ext_tracker (Create for "ext_tracker" only)
 User is allowed to create issue (Create for "issue" only)
 User is allowed to create keyword (Create for "keyword" only)
 User is allowed to create kind (Create for "kind" only)
 User is allowed to create msg_keyword (Create for "msg_keyword" only)
 User is allowed to create query (Create for "query" only)
 User is allowed to create severity (Create for "severity" only)
 User is allowed to create status (Create for "status" only)
 User is allowed to create status_transition (Create for "status_transition" only)
 User is allowed to edit area (Edit for "area" only)
 User is allowed to edit category (Edit for "category" only)
 User is allowed to edit doc_issue_status (Edit for "doc_issue_status" only)
 User is allowed to edit ext_tracker (Edit for "ext_tracker" only)
 User is allowed to edit issue (Edit for "issue" only)
 User is allowed to edit keyword (Edit for "keyword" only)
 User is allowed to edit kind (Edit for "kind" only)
 User is allowed to edit msg_keyword (Edit for "msg_keyword" only)
 User is allowed to edit query (Edit for "query" only)
 User is allowed to edit severity (Edit for "severity" only)
 User is allowed to edit status (Edit for "status" only)
 User is allowed to edit status_transition (Edit for "status_transition" only)
Role "it":
 User is allowed Edit on (Edit for "location": ('domain_part',) only)
 User is allowed Edit on (Edit for "org_location": ('dhcp_server', 'domino_dn', 'smb_domain') only)
 User is allowed Edit on (Edit for "organisation": ('domain_part',) only)
 User is allowed Edit on (Edit for "user": ('address', 'alternate_addresses', 'nickname', 'password', 'timezone', 'username', 'is_lotus_user', 'sync_with_ldap', 'group', 'secondary_groups', 'uid', 'home_directory', 'login_shell', 'samba_home_drive', 'samba_home_path', 'samba_kickoff_time', 'samba_lm_password', 'samba_logon_script', 'samba_nt_password', 'samba_profile_path', 'samba_pwd_can_change', 'samba_pwd_last_set', 'samba_pwd_must_change', 'user_password', 'shadow_last_change', 'shadow_min', 'shadow_max', 'shadow_warning', 'shadow_inactive', 'shadow_expire', 'shadow_used') only)
 User is allowed Edit on (Edit for "user": ('address', 'alternate_addresses', 'nickname', 'password', 'timezone', 'username') only)
 User is allowed Edit on (Edit for "user": ('firstname', 'lastname', 'realname', 'roles', 'status') only)
 User is allowed Edit on msg if msg is linked from an item with Edit permission (Edit for "msg" only)
 User is allowed View on (View for "user": ('roles',) only)
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
Role "msgsync":
  (Search for "msg": ('date', 'id') only)
 User is allowed Edit on (Edit for "msg": ('author', 'date', 'id', 'keywords', 'subject', 'summary') only)
 User is allowed to access ext_msg (View for "ext_msg" only)
 User is allowed to create ext_msg (Create for "ext_msg" only)
 User is allowed to edit ext_msg (Edit for "ext_msg" only)
Role "nosy":
 User may get nosy messages for issue (Nosy for "issue" only)
 User may get nosy messages for it_issue (Nosy for "it_issue" only)
 User may get nosy messages for it_project (Nosy for "it_project" only)
 User may get nosy messages for support (Nosy for "support" only)
Role "pgp":
Role "supportadmin":
 User is allowed to access analysis_result (View for "analysis_result" only)
 User is allowed to access contact (View for "contact" only)
 User is allowed to access customer (View for "customer" only)
 User is allowed to access customer_agreement (View for "customer_agreement" only)
 User is allowed to access mailgroup (View for "mailgroup" only)
 User is allowed to access return_type (View for "return_type" only)
 User is allowed to access sup_classification (View for "sup_classification" only)
 User is allowed to access support (View for "support" only)
 User is allowed to create analysis_result (Create for "analysis_result" only)
 User is allowed to create contact (Create for "contact" only)
 User is allowed to create contact_type (Create for "contact_type" only)
 User is allowed to create customer (Create for "customer" only)
 User is allowed to create customer_agreement (Create for "customer_agreement" only)
 User is allowed to create mailgroup (Create for "mailgroup" only)
 User is allowed to create return_type (Create for "return_type" only)
 User is allowed to create sup_classification (Create for "sup_classification" only)
 User is allowed to create support (Create for "support" only)
 User is allowed to edit analysis_result (Edit for "analysis_result" only)
 User is allowed to edit contact (Edit for "contact" only)
 User is allowed to edit contact_type (Edit for "contact_type" only)
 User is allowed to edit customer (Edit for "customer" only)
 User is allowed to edit customer_agreement (Edit for "customer_agreement" only)
 User is allowed to edit mailgroup (Edit for "mailgroup" only)
 User is allowed to edit return_type (Edit for "return_type" only)
 User is allowed to edit sup_classification (Edit for "sup_classification" only)
 User is allowed to edit support (Edit for "support" only)
Role "user":
  (Search for "user": ('realname',) only)
 User is allowed Edit on (Edit for "msg": ('keywords',) only)
 User is allowed Edit on file if file is linked from an item with Edit permission (Edit for "file" only)
 User is allowed Edit on issue if issue is non-confidential or user is on nosy list (Edit for "issue" only)
 User is allowed Edit on it_issue if it_issue is non-confidential or user is on nosy list (Edit for "it_issue": ('messages', 'files', 'nosy') only)
 User is allowed Edit on it_project if it_project is non-confidential or user is on nosy list (Edit for "it_project": ('messages', 'files', 'nosy') only)
 User is allowed Edit on support if support is non-confidential or user is on nosy list (Edit for "support" only)
 User is allowed View on (View for "user": ('activity', 'actor', 'address', 'alternate_addresses', 'clearance_by', 'creation', 'creator', 'department', 'firstname', 'home_directory', 'id', 'job_description', 'lastname', 'login_shell', 'lunch_duration', 'lunch_start', 'nickname', 'pictures', 'position', 'queries', 'realname', 'room', 'samba_home_drive', 'samba_home_path', 'sex', 'status', 'subst_active', 'substitute', 'supervisor', 'timezone', 'title', 'username') only)
 User is allowed View on (View for "user": ('activity', 'actor', 'address', 'alternate_addresses', 'creation', 'creator', 'firstname', 'id', 'lastname', 'nickname', 'realname', 'status', 'timezone', 'title', 'username') only)
 User is allowed View on file if file is linked from an item with View permission (View for "file" only)
 User is allowed View on issue if issue is non-confidential or user is on nosy list (View for "issue" only)
 User is allowed View on it_issue if it_issue is non-confidential or user is on nosy list (View for "it_issue" only)
 User is allowed View on it_project if it_project is non-confidential or user is on nosy list (View for "it_project" only)
 User is allowed View on msg if msg is linked from an item with View permission (View for "msg" only)
 User is allowed View on support if support is non-confidential or user is on nosy list (View for "support" only)
 User is allowed to access analysis_result (View for "analysis_result" only)
 User is allowed to access area (View for "area" only)
 User is allowed to access business_unit (View for "business_unit" only)
 User is allowed to access category (View for "category" only)
 User is allowed to access contact (View for "contact" only)
 User is allowed to access contact_type (View for "contact_type" only)
 User is allowed to access customer (View for "customer" only)
 User is allowed to access customer_agreement (View for "customer_agreement" only)
 User is allowed to access doc_issue_status (View for "doc_issue_status" only)
 User is allowed to access ext_tracker (View for "ext_tracker" only)
 User is allowed to access it_category (View for "it_category" only)
 User is allowed to access it_issue_status (View for "it_issue_status" only)
 User is allowed to access it_prio (View for "it_prio" only)
 User is allowed to access it_project_status (View for "it_project_status" only)
 User is allowed to access it_request_type (View for "it_request_type" only)
 User is allowed to access keyword (View for "keyword" only)
 User is allowed to access kind (View for "kind" only)
 User is allowed to access mailgroup (View for "mailgroup" only)
 User is allowed to access msg_keyword (View for "msg_keyword" only)
 User is allowed to access prodcat (View for "prodcat" only)
 User is allowed to access product (View for "product" only)
 User is allowed to access return_type (View for "return_type" only)
 User is allowed to access severity (View for "severity" only)
 User is allowed to access status (View for "status" only)
 User is allowed to access status_transition (View for "status_transition" only)
 User is allowed to access sup_classification (View for "sup_classification" only)
 User is allowed to access sup_execution (View for "sup_execution" only)
 User is allowed to access sup_prio (View for "sup_prio" only)
 User is allowed to access sup_status (View for "sup_status" only)
 User is allowed to access sup_type (View for "sup_type" only)
 User is allowed to access user_status (View for "user_status" only)
 User is allowed to create file (Create for "file" only)
 User is allowed to create issue (Create for "issue" only)
 User is allowed to create it_issue (Create for "it_issue" only)
 User is allowed to create msg (Create for "msg" only)
 User is allowed to create queries (Create for "query" only)
 User is allowed to create support (Create for "support" only)
 User is allowed to edit (some of) their own user details (Edit for "user": ('csv_delimiter', 'password', 'queries', 'realname', 'timezone') only)
 User is allowed to edit category if he is responsible for it (Edit for "category": ('nosy', 'default_part_of') only)
 User is allowed to edit several fields if he is Stakeholder/Responsible for an it_issue (Edit for "it_issue": ('deadline', 'responsible', 'status', 'title') only)
 User is allowed to edit their queries (Edit for "query" only)
 User is allowed to retire their queries (Retire for "query" only)
 User is allowed to search for their own files (Search for "file" only)
 User is allowed to search for their own messages (Search for "msg" only)
 User is allowed to search for their queries (Search for "query" only)
 User is allowed to view their own files (View for "file" only)
 User is allowed to view their own messages (View for "msg" only)
 User may access the web interface (Web Access)
 User may use the email interface (Email Access)
 Users are allowed to view their own and public queries for classes where they have search permission (View for "query" only)
 search issue (Search for "issue" only)
 search it_issue (Search for "it_issue" only)
 search it_project (Search for "it_project" only)
 search support (Search for "support" only)
""".strip ()
