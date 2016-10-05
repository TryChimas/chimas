
from flask import Flask, request, g, abort

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, func
from marshmallow import fields, Schema

# https://github.com/pallets/flask/blob/master/flask/wrappers.py
from werkzeug.wrappers import Response as ResponseBase

import datetime # or use time.time to make timestamps
import sys

ROOT_PATH = sys.path[0] + "/"
ETC_PATH = ROOT_PATH + "etc/"

class Response(ResponseBase):
    default_mimetype = "application/json"

class CommonAPI:
    def __init__(self, app):
        self.app = app
        self.db = app.db

    def register_endpoints(self, api_endpoints):
        for endpoint in api_endpoints:
            rule, function, options = endpoint
            self.register_endpoint(rule, function, **options)

    def register_endpoint(self, rule, function, **options):
        self.app.add_url_rule(rule, endpoint=function.__name__, view_func=function, **options)

from . import errorhandling
from . import config
from . import roles, authentication, authorization
from . import users, boards, topics, posts, threads, login, timetokens

class Chimas(Flask):
    def __init__(self, instance=None, import_name=__package__, **kwargs):
        super(Chimas, self).__init__(import_name, **kwargs)

        self.response_class = Response

        self.instance = instance

        self.db = SQLAlchemy(self)

        self.config['DEBUG'] = True

        if instance:
            self.config['SQLALCHEMY_DATABASE_URI'] = "".\
                join(["sqlite:///", ROOT_PATH, "dummy-", instance, ".sqlite3-autocreate"])
        else:
            self.config['SQLALCHEMY_DATABASE_URI'] = "".\
                join(["sqlite:///", ROOT_PATH, "dummy.sqlite3NHA-autocreate"])

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

        self.config.update(config.app_config)

        # this transforms the 'ErrorHandling' in this list to:
        # self.errorhandling = errorhandling.ErrorHandlingAPI(self)
        # and also do this to all the api list items
        api_list = [
            'ErrorHandling', 'Authentication', 'Authorization', 'Users',
            'Boards', 'Posts', 'Topics', 'Threads', 'Login', 'TimeTokens',
            'Roles' ]

        # }:-{> hell-o
        for api in api_list:

            # 1. 'ErrorHandling'.lower() == 'errorhandling'. So method and module.
            method = module = api.lower()
            #module_api = eval("{0}.{1}API(self)".format(module,api) )

            # 2. eval('errorhandling.ErrorHandlingAPI(self)')
            #  module_api = eval(".".join([module,api])+'API(self)' )
            module_api = eval("".join([module,'.',api,'API(self)'] ))

            # 3. self.errorhandling = errorhandling.ErrorHandlingAPI(self)
            setattr(self, method, module_api)

        # self.errorhandling = errorhandling.ErrorHandlingAPI(self)
        #
        # self.authentication = authentication.AuthenticationAPI(self)
        # self.authorization = authorization.AuthorizationAPI(self)
        #
        # self.users = users.UsersAPI(self)
        # self.boards = boards.BoardsAPI(self)
        # self.posts = posts.PostsAPI(self)
        # self.topics = topics.TopicsAPI(self)
        # self.threads = threads.ThreadsAPI(self)
        # self.login = login.LoginAPI(self)
        # self.timetokens = timetokens.TimeTokensAPI(self)
        # self.roles = roles.RolesAPI(self)

        print(self.url_map)

        self.before_request(self.check_authentication)

        try:
            dummyuser = self.users.Users(username='admin', password='p4ssw0rd')
            self.db.session.add(dummyuser)
            self.db.session.commit()
        except:
            pass

        self.db.create_all()

    def check_authentication(self):
        has_authentication = self.authentication.verify_authentication()

        if has_authentication:
            g.is_authenticated = True
            g.username = has_authentication['username']
        else:
            g.is_authenticated = False
