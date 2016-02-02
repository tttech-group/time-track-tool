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
Role "board":
Role "controlling":
 User is allowed to access query (View for "query" only)
 User is allowed to access time_project (View for "time_project" only)
 User is allowed to create organisation (Create for "organisation" only)
 User is allowed to create query (Create for "query" only)
 User is allowed to edit organisation (Edit for "organisation" only)
 User is allowed to edit query (Edit for "query" only)
Role "finance":
Role "hr":
Role "it-approval":
Role "nosy":
 User may get nosy messages for purchase_request (Nosy for "purchase_request" only)
Role "pgp":
Role "pr-view":
 User is allowed to access pr_approval (View for "pr_approval" only)
 User is allowed to access pr_offer_item (View for "pr_offer_item" only)
 User is allowed to access purchase_request (View for "purchase_request" only)
Role "procure-approval":
Role "procurement":
  (View for "sap_cc" only)
  (View for "time_project" only)
 User is allowed Edit on (Edit for "sap_cc": ('purchasing_agents',) only)
 User is allowed Edit on (Edit for "time_project": ('purchasing_agents',) only)
 User is allowed to access pr_approval (View for "pr_approval" only)
 User is allowed to access pr_approval_order (View for "pr_approval_order" only)
Role "procurement-admin":
  (Search for "user" only)
 User is allowed Edit on (Edit for "user": ('roles', 'password') only)
 User is allowed to access user (View for "user" only)
 User is allowed to create department (Create for "department" only)
 User is allowed to create pr_approval_order (Create for "pr_approval_order" only)
 User is allowed to create pr_currency (Create for "pr_currency" only)
 User is allowed to create pr_supplier_rating_by_org (Create for "pr_supplier_rating_by_org" only)
 User is allowed to create purchase_type (Create for "purchase_type" only)
 User is allowed to edit department (Edit for "department" only)
 User is allowed to edit pr_approval_order (Edit for "pr_approval_order" only)
 User is allowed to edit pr_currency (Edit for "pr_currency" only)
 User is allowed to edit pr_supplier_rating_by_org (Edit for "pr_supplier_rating_by_org" only)
 User is allowed to edit purchase_type (Edit for "purchase_type" only)
Role "project":
 User is allowed Edit on (Edit for "time_project": ('cost_center', 'deputy', 'description', 'department', 'name', 'nosy', 'organisation', 'responsible', 'status') only)
 User is allowed to access time_project (View for "time_project" only)
 User is allowed to create time_project (Create for "time_project" only)
 User is allowed to create time_project_status (Create for "time_project_status" only)
 User is allowed to edit time_project_status (Edit for "time_project_status" only)
Role "project_view":
 User is allowed to access time_project (View for "time_project" only)
