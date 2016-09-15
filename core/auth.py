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
                # Flask/Werkzeug do not recognize any authentication types
                # other than Basic or Digest, so here we parse the header by
                # hand
                try:
                    auth_type, token = request.headers['Authorization'].split(
                        None, 1)
                    auth = Authorization(auth_type, {'token': token})
                except ValueError:
                    # The Authorization header is either empty or has no token
                    pass

            # if the auth type does not match, we act as if there is no auth
            # this is better than failing directly, as it allows the callback
            # to handle special cases, like supporting multiple auth types
            if auth and auth.type.lower() != self.scheme.lower():
                auth = None

            # Flask normally handles OPTIONS requests on its own, but in the
            # case it is configured to forward those to the application, we
            # need to ignore authentication headers and let the request through
            # to avoid unwanted interactions with CORS.
            if request.method != 'OPTIONS':  # pragma: no cover
                if auth and auth.username:
                    password = self.get_password_callback(auth.username)
                else:
                    password = None
                #if not self.authenticate(auth, password):
                #    # Clear TCP receive buffer of any pending data
                #    request.data
                #    return self.auth_error_callback()

            return endpoint_function(*args, **kwargs)
        return decorated

auth = ChimasAuth(scheme='Token')
