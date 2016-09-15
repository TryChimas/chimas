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

class ChimasAuth(HTTPTokenAuth):
    def __init__(self, scheme='Token', realm=None):
        super(ChimasAuth, self).__init__(scheme=scheme, realm=realm)

        self.verify_token(self.check_token)

    #@super(ChimasAuth, self).verify_token
    def check_token(self, token):
        print('Good Morning')
        return False

    def verify_authorization(self, endpoint_function, roles_allowed=None):

        if not roles_allowed:
            abort(401)



def check_authorization(read_roles, write_roles):
    pass

auth = ChimasAuth(scheme='Token')
