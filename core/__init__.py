import sys
#print(sys.path)

# all our _PATH globals should end with '/', our _FILEPATH(s) should not

ROOT_PATH = sys.path[0] + "/"
INCLUDE_PATH = ROOT_PATH + "inc/"
ETC_PATH = ROOT_PATH + "etc/"

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

#from .auth import ChimasAuth

from .config import ConfigParser

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import (
        Column,
        String,
        Integer,
        ForeignKey,
        DateTime )

from sqlalchemy import func

Base = declarative_base()

#APP = Flask(__name__)

class Chimas(Flask):

    def __init__(self, import_name=__package__, **kwargs):
        super(Chimas, self).__init__(import_name, **kwargs)

APP = Chimas(__name__)

APP.config['DEBUG'] = True
APP.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///{0}dummy.sqlite3-autocreate".format(ROOT_PATH)

DB = SQLAlchemy(APP)
MA = Marshmallow(APP)

class CommonTable(DB.Model):
    __abstract__ =  True

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime, default = func.now())
    updated = Column(DateTime, default = func.now(), onupdate = func.now())
    etag = Column(String)
    deleted = Column(String)

#class CommonSchema(MA.ModelSchema):
#    class Meta:
#        model = CommonTable

#    def __init__(self):
#        super(CommonSchema, self).__init__()

class Boards(CommonTable):
    __tablename__ = 'boards'

    id = None
    title = Column(String, primary_key=True, unique=True)
    description = Column(String)

#class BoardsSchema(CommonSchema):
class BoardsSchema(MA.ModelSchema):
    class Meta:
        model = Boards

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

class PostsSchema(MA.ModelSchema):
    class Meta:
        model = Posts

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
        pass

@APP.route('/posts/<int:topic_id>')
def get_topic(topic_id):
    posts_schema = PostsSchema(many=True)
    #posts = Posts.query.filter(Posts.id == topic_id).first()
    #posts = Posts().query_class.filter_by(topic_id=topic_id).first()
    posts = Posts().query.filter_by(topic_id=topic_id).first()
    return posts

@APP.route('/boards')
def list_boards():
    #posts = Posts.query.filter(Posts.id == topic_id).first()
    boards_schema = BoardsSchema(many=True)
    boards = Boards().query.all()
    from flask import jsonify
    return boards_schema.dumps(boards).data
    #return boards

DB.create_all()
