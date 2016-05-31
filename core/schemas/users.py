from sqlalchemy import func

users_schema = {
    'allowed_read_roles': ['admin', 'owner'],
    'allowed_roles': [], #FIXME!!
    'allowed_write_roles': ['public'],
    'allowed_item_read_roles': ['admin', 'owner'],
    'allowed_item_roles': ['admin', 'owner']
    'allowed_item_write_roles': ['admin', 'owner'],
    'datasource': {
        'projection': {
            'created': 1,
            'deleted': 1,
            'email': 1,
            'etag': 1,
            'id': 1,
            'login': 1,
            'password': 0,
            'updated': 1
        },
        'source': 'Users'
    },
    'id_field': 'login',
    'item_lookup': True,
    'item_lookup_field': 'login',
    'item_methods': ['GET', 'HEAD', 'PATCH', 'DELETE'],
    'item_url': 'regex("[0-9]+")',
    'resource_methods': ['POST'],
    'schema': {
        'created': {
            'default': func.now(),
            'nullable': True,
            'required': False,
            'type': 'datetime',
            'unique': False
        },
        'deleted': {
            'nullable': True,
            'required': False,
            'type': 'string',
            'unique': False
        },
        'email': {
            'nullable': True,
            'required': False,
            'type': 'string',
            'unique': False
        },
        'etag': {
            'nullable': True,
            'required': False,
            'type': 'string',
            'unique': False
        },
        'id': {
            'nullable': True,
            'required': False,
            'type': 'integer',
            'unique': True
        },
        'login': {
            'required': False,
            'type': 'string',
            'unique': True
        },
        'password': {
            'nullable': True,
            'required': False,
            'type': 'string',
            'unique': False
        },
        'updated': {
            'default': func.now(),
            'nullable': True,
            'required': False,
            'type': 'datetime',
            'unique': False
        }
    } # END OF 'schema'
} # END OF 'users_schema' dict
