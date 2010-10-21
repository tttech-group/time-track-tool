security = """
New Web users get the Role "User"
New Email users get the Role "User"
Role "abo":
 User is allowed to access abo (View for "abo" only)
 User is allowed to access abo_type (View for "abo_type" only)
 User is allowed to create abo (Create for "abo" only)
 User is allowed to create abo_type (Create for "abo_type" only)
 User is allowed to create letter (Create for "letter" only)
 User is allowed to create tmplate (Create for "tmplate" only)
 User is allowed to edit abo (Edit for "abo" only)
 User is allowed to edit abo_type (Edit for "abo_type" only)
 User is allowed to edit letter (Edit for "letter" only)
 User is allowed to edit tmplate (Edit for "tmplate" only)
Role "admin":
 User may access the web interface (Web Access)
 User may create everthing (Create)
 User may edit everthing (Edit)
 User may manipulate user Roles through the web (Web Roles)
 User may retire everthing (Retire)
 User may use the email interface (Email Access)
 User may view everthing (View)
Role "adr_readonly":
 User is allowed View on (View for "user": ('username', 'realname', 'phone') only)
 User is allowed to access address (View for "address" only)
 User is allowed to access adr_type (View for "adr_type" only)
 User is allowed to access adr_type_cat (View for "adr_type_cat" only)
 User is allowed to access contact (View for "contact" only)
 User is allowed to access contact_type (View for "contact_type" only)
 User is allowed to access file (View for "file" only)
 User is allowed to access msg (View for "msg" only)
 User is allowed to access opening_hours (View for "opening_hours" only)
 User is allowed to access valid (View for "valid" only)
 User is allowed to access weekday (View for "weekday" only)
 User is allowed to edit (some of) their own user details (Edit for "user": ('address', 'alternate_addresses', 'csv_delimiter', 'password', 'phone', 'queries', 'realname', 'timezone') only)
 User may access the web interface (Web Access)
Role "anonymous":
 User may access the web interface (Web Access)
Role "contact":
 User is allowed to access address (View for "address" only)
 User is allowed to access contact (View for "contact" only)
 User is allowed to access opening_hours (View for "opening_hours" only)
 User is allowed to access weekday (View for "weekday" only)
 User is allowed to create contact (Create for "contact" only)
 User is allowed to create opening_hours (Create for "opening_hours" only)
 User is allowed to edit contact (Edit for "contact" only)
 User is allowed to edit opening_hours (Edit for "opening_hours" only)
Role "invoice":
 User is allowed to access abo (View for "abo" only)
 User is allowed to access abo_type (View for "abo_type" only)
 User is allowed to access invoice (View for "invoice" only)
 User is allowed to access invoice_group (View for "invoice_group" only)
 User is allowed to access invoice_template (View for "invoice_template" only)
 User is allowed to access payment (View for "payment" only)
 User is allowed to create abo_type (Create for "abo_type" only)
 User is allowed to create invoice (Create for "invoice" only)
 User is allowed to create invoice_group (Create for "invoice_group" only)
 User is allowed to create invoice_template (Create for "invoice_template" only)
 User is allowed to create payment (Create for "payment" only)
 User is allowed to create tmplate (Create for "tmplate" only)
 User is allowed to edit abo_type (Edit for "abo_type" only)
 User is allowed to edit invoice (Edit for "invoice" only)
 User is allowed to edit invoice_group (Edit for "invoice_group" only)
 User is allowed to edit invoice_template (Edit for "invoice_template" only)
 User is allowed to edit payment (Edit for "payment" only)
 User is allowed to edit tmplate (Edit for "tmplate" only)
Role "letter":
 User is allowed to create letter (Create for "letter" only)
 User is allowed to create tmplate (Create for "tmplate" only)
 User is allowed to edit letter (Edit for "letter" only)
 User is allowed to edit tmplate (Edit for "tmplate" only)
Role "product":
 User is allowed to access abo (View for "abo" only)
 User is allowed to access abo_type (View for "abo_type" only)
 User is allowed to create abo_price (Create for "abo_price" only)
 User is allowed to create abo_type (Create for "abo_type" only)
 User is allowed to create currency (Create for "currency" only)
 User is allowed to edit abo_price (Edit for "abo_price" only)
 User is allowed to edit abo_type (Edit for "abo_type" only)
 User is allowed to edit currency (Edit for "currency" only)
Role "type":
 User is allowed to create adr_type (Create for "adr_type" only)
 User is allowed to create adr_type_cat (Create for "adr_type_cat" only)
 User is allowed to edit adr_type (Edit for "adr_type" only)
 User is allowed to edit adr_type_cat (Edit for "adr_type_cat" only)
Role "user":
 User is allowed Edit on file if file is linked from an item with Edit permission (Edit for "file" only)
 User is allowed View on (View for "user": ('activity', 'actor', 'address', 'alternate_addresses', 'clearance_by', 'creation', 'creator', 'department', 'external_phone', 'firstname', 'id', 'job_description', 'lastname', 'lunch_duration', 'lunch_start', 'nickname', 'password', 'phone', 'pictures', 'position', 'queries', 'realname', 'room', 'sex', 'status', 'subst_active', 'substitute', 'supervisor', 'timezone', 'title', 'username', 'home_directory', 'login_shell', 'samba_home_drive', 'samba_home_path') only)
 User is allowed View on file if file is linked from an item with View permission (View for "file" only)
 User is allowed View on msg if msg is linked from an item with View permission (View for "msg" only)
 User is allowed to access abo_price (View for "abo_price" only)
 User is allowed to access address (View for "address" only)
 User is allowed to access adr_type (View for "adr_type" only)
 User is allowed to access adr_type_cat (View for "adr_type_cat" only)
 User is allowed to access contact (View for "contact" only)
 User is allowed to access contact_type (View for "contact_type" only)
 User is allowed to access currency (View for "currency" only)
 User is allowed to access file (View for "file" only)
 User is allowed to access letter (View for "letter" only)
 User is allowed to access msg (View for "msg" only)
 User is allowed to access opening_hours (View for "opening_hours" only)
 User is allowed to access query (View for "query" only)
 User is allowed to access tmplate (View for "tmplate" only)
 User is allowed to access tmplate_status (View for "tmplate_status" only)
 User is allowed to access user_status (View for "user_status" only)
 User is allowed to access valid (View for "valid" only)
 User is allowed to access weekday (View for "weekday" only)
 User is allowed to create address (Create for "address" only)
 User is allowed to create file (Create for "file" only)
 User is allowed to create msg (Create for "msg" only)
 User is allowed to create opening_hours (Create for "opening_hours" only)
 User is allowed to create queries (Create for "query" only)
 User is allowed to create query (Create for "query" only)
 User is allowed to edit (some of) their own user details (Edit for "user": ('address', 'alternate_addresses', 'csv_delimiter', 'password', 'phone', 'queries', 'realname', 'timezone') only)
 User is allowed to edit address (Edit for "address" only)
 User is allowed to edit file (Edit for "file" only)
 User is allowed to edit msg (Edit for "msg" only)
 User is allowed to edit opening_hours (Edit for "opening_hours" only)
 User is allowed to edit query (Edit for "query" only)
 User is allowed to edit their queries (Edit for "query" only)
 User is allowed to retire their queries (Retire for "query" only)
 User is allowed to search for their own files (Search for "file" only)
 User is allowed to search for their own messages (Search for "msg" only)
 User is allowed to search for their queries (Search for "query" only)
 User is allowed to view their own and public queries (View for "query" only)
 User is allowed to view their own files (View for "file" only)
 User is allowed to view their own messages (View for "msg" only)
 User may access the web interface (Web Access)
 User may use the email interface (Email Access)
""".strip ()
