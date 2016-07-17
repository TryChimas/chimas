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

from flask.ext.security import RoleMixin

#class Roles_Users(CommonTable):
#    __tablename__ = 'roles_users'

#    user_id = Column(Integer, DB.ForeignKey('users.id'))
#    role_id = Column(Integer, DB.ForeignKey('roles.id'))

#class Groups(CommonTable):
#    __tablename__ = 'roles'

#    name = Column(String, primary_key=True, unique=True)
#    descriṕtion = Column(String)
#    users = Column(String)

#class Roles(CommonTable, RoleMixin):
#    __tablename__ = 'roles'

#    name = Column(String, primary_key=True, unique=True)
#    descriṕtion = Column(String)
#    users = Column(String, ForeignKey('users.login'))

#    def is_authorized(user, is_authenticated, allowed_roles, resource, method, lookup):
#        pass
