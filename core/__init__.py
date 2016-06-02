import sys

# all our _PATH globals should end with '/', our _FILEPATH(s) should not

ROOT_PATH = sys.path[0] + "/"
INCLUDE_PATH = ROOT_PATH + "inc/"
ETC_PATH = ROOT_PATH + "etc/"

#from eve.utils import config as EVE_CONFIG # FIXME
#EVE_CONFIG.ID_FIELD = 'id'

from sqlalchemy.ext.declarative import declarative_base
from eve_sqlalchemy.decorators import registerSchema

from sqlalchemy import (
        Column,
        String,
        Integer,
        ForeignKey,
        DateTime )

from sqlalchemy import func

from .schemas.boards import boards_schema
from .schemas.posts import posts_schema
from .schemas.users import users_schema

from flask import current_app as app
from flask import abort

Base = declarative_base()

def get_class_by_tablename(table_fullname, base=Base):
    for c in base._decl_class_registry.values():
        if hasattr(c, '__table__') and c.__table__.fullname == table_fullname:
            return c
        else:
            return None

class CommonTable(Base):
    __abstract__ =  True

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime, default = func.now())
    updated = Column(DateTime, default = func.now(), onupdate = func.now())
    etag = Column(String)
    deleted = Column(String)

    def do_method(preorpost_prefix, resource, request, lookup):

        method = request.method.lower()
        table = get_class_by_tablename(resource)

        if table != None:
            print("table {0} found!\n".format(table.__tablename__))
            try :
                print("We're trying '{0}' the method".format(preorpost_prefix))
                methodCall = getattr(table, preorpost_prefix + method)
                return methodCall(resource, request, lookup)
            except:
                pass

            print("Passed executing method")

    def do_pre_method(resource, request, lookup=None):
        __class__.do_method('pre_', resource, request, lookup)

    def do_post_method(resource, request, payload=None):
        __class__.do_method('post_', resource, request, payload)

class Boards(CommonTable):
    __tablename__ = 'boards'

    id = None
    title = Column(String, primary_key=True, unique=True)
    description = Column(String)

class Posts(CommonTable):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    topic_id = Column(String) # FIXME: int is returning 422 when using python's requests
    reply_to_id = Column(String) # FIXME: int is returning 422 when using python's requests

    board_id = Column(String)
    author_id = Column(String)
    title = Column(String)
    post_text = Column(String)
    hash_id = Column(String)

class Users(CommonTable):
    __tablename__ = 'users'

    #id = Column(Integer, autoincrement=True, unique=True)
    id = None
    login = Column(String, primary_key=True, unique=True)
    email = Column(String, unique=True)
    password = Column(String)

class Roles(CommonTable):
    __tablename__ = 'roles'

    id = Column(Integer, autoincrement=True, unique=True)
    title = Column(String, primary_key=True, unique=True)
    prefix = Column(String)
    users = Column(String)

    def is_authorized(user, is_authenticated, allowed_roles, resource, method, lookup):

        if 'anonymous' in allowed_roles:
            return True

        if 'registered' in allowed_roles:
            if is_authenticated:
                return True

        if 'moderators' in allowed_roles:
            pass

        #if 'owner' in allowed_roles:


        #login = user.login


registerSchema('boards')(Boards)
registerSchema('posts')(Posts)
registerSchema('users')(Users)
Boards._eve_schema['boards'].update(boards_schema)
Posts._eve_schema['posts'].update(posts_schema)
Users._eve_schema['users'].update(users_schema)
