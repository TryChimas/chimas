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
#from .boards import Boards
#from .roles import Roles


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

class ChimasAuthentication:
    def __init__(self, scheme='Token', realm=None):
        self.scheme = scheme
        self.realm = realm

    def verify_authentication(self):
        # process http header
        auth = self.process_auth_http_header()
        if not auth:
            return False

        # process token to verify if user:token is valid
        user_token = self.process_token(auth['token'])
        if not user_token:
            return False

        return user_token

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
        else:
            auth = None

        return auth

    def process_token(self, token):
        username, auth_token = token.split(sep=':', maxsplit=1)

        if AuthTokens.query.filter_by(username=username,\
            token=auth_token).first():

            return { 'username':username, 'auth_token':auth_token }
        # else
        return None

authentication = ChimasAuthentication(scheme='Token')
