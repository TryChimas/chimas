from sqlalchemy import func

boards_schema = {
    'allowed_read_roles': ['public'],
    'allowed_roles': [], #FIXME!!
    'allowed_write_roles': ['admin'],
    'allowed_item_read_roles': ['public'],
    'allowed_item_roles': [],
    'allowed_item_write_roles': ['admin'],
    'datasource': {
        'projection': {
            'created': 1,
            'deleted': 1,
            'description': 1,
            'etag': 1,
            'id': 1,
            'title': 1,
            'updated': 1
        },
        'source': 'Boards'
    },
    'item_lookup': True,
    'item_lookup_field': 'id',
    'item_url': 'regex("[0-9]+")',
    'public_methods': ['GET', 'HEAD'],
    'public_item_methods': ['GET', 'HEAD'],
    'resource_methods': ['GET', 'POST'],
    'schema': {
        'created': {
            'default': func.now,
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
        'description': {
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
            'required': False,
            'type': 'integer',
            'unique': True
        },
        'title': {
            'nullable': True,
            'required': False,
            'type': 'string',
            'unique': False
        },
        'updated': {
            'default': func.now,
            'nullable': True,
            'required': False,
            'type': 'datetime',
            'unique': False
        }
    } # 'schema key'
} # dict
