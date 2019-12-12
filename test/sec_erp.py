security = """
New Web users get the Role "User"
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
Role "adr_readonly":
 User is allowed to access address (View for "address" only)
 User is allowed to access adr_type (View for "adr_type" only)
 User is allowed to access adr_type_cat (View for "adr_type_cat" only)
 User is allowed to access contact (View for "contact" only)
 User is allowed to access contact_type (View for "contact_type" only)
 User is allowed to access valid (View for "valid" only)
 User may access the web interface (Web Access)
Role "anonymous":
 User may access the web interface (Web Access)
Role "contact":
 User is allowed to create address (Create for "address" only)
 User is allowed to create bank_account (Create for "bank_account" only)
 User is allowed to create contact (Create for "contact" only)
 User is allowed to create cust_supp (Create for "cust_supp" only)
 User is allowed to create opening_hours (Create for "opening_hours" only)
 User is allowed to edit address (Edit for "address" only)
 User is allowed to edit bank_account (Edit for "bank_account" only)
 User is allowed to edit contact (Edit for "contact" only)
 User is allowed to edit cust_supp (Edit for "cust_supp" only)
 User is allowed to edit opening_hours (Edit for "opening_hours" only)
Role "discount":
 User is allowed to create discount_group (Create for "discount_group" only)
 User is allowed to create group_discount (Create for "group_discount" only)
 User is allowed to create overall_discount (Create for "overall_discount" only)
 User is allowed to edit discount_group (Edit for "discount_group" only)
 User is allowed to edit group_discount (Edit for "group_discount" only)
 User is allowed to edit overall_discount (Edit for "overall_discount" only)
Role "invoice":
 User is allowed to access invoice_template (View for "invoice_template" only)
 User is allowed to access payment (View for "payment" only)
 User is allowed to create invoice_template (Create for "invoice_template" only)
 User is allowed to create payment (Create for "payment" only)
 User is allowed to edit invoice_template (Edit for "invoice_template" only)
 User is allowed to edit payment (Edit for "payment" only)
Role "letter":
 User is allowed to create letter (Create for "letter" only)
 User is allowed to create tmplate (Create for "tmplate" only)
 User is allowed to edit letter (Edit for "letter" only)
 User is allowed to edit tmplate (Edit for "tmplate" only)
Role "product":
 User is allowed to create product (Create for "product" only)
 User is allowed to create product_group (Create for "product_group" only)
 User is allowed to edit product (Edit for "product" only)
 User is allowed to edit product_group (Edit for "product_group" only)
Role "type":
 User is allowed to create adr_type (Create for "adr_type" only)
 User is allowed to create adr_type_cat (Create for "adr_type_cat" only)
 User is allowed to edit adr_type (Edit for "adr_type" only)
 User is allowed to edit adr_type_cat (Edit for "adr_type_cat" only)
Role "user":
 User is allowed Edit on file if file is linked from an item with Edit permission (Edit for "file" only)
 User is allowed View on file if file is linked from an item with View permission (View for "file" only)
 User is allowed View on msg if msg is linked from an item with View permission (View for "msg" only)
 User is allowed to access address (View for "address" only)
 User is allowed to access adr_type (View for "adr_type" only)
 User is allowed to access adr_type_cat (View for "adr_type_cat" only)
 User is allowed to access bank_account (View for "bank_account" only)
 User is allowed to access contact (View for "contact" only)
 User is allowed to access contact_type (View for "contact_type" only)
 User is allowed to access currency (View for "currency" only)
 User is allowed to access cust_supp (View for "cust_supp" only)
 User is allowed to access customer_group (View for "customer_group" only)
 User is allowed to access customer_status (View for "customer_status" only)
 User is allowed to access customer_type (View for "customer_type" only)
 User is allowed to access discount_group (View for "discount_group" only)
 User is allowed to access dispatch_type (View for "dispatch_type" only)
 User is allowed to access group_discount (View for "group_discount" only)
 User is allowed to access invoice_dispatch (View for "invoice_dispatch" only)
 User is allowed to access letter (View for "letter" only)
 User is allowed to access measuring_unit (View for "measuring_unit" only)
 User is allowed to access opening_hours (View for "opening_hours" only)
 User is allowed to access overall_discount (View for "overall_discount" only)
 User is allowed to access packaging_unit (View for "packaging_unit" only)
 User is allowed to access person (View for "person" only)
 User is allowed to access person_type (View for "person_type" only)
 User is allowed to access pharma_ref (View for "pharma_ref" only)
 User is allowed to access proceeds_group (View for "proceeds_group" only)
 User is allowed to access product (View for "product" only)
 User is allowed to access product_group (View for "product_group" only)
 User is allowed to access product_status (View for "product_status" only)
 User is allowed to access sales_conditions (View for "sales_conditions" only)
 User is allowed to access shelf_life_code (View for "shelf_life_code" only)
 User is allowed to access tmplate (View for "tmplate" only)
 User is allowed to access tmplate_status (View for "tmplate_status" only)
 User is allowed to access user (View for "user" only)
 User is allowed to access user_status (View for "user_status" only)
 User is allowed to access valid (View for "valid" only)
 User is allowed to access weekday (View for "weekday" only)
 User is allowed to create file (Create for "file" only)
 User is allowed to create msg (Create for "msg" only)
 User is allowed to create person (Create for "person" only)
 User is allowed to create person_type (Create for "person_type" only)
 User is allowed to create queries (Create for "query" only)
 User is allowed to edit (some of) their own user details (Edit for "user": ('password', 'queries', 'realname', 'timezone') only)
 User is allowed to edit person (Edit for "person" only)
 User is allowed to edit person_type (Edit for "person_type" only)
 User is allowed to edit their queries (Edit for "query" only)
 User is allowed to retire their queries (Retire for "query" only)
 User is allowed to search for their own files (Search for "file" only)
 User is allowed to search for their own messages (Search for "msg" only)
 User is allowed to search for their queries (Search for "query" only)
 User is allowed to view their own files (View for "file" only)
 User is allowed to view their own messages (View for "msg" only)
 User may access the rest interface (Rest Access)
 User may access the web interface (Web Access)
 User may access the xmlrpc interface (Xmlrpc Access)
 User may use the email interface (Email Access)
 Users are allowed to view their own and public queries for classes where they have search permission (View for "query" only)
""".strip ()
