import sqlalchemy as sqla

from marshmallow import fields, Schema, post_load

from flask import request, abort

from werkzeug.datastructures import Authorization

class AuthenticationAPI:
    def __init__(self, app):
        self.scheme = 'Token'
        self.realm = None

        self.app = app

        class AuthTokens(app.CommonTable):
            __tablename__ = 'authtokens'

            id = None
            username = sqla.Column(sqla.String)
            token = sqla.Column(sqla.String, primary_key=True, unique=True, autoincrement=True)
            expires = sqla.Column(sqla.String)

        class AuthTokensSchema(app.CommonSchema):
            id = None
            username = fields.Str()
            token = fields.Str()
            expires = fields.Str()

            @post_load
            def make_authtoken(self, data):
                return AuthTokens(**data)

        self.AuthTokens = AuthTokens
        self.AuthTokensSchema = AuthTokensSchema

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

        if self.AuthTokens.query.filter_by(username=username,\
            token=auth_token).first():

            return { 'username':username, 'auth_token':auth_token }
        # else
        return None
