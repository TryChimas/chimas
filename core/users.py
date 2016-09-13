from . import APP, DB, CommonTable, CommonSchema
from . import validators

from sqlalchemy import (
        Column,
        String,
        Integer,
        ForeignKey,
        DateTime,
        func )

from marshmallow import fields, Schema, post_load

from flask import request, abort

class Users(CommonTable):
    __tablename__ = 'users'

    username = Column(String, unique=True)
    password = Column(String)

class UsersSchema(CommonSchema):
    #id = None
    username = fields.Str(validate=validators.validate_username)
    password = fields.Str(load_only=True) # write-only field

    @post_load
    def make_user(self, data):
        return Users(**data)

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
