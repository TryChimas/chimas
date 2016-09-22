from . import app, db, CommonTable, CommonSchema
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

from .utils import all_required_fields_dict

class Users(CommonTable):
    __tablename__ = 'users'

    username = Column(String, unique=True)
    password = Column(String)

class UsersSchema(CommonSchema):
    #id = None
    username = fields.Str(validate=validators.validate_username)
    #password = fields.Str(load_only=True) # write-only field
    password = fields.Str() # write-only field

    @post_load
    def make_user(self, data):
        return Users(**data)

@app.route('/users/new', methods=['POST'])
def register_user():
    required_fields = ['username', 'password']

    user_data = all_required_fields_dict(required_fields, request.form)

    if not user_data:
            abort(400)

    newuser = UsersSchema(many=False).load(user_data).data
    db.session.add(newuser)
    db.session.commit()
