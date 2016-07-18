import sys

# all our _PATH globals should end with '/', our _FILEPATH(s) should not
print(sys.path[0])
ROOT_PATH = sys.path[0] + "/"
INCLUDE_PATH = ROOT_PATH + "inc/"
ETC_PATH = ROOT_PATH + "etc/"

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_marshmallow import fields

from flask import request

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
APP.config['SECRET_KEY'] = 'super-secret'

DB = SQLAlchemy(APP)
MA = Marshmallow(APP)

class CommonTable(DB.Model):
    __abstract__ =  True

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime, default = func.now())
    updated = Column(DateTime, default = func.now(), onupdate = func.now())
    etag = Column(String)
    deleted = Column(String)

from . import boards
from . import posts
#from . import roles
from . import users

from . import auth

DB.create_all()

try:
    dummyuser = users.Users(login='admin', email='kassivs@gmail.com', password='p4ssw0rd')
    DB.session.add(dummyuser)
    DB.session.commit()
except:
    pass
