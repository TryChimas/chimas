from . import APP, DB, CommonTable, CommonSchema

from flask_httpauth import HTTPTokenAuth

from werkzeug.http import parse_authorization_header

from .users import Users

#class AuthTokens(CommonTable):
#    __tablename__ = 'authtokens'

    #id = None
#    username = Column(String)
#    token = Column(String)
#    expires = Column(String)

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
                abort(401)

            print(auth['token']) #works
            return endpoint_function(*args, **kwargs)
        return decorated

auth = ChimasAuth(scheme='Token')
