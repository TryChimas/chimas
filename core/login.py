from . import app, db, CommonTable

from sqlalchemy.orm import relationship, noload, joinedload
from marshmallow import fields, Schema

from flask import request, abort

from .users import Users, UsersSchema
from .authentication import AuthTokens, AuthTokensSchema

from os import urandom

from .utils import all_required_fields_dict

@app.route('/users/login', methods=['POST'])
def login_user():
    required_fields = ['username', 'password']

    user_req = all_required_fields_dict(required_fields, request.form)
    if not user_req:
            abort(400)

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

        new_token = AuthTokensSchema(many=False).load(token_data).data

        try:
            db.session.add(new_token)
            db.session.commit()
        except:
            abort(500)

        new_token_json = AuthTokensSchema(many=False).dumps(new_token).data
        return new_token_json

    else:
        # password sent by doesn't match the username.
        abort(401)

@app.route('/users/logout', methods=['POST'])
def unregister_user_token():
    required_fields = ['username', 'token']

    user_req = all_required_fields_dict(required_fields, request.form)
    if not user_req:
            abort(400)

    token_to_unregister = AuthTokens.query.filter_by( \
        username=user_req['username'], token=user_req['token'] ).\
        first()

    if not token_to_unregister:
        abort(404)

    db.session.delete(token_to_unregister)
    db.session.commit()

@app.route('/users/logoutall', methods=['POST'])
def unregister_all_user_tokens():
    required_fields = ['username'] # FIXME (maybe user:password instead)

    user_req = all_required_fields_dict(required_fields, request.form)
    if not user_req:
            abort(400)

    num_deleted = AuthTokens.query.\
        filter_by( username=user_req['username'] ).delete()
    db.session.commit()

    return "{0} tokens deleted.".format(num_deleted) # FIXME
