from . import APP, DB, CommonTable

from sqlalchemy.orm import relationship, noload, joinedload
from marshmallow import fields, Schema

from flask import request, abort

from .users import Users, UsersSchema
from .auth import AuthTokens, AuthTokensSchema

from os import urandom

@APP.route('/users/login', methods=['POST'])
def login_user():
    required_fields = ['username', 'password']

    user_req = {}
    for field in required_fields:
        if not request.form[field]:
            abort(400)
        else:
            user_req.update( { field : request.form[field] })

    user_logging_in = \
        Users.query.filter_by( username=user_req['username'] ).first()

    if not user_logging_in:
        abort(401)
    else:
         user_dump = UsersSchema(many=False).dump(user_logging_in).data

    if user_dump['password'] == user_req['password']: # FIXME

        the_token = urandom(32).hex() # FIXME
        token_data = {
            'username' : user_dump['username'],
            'token' : the_token,
            'expires': '66'
        }

        newtoken = AuthTokensSchema(many=False).load(token_data).data

        try:
            DB.session.add(newtoken)
            DB.session.commit()
        except:
            abort(500)

        new_token_json = AuthTokensSchema(many=False).dumps(newtoken).data
        return new_token_json

    else:
        # password sent by doesn't match the username.
        abort(401)

@APP.route('/users/logout', methods=['POST'])
def unregister_user_token():
    required_fields = ['username', 'token']

    user_req = {}
    for field in required_fields:
        if not request.form[field]:
            abort(400)
        else:
            user_req.update( { field : request.form[field] })

    token_to_unregister = AuthTokens.query.filter_by( \
        username=user_req['username'], token=user_req['token'] ).\
        first()

    if not token_to_unregister:
        abort(404)

    DB.session.delete(token_to_unregister)
    DB.session.commit()

@APP.route('/users/logoutall', methods=['POST'])
def unregister_all_user_tokens():
    required_fields = ['username'] # FIXME (maybe user:password instead)

    user_req = {}
    for field in required_fields:
        if not request.form[field]:
            abort(400)
        else:
            user_req.update( { field : request.form[field] })

    num_deleted = AuthTokens.query.\
        filter_by( username=user_req['username'] ).delete()

    DB.session.commit()

    return "{0}".format(num_deleted) # FIXME
