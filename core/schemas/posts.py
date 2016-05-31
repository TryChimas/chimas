from sqlalchemy import func

posts_schema = {
    'allowed_read_roles' : ['public'],
    'allowed_roles': [],
    'allowed_write_roles' : ['registered'],
    'allowed_item_read_roles': ['public'],
    'allowed_item_roles': [],
    'allowed_item_write_roles': ['admin', 'owner'],
#    'allowed_item_read_roles': ['admin', 'owner', 'registered'],
    'datasource': {
        'projection': {
            'author_id': 1,
            'board_id': 1,
            'created': 1,
            'deleted': 1,
            'etag': 1,
            'hash_id': 1,
            'id': 1,
            'post_text': 1,
            'reply_to_id': 1,
            'title': 1,
            'topic_id': 1,
            'updated': 1
        },
        'source': 'Posts'
    },
    'item_lookup': True,
    'item_lookup_field': 'id',
    'item_methods': ['GET', 'DELETE'],
    'item_url': 'regex("[0-9]+")',
    'resource_methods': ['GET', 'POST'],
    'schema': {
        'author_id': {
            'nullable': True,
            'required': False,
            'type': 'string',
            'unique': False
        },
        'board_id': {
            'nullable': True,
            'required': False,
            'type': 'string',
            'unique': False
        },
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
        'etag': {
            'nullable': True,
            'required': False,
            'type': 'string',
            'unique': False
        },
        'hash_id': {
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
        'post_text': {
            'nullable': True,
            'required': False,
            'type': 'string',
            'unique': False
        },
        'reply_to_id': {
            'nullable': True,
            'required': False,
            'type': 'string', # FIXME: int is returning 422 when using python's requests
            'unique': False
        },
        'title': {
            'nullable': True,
            'required': False,
            'type': 'string',
            'unique': False
        },
        'topic_id': {
            'nullable': True,
            'required': False,
            'type': 'string', # FIXME: int is returning 422 when using python's requests
            'unique': False
        },
        'updated': {
            'default': func.now(),
            'nullable': True,
            'required': False,
            'type': 'datetime',
            'unique': False
        }
    } # 'schema' key
} # dict
