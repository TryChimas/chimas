#import sys

#from flask import current_app as app
#from flask import request

from flask_httpauth import HTTPBasicAuth

from .users import Users

auth = HTTPBasicAuth()

@auth.get_password
def get_pw(username):
        this_user = Users().query.filter_by(login=username).first()
        if this_user:
            return this_user.password
        return None
