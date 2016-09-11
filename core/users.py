from . import APP, DB, CommonTable

from sqlalchemy import (
        Column,
        String,
        Integer,
        ForeignKey,
        DateTime,
        func )

from marshmallow import fields, Schema, post_load

from flask import request

class Users(CommonTable):
    __tablename__ = 'users'

    id = None
    username = Column(String, primary_key=True, unique=True)
    #email = Column(String, unique=True)
    password = Column(String)

class UsersSchema(Schema):
    username = fields.Str()
    password = fields.Str()

    created = fields.DateTime()
    updated = fields.DateTime()

    @post_load
    def make_user(self, data):
        return Users(**data)

@APP.route('/users/new', methods=['POST'])
def register_user():
    if request.form['username'] and request.form['password']:
            user_data = { 'username': request.form['username'], 'password': request.form['password'] }
            newuser = UsersSchema(many=False).load(user_data).data
            #newuser = Users(username=request.form['username'], password=request.form['password'])
            DB.session.add(newuser)
            DB.session.commit()
