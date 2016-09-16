from . import APP, DB, CommonTable, CommonSchema

from sqlalchemy import (
        Column,
        String,
        Integer,
        ForeignKey,
        DateTime,
        func )

from marshmallow import fields, Schema, post_load

from functools import wraps
from flask import request, abort, make_response, session
from werkzeug.datastructures import Authorization

from .users import Users

class AuthTokens(CommonTable):
    __tablename__ = 'authtokens'

    id = None
    username = Column(String)
    token = Column(String, primary_key=True, unique=True, autoincrement=True)
    expires = Column(String)

class AuthTokensSchema(CommonSchema):
    id = None
    username = fields.Str()
    token = fields.Str()
    expires = fields.Str()

    @post_load
    def make_authtoken(self, data):
        return AuthTokens(**data)

class ChimasAuth:
    def __init__(self, scheme='Token', realm=None):
        self.scheme = scheme
        self.realm = realm

    def verify_authorization(self, allowed_roles):

        def actual_decorator(endpoint_function):

            @wraps(endpoint_function)
            def decorated(*args, **kwargs):

                # process http header
                auth = self.process_auth_http_header()
                if auth and self.process_token(auth['token']):
                    pass
                else:
                    abort(401)

                import json
                return json.dumps(allowed_roles)
            return decorated

        return actual_decorator

    def process_auth_http_header(self):
        auth = None

        if 'Authorization' in request.headers:
            try:
                # https://docs.python.org/3.5/library/stdtypes.html#str.split
                auth_type, token = request.headers['Authorization'].\
                    split(sep=None, maxsplit=1)
                auth = Authorization(auth_type, {'token': token})
            except ValueError:
                auth = None
                #pass
        else:
            auth = None

        return auth

    def process_token(self, token):
        username, auth_token = token.split(sep=':', maxsplit=1)

        if AuthTokens.query.filter_by(username=username, token=auth_token).first():
            return True

        # else
        return False

chimas_auth = ChimasAuth(scheme='Token')
