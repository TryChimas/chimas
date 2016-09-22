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
from marshmallow import fields, Schema

import datetime # or use time.time to make timestamps

from flask import current_app as app

class Response(ResponseBase):
    default_mimetype = "application/json"

# http://flask-sqlalchemy.pocoo.org/2.1/contexts/

class Chimas(Flask):
    def __init__(self, import_name=__package__, **kwargs):

        super(Chimas, self).__init__(import_name, **kwargs)

        self.response_class = Response

        self.db = SQLAlchemy(self)

        self.config['DEBUG'] = True
        self.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///{0}dummy.sqlite3-autocreate".format(ROOT_PATH)

        from . import config

        self.config.update(config.app_config)

        #def __call__(self):
        #    self.db.init_app(self)
        class CommonTable(self.db.Model):
            __abstract__ =  True

            id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
            created = Column(DateTime, default = datetime.datetime.now)
            updated = Column(DateTime, default = datetime.datetime.now, onupdate = datetime.datetime.now)
            deleted = Column(String, default = 0)

        class CommonSchema(Schema):
            class Meta:
                strict = True

            id = fields.Integer(dump_only=True)
            created = fields.DateTime(dump_only=True) # read-only fields
            updated = fields.DateTime(dump_only=True)
            deleted = fields.String(dump_only=True)

        self.CommonTable = CommonTable
        self.CommonSchema = CommonSchema

        with self.app_context():
            from . import errorhandling
            from . import users, boards, topics, posts, threads,\
                            authentication, login, timetokens

            @app.before_request
            def check_authentication():
                has_authentication = authentication.authentication.verify_authentication()

                if has_authentication:
                    g.is_authenticated = True
                    g.username = has_authentication['username']
                else:
                    g.is_authenticated = False

    def create_app(self):
        return self


#db = SQLAlchemy()
#app = Chimas()
#def create_app():
#
#    app = Chimas(__name__)
#    return app
#    db.create_all()

try:
    dummyuser = users.Users(username='admin', password='p4ssw0rd')
    db.session.add(dummyuser)
    db.session.commit()
except:
    pass
