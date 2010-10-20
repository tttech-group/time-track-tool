properties = \
    [ ( 'address'
      , [ ( 'adr_type'
          , ["admin", "adr_readonly", "contact", "user"]
          )
        , ( 'affix'
          , ["admin", "adr_readonly", "contact", "user"]
          )
        , ( 'birthdate'
          , ["admin", "adr_readonly", "contact", "user"]
          )
        , ( 'city'
          , ["admin", "adr_readonly", "contact", "user"]
          )
        , ( 'contacts'
          , ["admin", "adr_readonly", "contact", "user"]
          )
        , ( 'country'
          , ["admin", "adr_readonly", "contact", "user"]
          )
        , ( 'files'
          , ["admin", "adr_readonly", "contact", "user"]
          )
        , ( 'firstname'
          , ["admin", "adr_readonly", "contact", "user"]
          )
        , ( 'function'
          , ["admin", "adr_readonly", "contact", "user"]
          )
        , ( 'initial'
          , ["admin", "adr_readonly", "contact", "user"]
          )
        , ( 'lastname'
          , ["admin", "adr_readonly", "contact", "user"]
          )
        , ( 'letters'
          , ["admin", "adr_readonly", "contact", "user"]
          )
        , ( 'lettertitle'
          , ["admin", "adr_readonly", "contact", "user"]
          )
        , ( 'lookalike_city'
          , ["admin", "adr_readonly", "contact", "user"]
          )
        , ( 'lookalike_firstname'
          , ["admin", "adr_readonly", "contact", "user"]
          )
        , ( 'lookalike_function'
          , ["admin", "adr_readonly", "contact", "user"]
          )
        , ( 'lookalike_lastname'
          , ["admin", "adr_readonly", "contact", "user"]
          )
        , ( 'lookalike_street'
          , ["admin", "adr_readonly", "contact", "user"]
          )
        , ( 'messages'
          , ["admin", "adr_readonly", "contact", "user"]
          )
        , ( 'opening_hours'
          , ["admin", "adr_readonly", "contact", "user"]
          )
        , ( 'parent'
          , ["admin", "adr_readonly", "contact", "user"]
          )
        , ( 'postalcode'
          , ["admin", "adr_readonly", "contact", "user"]
          )
        , ( 'salutation'
          , ["admin", "adr_readonly", "contact", "user"]
          )
        , ( 'street'
          , ["admin", "adr_readonly", "contact", "user"]
          )
        , ( 'title'
          , ["admin", "adr_readonly", "contact", "user"]
          )
        , ( 'valid'
          , ["admin", "adr_readonly", "contact", "user"]
          )
        ]
      )
    , ( 'adr_type'
      , [ ( 'code'
          , ["admin", "adr_readonly", "user"]
          )
        , ( 'description'
          , ["admin", "adr_readonly", "user"]
          )
        , ( 'typecat'
          , ["admin", "adr_readonly", "user"]
          )
        ]
      )
    , ( 'adr_type_cat'
      , [ ( 'code'
          , ["admin", "adr_readonly", "user"]
          )
        , ( 'description'
          , ["admin", "adr_readonly", "user"]
          )
        , ( 'type_valid'
          , ["admin", "adr_readonly", "user"]
          )
        ]
      )
    , ( 'contact'
      , [ ( 'address'
          , ["admin", "adr_readonly", "contact", "user"]
          )
        , ( 'contact'
          , ["admin", "adr_readonly", "contact", "user"]
          )
        , ( 'contact_type'
          , ["admin", "adr_readonly", "contact", "user"]
          )
        , ( 'description'
          , ["admin", "adr_readonly", "contact", "user"]
          )
        ]
      )
    , ( 'contact_type'
      , [ ( 'description'
          , ["admin", "adr_readonly", "user"]
          )
        , ( 'name'
          , ["admin", "adr_readonly", "user"]
          )
        , ( 'order'
          , ["admin", "adr_readonly", "user"]
          )
        , ( 'url_template'
          , ["admin", "adr_readonly", "user"]
          )
        ]
      )
    , ( 'file'
      , [ ( 'content'
          , ["admin", "adr_readonly", "user"]
          )
        , ( 'name'
          , ["admin", "adr_readonly", "user"]
          )
        , ( 'type'
          , ["admin", "adr_readonly", "user"]
          )
        ]
      )
    , ( 'letter'
      , [ ( 'address'
          , ["admin", "user"]
          )
        , ( 'date'
          , ["admin", "user"]
          )
        , ( 'files'
          , ["admin", "user"]
          )
        , ( 'messages'
          , ["admin", "user"]
          )
        , ( 'subject'
          , ["admin", "user"]
          )
        ]
      )
    , ( 'msg'
      , [ ( 'author'
          , ["admin", "adr_readonly", "user"]
          )
        , ( 'content'
          , ["admin", "adr_readonly", "user"]
          )
        , ( 'date'
          , ["admin", "adr_readonly", "user"]
          )
        , ( 'files'
          , ["admin", "adr_readonly", "user"]
          )
        , ( 'inreplyto'
          , ["admin", "adr_readonly", "user"]
          )
        , ( 'messageid'
          , ["admin", "adr_readonly", "user"]
          )
        , ( 'recipients'
          , ["admin", "adr_readonly", "user"]
          )
        , ( 'summary'
          , ["admin", "adr_readonly", "user"]
          )
        , ( 'type'
          , ["admin", "adr_readonly", "user"]
          )
        ]
      )
    , ( 'opening_hours'
      , [ ( 'from_hour'
          , ["admin", "adr_readonly", "contact", "user"]
          )
        , ( 'from_minute'
          , ["admin", "adr_readonly", "contact", "user"]
          )
        , ( 'to_hour'
          , ["admin", "adr_readonly", "contact", "user"]
          )
        , ( 'to_minute'
          , ["admin", "adr_readonly", "contact", "user"]
          )
        , ( 'weekday'
          , ["admin", "adr_readonly", "contact", "user"]
          )
        ]
      )
    , ( 'query'
      , [ ( 'klass'
          , ["admin", "user"]
          )
        , ( 'name'
          , ["admin", "user"]
          )
        , ( 'private_for'
          , ["admin", "user"]
          )
        , ( 'tmplate'
          , ["admin", "user"]
          )
        , ( 'url'
          , ["admin", "user"]
          )
        ]
      )
    , ( 'tmplate'
      , [ ( 'files'
          , ["admin", "user"]
          )
        , ( 'name'
          , ["admin", "user"]
          )
        , ( 'tmplate_status'
          , ["admin", "user"]
          )
        ]
      )
    , ( 'tmplate_status'
      , [ ( 'description'
          , ["admin", "user"]
          )
        , ( 'name'
          , ["admin", "user"]
          )
        , ( 'order'
          , ["admin", "user"]
          )
        , ( 'use_for_invoice'
          , ["admin", "user"]
          )
        , ( 'use_for_letter'
          , ["admin", "user"]
          )
        ]
      )
    , ( 'user'
      , [ ( 'address'
          , ["admin", "user"]
          )
        , ( 'alternate_addresses'
          , ["admin", "user"]
          )
        , ( 'csv_delimiter'
          , ["admin"]
          )
        , ( 'password'
          , ["admin", "user"]
          )
        , ( 'phone'
          , ["admin", "adr_readonly", "user"]
          )
        , ( 'queries'
          , ["admin", "user"]
          )
        , ( 'realname'
          , ["admin", "adr_readonly", "user"]
          )
        , ( 'roles'
          , ["admin"]
          )
        , ( 'status'
          , ["admin", "user"]
          )
        , ( 'timezone'
          , ["admin", "user"]
          )
        , ( 'username'
          , ["admin", "adr_readonly", "user"]
          )
        ]
      )
    , ( 'user_status'
      , [ ( 'description'
          , ["admin", "user"]
          )
        , ( 'name'
          , ["admin", "user"]
          )
        ]
      )
    , ( 'valid'
      , [ ( 'description'
          , ["admin", "adr_readonly", "user"]
          )
        , ( 'name'
          , ["admin", "adr_readonly", "user"]
          )
        ]
      )
    , ( 'weekday'
      , [ ( 'name'
          , ["admin", "adr_readonly", "contact", "user"]
          )
        , ( 'order'
          , ["admin", "adr_readonly", "contact", "user"]
          )
        ]
      )
    ]

if __name__ == '__main__' :
    for cl, props in properties :
        print cl
        for p in props :
            print '    ', p
