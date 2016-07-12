import sys
#print(sys.path)

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

from .auth import check_auth

from .config import ConfigParser

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import (
        Column,
        String,
        Integer,
        ForeignKey,
        DateTime )

from sqlalchemy import func

from flask.ext.security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required

Base = declarative_base()

#APP = Flask(__name__)

class Chimas(Flask):

    def __init__(self, import_name=__package__, **kwargs):
        super(Chimas, self).__init__(import_name, **kwargs)

APP = Chimas(__name__)

APP.config['DEBUG'] = True
APP.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///{0}dummy.sqlite3-autocreate".format(ROOT_PATH)
APP.config['SECRET_KEY'] = 'super-secret'
APP.config['SECURITY_TOKEN_AUTHENTICATION_HEADER'] = 'lolwat'


DB = SQLAlchemy(APP)
MA = Marshmallow(APP)

APP.before_request(check_auth)

class CommonTable(DB.Model):
    __abstract__ =  True

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime, default = func.now())
    updated = Column(DateTime, default = func.now(), onupdate = func.now())
    etag = Column(String)
    deleted = Column(String)

from . import boards
from . import posts
from . import roles
from . import users

#roles_users = db.Table('roles_users',
#        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
#        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

user_datastore = SQLAlchemyUserDatastore(DB, users.Users, roles.Roles)
security = Security(APP, user_datastore)

#class AppError(Exception):
#    pass

#DB.create_all()

#@APP.before_first_request
#def create_user():
DB.create_all()

try:
    user_datastore.create_user(login='admin', email='kassivs@gmail.com', password='p4ssw0rd')
    DB.session.commit()

except:
    pass
