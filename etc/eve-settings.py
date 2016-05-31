from core import Boards, Posts, Users

from flask import current_app as app

from os.path import abspath

basedir = abspath(".") # FIXME: this gets parent directory from 'etc/'

DEBUG = True

# FIELDS

ID_FIELD            = "id"
ITEM_LOOKUP_FIELD   = "id"
ETAG                = "etag"
DATE_CREATED        = "created"
LAST_UPDATED        = "updated"
DELETED             = "deleted"

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + join(basedir,'dummy.sqlite3-autocreate')

DOMAIN = {
    'boards' : Boards._eve_schema['boards'],
    'posts'  : Posts._eve_schema['posts'],
    'users'  : Users._eve_schema['users'],
}

ITEM_METHODS = []
PUBLIC_ITEM_METHODS = []
PUBLIC_METHODS = []
RESOURCE_METHODS = []

ALLOWED_ROLES = []
ALLOWED_READ_ROLES = []
ALLOWED_WRITE_ROLES = []
ALLOWED_ITEM_ROLES = []
ALLOWED_ITEM_READ_ROLES = []
ALLOWED_ITEM_WRITE_ROLES = []
