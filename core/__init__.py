import sys

# all our _PATH globals should end with '/', our _FILEPATH(s) should not
#print(sys.path[0])
ROOT_PATH = sys.path[0] + "/"
#INCLUDE_PATH = ROOT_PATH + "inc/"
ETC_PATH = ROOT_PATH + "etc/"

from flask import Flask, request, g, abort

# https://github.com/pallets/flask/blob/master/flask/wrappers.py
from werkzeug.wrappers import Request as RequestBase, Response as ResponseBase

from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
    DateTime,
    func )

import datetime

from marshmallow import fields, Schema

Base = declarative_base()

class Chimas(Flask):
    def __init__(self, import_name=__package__, **kwargs):
        super(Chimas, self).__init__(import_name, **kwargs)

class Response(ResponseBase):
    default_mimetype = "application/json"

APP = Chimas(__name__)
APP.response_class = Response

APP.config['DEBUG'] = True
APP.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///{0}dummy.sqlite3-autocreate".format(ROOT_PATH)

from . import config
from . import errorhandling

APP.config.update(config.app_config)

DB = SQLAlchemy(APP)

class CommonTable(DB.Model):
    __abstract__ =  True

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    created = Column(DateTime, default = datetime.datetime.now)
    updated = Column(DateTime, default = datetime.datetime.now, onupdate = datetime.datetime.now)
    deleted = Column(String, default = 0)


class CommonSchema(Schema):
    class Meta:
        strict = True
        #dump_only = ['id', 'created', 'updated', 'deleted']

    id = fields.Integer(dump_only=True)
    created = fields.DateTime(dump_only=True) # read-only fields
    updated = fields.DateTime(dump_only=True)
    deleted = fields.String(dump_only=True)

from . import users
from . import boards
from . import topics
from . import posts
from . import threads
from . import authentication
from . import login
from . import timetokens

@APP.before_request
def check_authentication():
    has_authentication = authentication.authentication.verify_authentication()

    if has_authentication:
        g.is_authenticated = True
        g.username = has_authentication['username']
    else:
        g.is_authenticated = False
        #abort(500)

    #import pprint
    #pprint.pprint(request.method)

DB.create_all()

try:
    dummyuser = users.Users(username='admin', password='p4ssw0rd')
    DB.session.add(dummyuser)
    DB.session.commit()
except:
    pass
