
from flask import Flask, request, g, abort

# https://github.com/pallets/flask/blob/master/flask/wrappers.py
from werkzeug.wrappers import Request as RequestBase, Response as ResponseBase



import datetime # or use time.time to make timestamps

# from flask import current_app as app

import sys

ROOT_PATH = sys.path[0] + "/"
ETC_PATH = ROOT_PATH + "etc/"

class Response(ResponseBase):
    default_mimetype = "application/json"

# http://flask-sqlalchemy.pocoo.org/2.1/contexts/

class CommonAPI:
    def __init__(self, app):
        self.app = app
        #pass


    def register_endpoint(self, rule, function, **options):
        self.app.add_url_rule(rule, endpoint=function.__name__, view_func=function, **options)

    # def route(self, rule, **options):
    #     def decorator(f):
    #         endpoint = options.pop('endpoint', None)
    #         self.add_url_rule(rule, endpoint, f, **options)
    #         return f
    #     return decorator

class Chimas(Flask):
    def __init__(self, instance=None, import_name=__package__, **kwargs):
        super(Chimas, self).__init__(import_name, **kwargs)

        from flask_sqlalchemy import SQLAlchemy
        from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, func
        from marshmallow import fields, Schema

        self.response_class = Response

        self.instance = instance

        self.app = self.app_context()
        self.db = SQLAlchemy()
        self.db.init_app(self)

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

        #from . import errorhandling
        #from . import users, boards, topics, posts, threads,\
        #                authentication, login, timetokens

        #with self.app_context():
            #self.do_registrations()
        #self.before_first_request(self.do_registrations)
        #    self.do_registrations()
        #    self.do_registrations
        #    self.do_registrations()
        #self.app_context(self.do_registrations)

    def __call__(self, environ, start_response):
        """Shortcut for :attr:`wsgi_app`."""
        #self.teardown_appcontext(self.teardown)
        with self.app:
            from . import config

            self.config.update(config.app_config)
            #self.db.init_app(self)

            self.g = g

            #self.db.init_app(self)
            from . import errorhandling
            from . import users, boards, topics, posts, threads,\
                            authentication, login, timetokens
            endpoint_submodules = ['errorhandling', 'login']

            self.g.users = users.UsersAPI(self)
            #self.g.boards = boards.BoardsAPI(self)
            #self.g.topics = topics.TopicsAPI(self)
            #self.g.posts = posts.PostsAPI(self)
            #self.g.threads = threads.ThreadsAPI(self)
            self.g.login = login.LoginAPI(self)
            #self.g.timetokens = timetokens.TimeTokensAPI(self)

            @self.before_request
            def check_authentication():
                #print(instance)
                has_authentication = authentication.authentication.verify_authentication()

                if has_authentication:
                    g.is_authenticated = True
                    g.username = has_authentication['username']
                else:
                    g.is_authenticated = False

            self.db.create_all()

            try:
                dummyuser = users.Users(username='admin', password='p4ssw0rd')
                self.db.session.add(dummyuser)
                self.db.session.commit()
            except:
                pass

        return self.wsgi_app(environ, start_response)

    # def do_registrations(self):
    #     #self.teardown_appcontext(self.teardown)
    #     #with self.app.app_context():
    #     from . import config
    #
    #     self.config.update(config.app_config)
    #
    #     self.g = g
    #
    #     self.db = self.db
    #     #self.db.init_app(self)
    #
    #     from . import errorhandling
    #     from . import users, boards, topics, posts, threads,\
    #                     authentication, login, timetokens
    #
    #     @self.before_request
    #     def check_authentication():
    #         #print(instance)
    #         has_authentication = authentication.authentication.verify_authentication()
    #
    #         if has_authentication:
    #             g.is_authenticated = True
    #             g.username = has_authentication['username']
    #         else:
    #             g.is_authenticated = False
    #
    #     self.db.create_all()
    #
    #     try:
    #         dummyuser = users.Users(username='admin', password='p4ssw0rd')
    #         self.db.session.add(dummyuser)
    #         self.db.session.commit()
    #     except:
    #         pass

        #return self.wsgi_app(environ, start_response)
