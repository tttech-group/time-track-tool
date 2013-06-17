security = """
New Web users get the Roles "User,Nosy"
New Email users get the Roles "User,Nosy"
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
Role "issue_admin":
 User is allowed Edit on msg if msg is linked from an item with Edit permission (Edit for "msg" only)
 User is allowed to access issue (View for "issue" only)
 User is allowed to create area (Create for "area" only)
 User is allowed to create category (Create for "category" only)
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
 User is allowed to edit issue (Edit for "issue" only)
 User is allowed to edit keyword (Edit for "keyword" only)
 User is allowed to edit kind (Edit for "kind" only)
 User is allowed to edit msg_keyword (Edit for "msg_keyword" only)
 User is allowed to edit prodcat (Edit for "prodcat" only)
 User is allowed to edit severity (Edit for "severity" only)
 User is allowed to edit status (Edit for "status" only)
 User is allowed to edit status_transition (Edit for "status_transition" only)
Role "nosy":
 User may get nosy messages for issue (Nosy for "issue" only)
Role "user":
 User is allowed Edit on file if file is linked from an item with Edit permission (Edit for "file" only)
 User is allowed Edit on issue if issue is non-confidential or user is on nosy list (Edit for "issue" only)
 User is allowed View on (View for "user": ('username', 'realname', 'id', 'creation', 'creator', 'activity', 'actor') only)
 User is allowed View on file if file is linked from an item with View permission (View for "file" only)
 User is allowed View on issue if issue is non-confidential or user is on nosy list (View for "issue" only)
 User is allowed View on msg if msg is linked from an item with View permission (View for "msg" only)
 User is allowed to access area (View for "area" only)
 User is allowed to access category (View for "category" only)
 User is allowed to access keyword (View for "keyword" only)
 User is allowed to access kind (View for "kind" only)
 User is allowed to access msg_keyword (View for "msg_keyword" only)
 User is allowed to access prodcat (View for "prodcat" only)
 User is allowed to access severity (View for "severity" only)
 User is allowed to access status (View for "status" only)
 User is allowed to access status_transition (View for "status_transition" only)
 User is allowed to access user_status (View for "user_status" only)
 User is allowed to create file (Create for "file" only)
 User is allowed to create issue (Create for "issue" only)
 User is allowed to create msg (Create for "msg" only)
 User is allowed to create queries (Create for "query" only)
 User is allowed to edit (some of) their own user details (Edit for "user": ('address', 'alternate_addresses', 'password', 'queries', 'realname', 'timezone') only)
 User is allowed to edit category if he is responsible for it (Edit for "category": ('nosy', 'default_part_of') only)
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
""".strip ()
