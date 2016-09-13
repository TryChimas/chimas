from . import APP, DB, CommonTable, CommonSchema
from . import validators

from sqlalchemy import (
        Column,
        String,
        Integer,
        ForeignKey,
        DateTime,
        func )

from marshmallow import fields, Schema, post_load, validates, validates_schema

from flask import request, abort

#def validate_username(value):
#    from marshmallow.validate import Length as ValidateLength
#    from marshmallow.validate import Regexp as ValidateRegexp
#
#    ValidateLength(min=3,max=15).__call__(value)
#    ValidateRegexp(regex="^[a-zA-Z0-9_.-]+$").__call__(value)


class Users(CommonTable):
    __tablename__ = 'users'

    id = None
    username = Column(String, primary_key=True, unique=True)
    #email = Column(String, unique=True)
    password = Column(String)

class UsersSchema(CommonSchema):
    id = None
    username = fields.Str(validate=validators.validate_username)
    password = fields.Str(load_only=True) # write-only field

    @post_load
    def make_user(self, data):
        return Users(**data)

    #@validates('username')
    #validate_username = validates('username')(validate_username)
#    @validates('username')
#    def validate_username(self, value):
#        from marshmallow.validate import Length as ValidateLength
#        from marshmallow.validate import Regexp as ValidateRegexp
#
#        ValidateLength(min=3,max=15).__call__(value)
#        ValidateRegexp(regex="^[a-zA-Z0-9_.-]+$").__call__(value)
    #@validates_schema
    #def validate_users(self, data):
    #
    #    validate_username(data['username'])

@APP.route('/users/new', methods=['POST'])
def register_user():
    required_fields = ['username', 'password']

    user_data = {}
    for field in required_fields:
        if not request.form[field]:
            abort(400)
        else:
            user_data.update( { field : request.form[field] })

    #if request.form['username'] and request.form['password']:
    #user_data = { 'username': request.form['username'], 'password': request.form['password'] }
    newuser = UsersSchema(many=False).load(user_data).data
    #newuser = Users(username=request.form['username'], password=request.form['password'])
    DB.session.add(newuser)
    DB.session.commit()
