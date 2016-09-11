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

#from flask.views import MethodView

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
    deleted = Column(Integer, default = 0)

class CommonSchema(Schema):
    class Meta:
        strict = True
    id = fields.Integer()
    created = fields.DateTime()
    updated = fields.DateTime()
    deleted = fields.Integer()

from . import users
from . import boards
from . import topics
from . import posts

DB.create_all()

try:
    dummyuser = users.Users(username='admin', password='p4ssw0rd')
    DB.session.add(dummyuser)
    DB.session.commit()
except:
    pass
