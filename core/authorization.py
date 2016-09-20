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
from .boards import Boards
from .roles import Roles


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
        # http://stackoverflow.com/questions/10176226/how-to-pass-extra-arguments-to-python-decorator
        def actual_decorator(endpoint_function):

            @wraps(endpoint_function)
            def decorated(*args, **kwargs):

                # process http header
                auth = self.process_auth_http_header()
                if not auth:
                    abort(401)

                # process token to verify if user:token is valid
                user_token = self.process_token(auth['token'])
                if not user_token:
                    abort(401)

                # verify if user has permission roles to acess endpoint
                has_permission = self.verify_permission(user_token['username'], allowed_roles)
                if not has_permission:
                    abort(401)

                # else
                return endpoint_function(*args, **kwargs)

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

        if AuthTokens.query.filter_by(username=username,\
            token=auth_token).first():

            return { 'username':username, 'auth_token':auth_token }
        # else
        return None

    def verify_permission(self, username, allowed_roles):

        if 'public' in allowed_roles:
            return True

        if 'admin' in allowed_roles and 'username' == 'admin':
            # FIXME: use db groups/roles instead of static username
            return True

        if 'owner' in allowed_roles:
            post_id = request.view_args['author_id']
            author_id = request.view_args['author_id']
            is_user_owner = Posts.query.filter_by(id=post_id,\
                author_id=username).first()

            if is_user_owner:
                return True

        if 'moderators' in allowed_roles:
            board_id = request.view_args['board_id']
            user_in_group = Groups.query.filter_by(role=moderators,\
                username=username, arguments=board_id).first()
            if user_in_group:
                return True

        import json
        print(request.view_args) #ta-da!!
        return True
        #pass


chimas_auth = ChimasAuth(scheme='Token')
