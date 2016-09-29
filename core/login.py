#from . import, CommonTable
#from flask import current_app as app

from sqlalchemy.orm import relationship, noload, joinedload
from marshmallow import fields, Schema

from flask import request, abort

#from .users import Users, UsersSchema
#from .authentication import AuthTokens, AuthTokensSchema

from os import urandom

from . import CommonAPI

from .utils import all_required_fields_dict

from functools import wraps

#def register_endpoint(app, rule, function, **options):
#    app.add_url_rule(rule, endpoint=function.__name__, view_func=function, **options)

class LoginAPI(CommonAPI):
    def __init__(self, app):
        super(LoginAPI, self).__init__(app)
        #self.app = app

        api_endpoints = [
            ('/users/login', self.login_user, {'methods':['POST']})
        ]

        self.register_endpoints(api_endpoints)
        #self.register_endpoint('/users/login', self.login_user, methods=['POST'])

    def login_user(self):
        required_fields = ['username', 'password']

        user_req = all_required_fields_dict(required_fields, request.form)
        if not user_req:
                abort(400)

        user_logging_in = \
            self.app.Users.query.filter_by( username=user_req['username'] ).first()

        if not user_logging_in:
            abort(401)
        else:
             user_dump = self.app.UsersSchema(many=False).dump(user_logging_in).data

        if user_dump['password'] == user_req['password']: # FIXME

            the_token = urandom(32).hex() # FIXME
            token_data = {
                'username' : user_dump['username'],
                'token' : the_token,
                'expires': '66'
            }

            new_token = AuthTokensSchema(many=False).load(token_data).data

            try:
                app.db.session.add(new_token)
                app.db.session.commit()
            except:
                abort(500)

            new_token_json = AuthTokensSchema(many=False).dumps(new_token).data
            return new_token_json

        else:
            # password sent by doesn't match the username.
            abort(401)

    #@__self__.app.route('/users/logout', methods=['POST'])
    def unregister_user_token(self):
        required_fields = ['username', 'token']

        user_req = all_required_fields_dict(required_fields, request.form)
        if not user_req:
                abort(400)

        token_to_unregister = AuthTokens.query.filter_by( \
            username=user_req['username'], token=user_req['token'] ).\
            first()

        if not token_to_unregister:
            abort(404)

        app.db.session.delete(token_to_unregister)
        app.db.session.commit()

    #@__self__.app.route('/users/logoutall', methods=['POST'])
    def unregister_all_user_tokens(self):
        required_fields = ['username'] # FIXME (maybe user:password instead)

        user_req = all_required_fields_dict(required_fields, request.form)
        if not user_req:
                abort(400)

        num_deleted = AuthTokens.query.\
            filter_by( username=user_req['username'] ).delete()
        app.db.session.commit()

        return "{0} tokens deleted.".format(num_deleted) # FIXME
