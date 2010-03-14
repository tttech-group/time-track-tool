security = """
New Web users get the Roles "User,Nosy"
New Email users get the Role "User"
Role "admin":
 User may create everthing (Create)
 User may edit everthing (Edit)
 User may retire everthing (Retire)
 User may view everthing (View)
 User may access the web interface (Web Access)
 User may manipulate user Roles through the web (Web Roles)
 User may use the email interface (Email Access)
Role "adr_readonly":
 User is allowed to access adr_type (View for "adr_type" only)
 User is allowed to access adr_type_cat (View for "adr_type_cat" only)
 User is allowed to access valid (View for "valid" only)
 User is allowed to access contact_type (View for "contact_type" only)
 User is allowed to access contact (View for "contact" only)
 User is allowed to access address (View for "address" only)
 User may access the web interface (Web Access)
 User is allowed to access file (View for "file" only)
 User is allowed to access msg (View for "msg" only)
 User is allowed to access address (View for "address" only)
 User is allowed to access contact (View for "contact" only)
 User is allowed to access weekday (View for "weekday" only)
 User is allowed to access opening_hours (View for "opening_hours" only)
 User is allowed View on (View for "user": ('username', 'realname', 'phone') only)
 User is allowed to edit (some of) their own user details (Edit for "user": ('password', 'phone', 'csv_delimiter', 'timezone', 'address', 'alternate_addresses') only)
 User is allowed to view (some of) their own user details (View for "user": ('username', 'realname') only)
Role "anonymous":
 User may access the web interface (Web Access)
Role "contact":
 User is allowed to edit contact (Edit for "contact" only)
 User is allowed to create contact (Create for "contact" only)
 User is allowed to edit opening_hours (Edit for "opening_hours" only)
 User is allowed to create opening_hours (Create for "opening_hours" only)
 User is allowed to access address (View for "address" only)
 User is allowed to access contact (View for "contact" only)
 User is allowed to edit contact (Edit for "contact" only)
 User is allowed to create contact (Create for "contact" only)
 User is allowed to access weekday (View for "weekday" only)
 User is allowed to access opening_hours (View for "opening_hours" only)
Role "it":
 User is allowed to edit it_category (Edit for "it_category" only)
 User is allowed to create it_category (Create for "it_category" only)
 User is allowed to access it_issue (View for "it_issue" only)
 User is allowed to edit it_issue (Edit for "it_issue" only)
 User is allowed to create it_issue (Create for "it_issue" only)
 User is allowed to access it_project (View for "it_project" only)
 User is allowed to edit it_project (Edit for "it_project" only)
 User is allowed to create it_project (Create for "it_project" only)
 User is allowed Edit on (Edit for "location": ('domain_part',) only)
 User is allowed Edit on (Edit for "org_location": ('smb_domain', 'dhcp_server', 'domino_dn') only)
 User is allowed Edit on (Edit for "organisation": ('domain_part',) only)
 User is allowed Edit on (Edit for "user": ('address', 'alternate_addresses', 'nickname', 'password', 'timezone', 'username', 'is_lotus_user', 'sync_with_ldap', 'group', 'secondary_groups', 'uid', 'home_directory', 'login_shell', 'samba_home_drive', 'samba_home_path', 'samba_kickoff_time', 'samba_lm_password', 'samba_logon_script', 'samba_nt_password', 'samba_profile_path', 'samba_pwd_can_change', 'samba_pwd_last_set', 'samba_pwd_must_change', 'user_password', 'shadow_last_change', 'shadow_min', 'shadow_max', 'shadow_warning', 'shadow_inactive', 'shadow_expire', 'shadow_used') only)
 User is allowed Edit on msg if msg is linked from an item with Edit permission (Edit for "msg" only)
Role "itview":
 User is allowed to access it_issue (View for "it_issue" only)
 User is allowed to access it_project (View for "it_project" only)
Role "letter":
 User is allowed to edit tmplate (Edit for "tmplate" only)
 User is allowed to create tmplate (Create for "tmplate" only)
Role "nosy":
 User may get nosy messages for it_issue (Nosy for "it_issue" only)
 User may get nosy messages for it_project (Nosy for "it_project" only)
Role "type":
 User is allowed to edit adr_type (Edit for "adr_type" only)
 User is allowed to create adr_type (Create for "adr_type" only)
 User is allowed to edit adr_type_cat (Edit for "adr_type_cat" only)
 User is allowed to create adr_type_cat (Create for "adr_type_cat" only)
Role "user":
 User is allowed to access it_category (View for "it_category" only)
 User is allowed to access it_issue_status (View for "it_issue_status" only)
 User is allowed to access it_prio (View for "it_prio" only)
 User is allowed to access it_project_status (View for "it_project_status" only)
 User is allowed View on (View for "user": ('activity', 'actor', 'address', 'alternate_addresses', 'clearance_by', 'creation', 'creator', 'department', 'external_phone', 'firstname', 'job_description', 'lastname', 'lunch_duration', 'lunch_start', 'nickname', 'password', 'phone', 'pictures', 'position', 'queries', 'realname', 'room', 'sex', 'status', 'subst_active', 'substitute', 'supervisor', 'timezone', 'title', 'username', 'home_directory', 'login_shell', 'samba_home_drive', 'samba_home_path') only)
 User is allowed to edit several fields if he is Stakeholder/Responsible for an it_issue (Edit for "it_issue": ('deadline', 'responsible', 'status', 'title') only)
 User is allowed to create it_issue (Create for "it_issue" only)
 User is allowed View on it_issue if it_issue is non-confidential or user is on nosy list (View for "it_issue" only)
 User is allowed Edit on it_issue if it_issue is non-confidential or user is on nosy list (Edit for "it_issue": ('messages', 'files', 'nosy') only)
 User is allowed View on it_project if it_project is non-confidential or user is on nosy list (View for "it_project" only)
 User is allowed Edit on it_project if it_project is non-confidential or user is on nosy list (Edit for "it_project": ('messages', 'files', 'nosy') only)
 User is allowed to access adr_type (View for "adr_type" only)
 User is allowed to access adr_type_cat (View for "adr_type_cat" only)
 User is allowed to access tmplate (View for "tmplate" only)
 User is allowed to access valid (View for "valid" only)
 User is allowed to access contact_type (View for "contact_type" only)
 User is allowed to access contact (View for "contact" only)
 User is allowed to access tmplate_status (View for "tmplate_status" only)
 User is allowed to access opening_hours (View for "opening_hours" only)
 User is allowed to access weekday (View for "weekday" only)
 User is allowed to access file (View for "file" only)
 User is allowed to edit file (Edit for "file" only)
 User is allowed to create file (Create for "file" only)
 User is allowed to access msg (View for "msg" only)
 User is allowed to edit msg (Edit for "msg" only)
 User is allowed to create msg (Create for "msg" only)
 User is allowed to access address (View for "address" only)
 User is allowed to edit address (Edit for "address" only)
 User is allowed to create address (Create for "address" only)
 User is allowed to access contact (View for "contact" only)
 User is allowed to access weekday (View for "weekday" only)
 User is allowed to access opening_hours (View for "opening_hours" only)
 User is allowed to edit opening_hours (Edit for "opening_hours" only)
 User is allowed to create opening_hours (Create for "opening_hours" only)
 User is allowed View on (View for "user": ('activity', 'actor', 'address', 'alternate_addresses', 'clearance_by', 'creation', 'creator', 'department', 'external_phone', 'firstname', 'job_description', 'lastname', 'lunch_duration', 'lunch_start', 'nickname', 'password', 'phone', 'pictures', 'position', 'queries', 'realname', 'room', 'sex', 'status', 'subst_active', 'substitute', 'supervisor', 'timezone', 'title', 'username', 'home_directory', 'login_shell', 'samba_home_drive', 'samba_home_path') only)
 User is allowed to edit (some of) their own user details (Edit for "user": ('password', 'phone', 'csv_delimiter', 'timezone', 'address', 'alternate_addresses') only)
 User is allowed to view (some of) their own user details (View for "user": ('username', 'realname') only)
 User is allowed to access user_status (View for "user_status" only)
 User is allowed to create file (Create for "file" only)
 User is allowed to create msg (Create for "msg" only)
 User is allowed to view their own messages (View for "msg" only)
 User is allowed to view their own files (View for "file" only)
 User is allowed View on file if file is linked from an item with View permission (View for "file" only)
 User is allowed Edit on file if file is linked from an item with Edit permission (Edit for "file" only)
 User is allowed View on msg if msg is linked from an item with View permission (View for "msg" only)
 User is allowed to view their own and public queries (View for "query" only)
 User is allowed to edit their queries (Edit for "query" only)
 User is allowed to retire their queries (Retire for "query" only)
 User is allowed to create queries (Create for "query" only)
 User may access the web interface (Web Access)
 User may use the email interface (Email Access)
""".strip ()
