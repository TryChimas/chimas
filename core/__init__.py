from flask import Flask

from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sqla
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


from marshmallow import fields, Schema

from werkzeug.wrappers import Response as ResponseBase

import datetime # or use time.time to make timestamps
import sys

print("HEllo i am core.__init__ and __file__ is" + __file__)

ROOT_PATH = sys.path[0] + "/"
ETC_PATH = ROOT_PATH + "etc/"

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

class DB:
    def __init__(self, db_file):
        self.engine = sqla.create_engine(db_file, echo=True)
        self.Base = declarative_base()
        self.session_factory = scoped_session(sessionmaker(bind=self.engine))
        self.session = self.session_factory()

    def create_all(self):
        self.Base.metadata.create_all(self.engine)


def commontable_factory(db):
    class CommonTable(db.Base):
        __abstract__ =  True
    
        id = sqla.Column(sqla.Integer, primary_key=True, unique=True, autoincrement=True)
        created = sqla.Column(sqla.DateTime, default = datetime.datetime.now)
        updated = sqla.Column(sqla.DateTime, default = datetime.datetime.now, onupdate = datetime.datetime.now)
        deleted = sqla.Column(sqla.String, default = 0)

        query = db.session_factory.query_property()
    
    return CommonTable
    
class Response(ResponseBase):
	default_mimetype = "application/json"

class Chimas(Flask):
    def __init__(self, instance=None, import_name=__package__, **kwargs):
        super(Chimas, self).__init__(import_name, **kwargs)

        self.response_class = Response

        self.instance = instance

        if instance:
            db_file = "".join(["sqlite:///", ROOT_PATH, "dummy-", instance, ".sqlite3-autocreate"])
        else:
            db_file = "".join(["sqlite:///", ROOT_PATH, "dummy.sqlite3NHA-autocreate"])

        self.db = DB(db_file)

        self.config['DEBUG'] = True

        self.CommonTable = commontable_factory(self.db)
        class CommonSchema(Schema):
            class Meta:
                strict = True

            id = fields.Integer(dump_only=True)
            created = fields.DateTime(dump_only=True) # read-only fields
            updated = fields.DateTime(dump_only=True)
            deleted = fields.String(dump_only=True)

        
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

        self.db.create_all()
        self.db.session.commit()
        
        # add dummy user
        session = self.db.session 
        Users = self.users.Users
        is_there_admin = Users.query.filter_by( username='admin' ).first()

        if not is_there_admin:
            dummyuser = Users(username='admin', password='p4ssw0rd')
            session.add(dummyuser)
            session.commit()

    def check_authentication(self):
        has_authentication = self.authentication.verify_authentication()

        if has_authentication:
            g.is_authenticated = True
            g.username = has_authentication['username']
        else:
            g.is_authenticated = False
