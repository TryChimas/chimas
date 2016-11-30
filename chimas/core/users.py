from flask import request, abort

import sqlalchemy as sqla

from marshmallow import fields, Schema, post_load
from . import validators

#from . import CommonTable, CommonAPI
from . import CommonAPI
from .utils import all_required_fields_dict

def userstable_factory(commontable):
        class Users(commontable):
                __tablename__ = 'users'

                username = sqla.Column(sqla.String, unique=True)
                password = sqla.Column(sqla.String)

        return Users

def usersschema_factory(usersschema):
    class UsersSchema(usersschema):
        #id = None
        username = fields.Str(validate=validators.validate_username)
        #password = fields.Str(load_only=True) # write-only field
        password = fields.Str() # write-only field

        @post_load
        def make_user(self, data):
            return Users(**data)
    return UsersSchema

class UsersAPI(CommonAPI):

    def __init__(self, app):
        super(UsersAPI, self).__init__(app)

        #self.app = app
        api_endpoints = [
            ('/users/new', self.register_user, {'methods':['POST']}) ]

        self.register_endpoints(api_endpoints)

        #Users = UsersTable(self.app.CommonTable)

        #class Users(self.app.CommonTable):
        #    __tablename__ = 'users'

        #    username = sqla.Column(sqla.String, unique=True)
        #    password = sqla.Column(sqla.String)

        # class UsersSchema(self.app.CommonSchema):
        #     #id = None
        #     username = fields.Str(validate=validators.validate_username)
        #     #password = fields.Str(load_only=True) # write-only field
        #     password = fields.Str() # write-only field
        #
        #     @post_load
        #     def make_user(self, data):
        #         return Users(**data)

        #self.Users = Users
        self.Users = userstable_factory(app.CommonTable)
        self.UsersSchema = usersschema_factory(app.CommonSchema)

    #@app.route('/users/new', methods=['POST'])
    def register_user(self):
        required_fields = ['username', 'password']

        user_data = all_required_fields_dict(required_fields, request.form)

        if not user_data:
                abort(400)

        newuser = self.UsersSchema(many=False).load(user_data).data
        self.db.session.add(newuser)
        self.db.session.commit()