Role "quality":
Role "subcontract":
Role "user":
  (Search for "pr_approval" only)
  (Search for "pr_offer_item" only)
  (Search for "purchase_request" only)
  (Search for "time_project": ('name', 'description', 'responsible', 'deputy', 'organisation', 'status', 'id', 'creation', 'creator', 'activity', 'actor') only)
 Allow setting add_to_las from 'None' for orphanes offer items (Edit for "pr_offer_item": ('add_to_las',) only)
 Approvers are allowed if not finance and PR not yet approved by finance (Edit for "pr_offer_item": ('vat',) only)
 Approvers are allowed if not finance and PR not yet approved by finance (Edit for "purchase_request": ('continuous_obligation', 'contract_term', 'termination_date') only)
 User is allowed Edit on file if file is linked from an item with Edit permission (Edit for "file" only)
 User is allowed View on (View for "user": ('realname', 'username', 'id') only)
 User is allowed View on file if file is linked from an item with View permission (View for "file" only)
 User is allowed View on msg if msg is linked from an item with View permission (View for "msg" only)
 User is allowed if on the nosy list (Edit for "purchase_request": ('files', 'messages', 'nosy') only)
 User is allowed if on the nosy list (View for "purchase_request" only)
 User is allowed if on the nosy list of the PR (View for "pr_approval" only)
 User is allowed if on the nosy list of the PR (View for "pr_offer_item" only)
 User is allowed permission on their own PRs if either creator or requester (Edit for "purchase_request": ('files', 'messages', 'nosy') only)
 User is allowed permission on their own PRs if either creator or requester (View for "purchase_request" only)
 User is allowed to access department (View for "department" only)
 User is allowed to access location (View for "location" only)
 User is allowed to access org_location (View for "org_location" only)
 User is allowed to access organisation (View for "organisation" only)
 User is allowed to access part_of_budget (View for "part_of_budget" only)
 User is allowed to access pr_approval_status (View for "pr_approval_status" only)
 User is allowed to access pr_currency (View for "pr_currency" only)
 User is allowed to access pr_status (View for "pr_status" only)
 User is allowed to access pr_supplier (View for "pr_supplier" only)
 User is allowed to access pr_supplier_rating (View for "pr_supplier_rating" only)
 User is allowed to access pr_supplier_rating_by_org (View for "pr_supplier_rating_by_org" only)
 User is allowed to access purchase_type (View for "purchase_type" only)
 User is allowed to access sap_cc (View for "sap_cc" only)
 User is allowed to access terms_conditions (View for "terms_conditions" only)
 User is allowed to access time_project (View for "time_project" only)
 User is allowed to access time_project_status (View for "time_project_status" only)
 User is allowed to access user_status (View for "user_status" only)
 User is allowed to cancel their own PR (Edit for "purchase_request": ('status', 'messages', 'nosy') only)
 User is allowed to change status of undecided approval if they are the owner/deputy or have appropriate role (Edit for "pr_approval": ('status', 'msg') only)
 User is allowed to create file (Create for "file" only)
 User is allowed to create msg (Create for "msg" only)
 User is allowed to create pr_offer_item (Create for "pr_offer_item" only)
 User is allowed to create purchase_request (Create for "purchase_request" only)
 User is allowed to create queries (Create for "query" only)
 User is allowed to edit (some of) their own user details (Edit for "user": ('csv_delimiter', 'password', 'queries', 'realname', 'timezone') only)
 User is allowed to edit their own PRs (creator or requester) while PR is open (Edit for "purchase_request" only)
 User is allowed to edit their queries (Edit for "query" only)
 User is allowed to reopen their own rejected PR (Edit for "purchase_request": ('messages', 'nosy', 'status') only)
 User is allowed to retire their queries (Retire for "query" only)
 User is allowed to search for their own files (Search for "file" only)
 User is allowed to search for their own messages (Search for "msg" only)
 User is allowed to search for their queries (Search for "query" only)
 User is allowed to view (some of) their own user details (View for "user": ('activity', 'address', 'alternate_addresses', 'creation', 'csv_delimiter', 'password', 'queries', 'realname', 'timezone') only)
 User is allowed to view their own files (View for "file" only)
 User is allowed to view their own messages (View for "msg" only)
 User may access the web interface (Web Access)
 User may use the email interface (Email Access)
 User may view time category if user is owner or deputy of time category or on nosy list of time category or if user is department manager of time category (View for "time_project" only)
 User with view role is allowed editing if status is 'approved' or 'ordered' (Edit for "purchase_request": ('files', 'messages', 'nosy', 'status') only)
 Users are allowed if an approval from them is linked to the PR (Edit for "purchase_request": ('files', 'messages', 'nosy') only)
 Users are allowed if an approval from them is linked to the PR (View for "purchase_request" only)
 Users are allowed if they have one of the view roles of the purchase type (Edit for "purchase_request": ('frame_purchase', 'frame_purchase_end', 'nosy', 'sap_reference', 'terms_conditions') only)
 Users are allowed if they have one of the view roles of the purchase type (View for "purchase_request" only)
 Users are allowed to edit if offer is linked from PR and PR is editable (Edit for "pr_offer_item" only)
 Users are allowed to edit message if a pending approval from them is linked to the PR (Edit for "purchase_request": ('files', 'messages', 'nosy') only)
 Users are allowed to view if approval is linked to viewable PR (View for "pr_approval" only)
 Users are allowed to view if offer is linked from PR (View for "pr_offer_item" only)
 Users are allowed to view if they have one of the view roles of the purchase type (Edit for "pr_offer_item": ('add_to_las', 'is_asset', 'pr_supplier', 'supplier') only)
 Users are allowed to view if they have one of the view roles of the purchase type (View for "pr_offer_item" only)
 Users are allowed to view their own and public queries for classes where they have search permission (View for "query" only)
Role "user_view":
 User is allowed to access user (View for "user" only)
""".strip ()
