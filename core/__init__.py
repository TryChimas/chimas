import sys
#print(sys.path)

# all our _PATH globals should end with '/', our _FILEPATH(s) should not

ROOT_PATH = sys.path[0] + "/"
INCLUDE_PATH = ROOT_PATH + "inc/"
ETC_PATH = ROOT_PATH + "etc/"

from flask import Flask
from flask_sqlalchmy import SQLAlchemy
#from eve import Eve

#from eve_sqlalchemy import SQL
#from eve_sqlalchemy.validation import ValidatorSQL

from .auth import ChimasAuth

from .config import ConfigParser

from sqlalchemy.ext.declarative import declarative_base
#from eve_sqlalchemy.decorators import registerSchema

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

#from flask import current_app as app
#from flask import abort

#APP = Eve(settings=ETC_PATH+'eve-settings.py', auth=ChimasAuth, validator=ValidatorSQL, data=SQL)

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

#def get_topic(self, topid_id):
#    #posts = Posts.query.filter(Posts.id == topic_id).first()
#    return "we are inside post item"

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

#registerSchema('boards')(Boards)
#registerSchema('posts')(Posts)
#registerSchema('users')(Users)
#Boards._eve_schema['boards'].update(boards_schema)
#Posts._eve_schema['posts'].update(posts_schema)
#Users._eve_schema['users'].update(users_schema)

#DOMAIN = {
#    'boards' : Boards._eve_schema['boards'],
#    'posts'  : Posts._eve_schema['posts'],
#    'users'  : Users._eve_schema['users'],
#}

SQLALCHEMY_DATABASE_URI = "sqlite:///{0}dummy.sqlite3-autocreate".format(ROOT_PATH)

#APP = Eve(settings=ETC_PATH+'eve-settings.py', auth=ChimasAuth, validator=ValidatorSQL, data=SQL)
APP = Flask(__name__)
#ConfigParser(APP)

#class Chimas(Flask):

#    def __init__(self, import_name=__package__, **kwargs):
#        super(Chimas, self).__init__(import_name, **kwargs)


#APP = Chimas(__name__)

#Db = SQLAlchemy(APP, metadata=Base.metadata)

@APP.route('/posts/<int:topic_id>')
def get_topic(self, topid_id):
    #posts = Posts.query.filter(Posts.id == topic_id).first()
    return "we are inside post item"

#Base.metadata.bind = APP.data.driver.engine
#APP.data.driver.Model = Base
APP.data.driver.create_all()

Base.query = APP.data.driver.session.query_property()
