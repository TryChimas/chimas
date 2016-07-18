from . import APP, DB, MA, CommonTable
#from . import Roles_Users

from flask.views import MethodView

from marshmallow.validate import Validator, ValidationError
from marshmallow import pre_load, post_load, validates_schema

from sqlalchemy import (
        Column,
        String,
        Integer,
        ForeignKey,
        DateTime )

from sqlalchemy import func

#from flask.ext.security import UserMixin

#from .roles import Roles, Roles_Users

class Users(CommonTable):
    __tablename__ = 'users'

    #id = Column(Integer, autoincrement=True, unique=True)
    #id = None
    #login = Column(String, primary_key=True, unique=True)
    login = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    #active = Column(String)
    #roles = DB.relationship('Roles', secondary="roles_users",
    #                        backref=DB.backref('users', lazy='dynamic'))


class UsersSchema(MA.ModelSchema):
    class Meta:
        model = Users

    @validates_schema
    def my_func(self):
        pass

    @pre_load
    def preload_values(self):
        pass

class UsersAPI(MethodView):
    def get(self):
        pass

    def post(self):
        pass

#posts_view = PostsAPI.as_view('posts_api')

#APP.add_url_rule('/topics/<string:board_id>', view_func=posts_view, methods=['GET', 'POST'])

#users_view = PostsAPI.as_view('users_api')
#APP.add_url_rule('/users/<string:board_id>', view_func=users_view, methods=['GET', 'POST'])
