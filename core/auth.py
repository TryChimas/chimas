from . import APP, DB, CommonTable, CommonSchema

from sqlalchemy import (
        Column,
        String,
        Integer,
        ForeignKey,
        DateTime,
        func )

#from flask_httpauth import HTTPTokenAuth
from marshmallow import fields, Schema, post_load

#from werkzeug.http import parse_authorization_header

from .users import Users

class AuthTokens(CommonTable):
    __tablename__ = 'authtokens'

    #id = None
    username = Column(String)
    token = Column(String)
    expires = Column(String)

class AuthTokensSchema(CommonSchema):
    username = fields.Str()
    token = fields.Str()
    expires = fields.Str()

    @post_load
    def make_authtoken(self, data):
        return AuthTokens(**data)

from functools import wraps
from hashlib import md5
from random import Random, SystemRandom
from flask import request, make_response, session
from werkzeug.datastructures import Authorization

class ChimasAuth:
    def __init__(self, scheme='Token', realm=None):
        self.scheme = scheme
        self.realm = realm

    def verify_authorization(self, endpoint_function):
        @wraps(endpoint_function)
        def decorated(*args, **kwargs):

            # process http header
            auth = self.process_auth_http_header()
            if not auth:
                abort(401)
            else:
                # process auth token
                self.process_token(auth['token'])


            return endpoint_function(*args, **kwargs)
        return decorated

    def process_auth_http_header(self):
        auth = None

        if 'Authorization' in request.headers:

            try:
                # https://docs.python.org/3.5/library/stdtypes.html#str.split
                auth_type, token = request.headers['Authorization'].\
                    split(sep=None, maxsplit=1)
                auth = Authorization(auth_type, {'token': token})
            except ValueError:
                # The Authorization header is either empty or has no token
                pass

        # if requested auth method is not our supported one (Token)
        # then lets give error 401
        if auth and auth.type.lower() != self.scheme.lower():
            #abort(401) #return None
            return None

        print(auth['token']) #works
        return auth

        def process_token(self, token):
            pass

chimas_auth = ChimasAuth(scheme='Token')
