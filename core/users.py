#from . import app, db, CommonTable, CommonSchema
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
#from flask import current_app as app

from . import CommonAPI
from .utils import all_required_fields_dict


#def register_endpoint(app, rule, function, **options):
#    app.add_url_rule(rule, endpoint=function.__name__, view_func=function, **options)


class UsersAPI(CommonAPI):
    def __init__(self, app):
        super(UsersAPI, self).__init__(app)

        #self.app = app

        self.register_endpoint('/users/new', self.register_user, methods=['POST'])

        class Users(self.app.CommonTable):
            __tablename__ = 'users'

            username = Column(String, unique=True)
            password = Column(String)

        class UsersSchema(self.app.CommonSchema):
            #id = None
            username = fields.Str(validate=validators.validate_username)
            #password = fields.Str(load_only=True) # write-only field
            password = fields.Str() # write-only field

            @post_load
            def make_user(self, data):
                return Users(**data)

        self.app.Users = Users
        self.app.UsersSchema = UsersSchema

    #@app.route('/users/new', methods=['POST'])
    def register_user():
        required_fields = ['username', 'password']

        user_data = all_required_fields_dict(required_fields, request.form)

        if not user_data:
                abort(400)

        newuser = UsersSchema(many=False).load(user_data).data
        app.db.session.add(newuser)
        app.db.session.commit()
