import sys

# all our _PATH globals should end with '/', our _FILEPATH(s) should not
#print(sys.path[0])
ROOT_PATH = sys.path[0] + "/"
#INCLUDE_PATH = ROOT_PATH + "inc/"
ETC_PATH = ROOT_PATH + "etc/"

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

#from .config import ConfigParser

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
    DateTime,
    func )

from marshmallow import fields, Schema

from flask.views import MethodView

Base = declarative_base()

class Chimas(Flask):
    def __init__(self, import_name=__package__, **kwargs):
        super(Chimas, self).__init__(import_name, **kwargs)

APP = Chimas(__name__)

APP.config['DEBUG'] = True
APP.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///{0}dummy.sqlite3-autocreate".format(ROOT_PATH)

DB = SQLAlchemy(APP)

class CommonTable(DB.Model):
    __abstract__ =  True

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime, default = func.now())
    updated = Column(DateTime, default = func.now(), onupdate = func.now())

# users.py
class Users(CommonTable):
    __tablename__ = 'users'

    id = None
    username = Column(String, primary_key=True, unique=True)
    #email = Column(String, unique=True)
    password = Column(String)

class UsersSchema(Schema):
    username = fields.Str()
    password = fields.Str()

    created = fields.DateTime()
    updated = fields.DateTime()

class UsersAPI(MethodView):
    def post(self):
        user_schema = UsersSchema()
        print('users API [post]')

users_view = UsersAPI.as_view('users_api')
APP.add_url_rule('/users', view_func=users_view, methods=['POST'])

DB.create_all()

try:
    dummyuser = users.Users(username='admin', password='p4ssw0rd')
    DB.session.add(dummyuser)
    DB.session.commit()
except:
    pass
