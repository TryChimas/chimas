from . import APP, DB, CommonTable

from sqlalchemy import (
        Column,
        String,
        Integer,
        ForeignKey,
        DateTime,
        func )

from marshmallow import fields, Schema

from flask import request

class Roles(CommonTable):
    __tablename__ = 'roles'

    #id = None
    role = Column(String)
    arguments = Column(String) # FIXME: arguments is best if a json/dict,eg. {'board_id':'41'}
    username = Column(String)

@APP.route('/roles', methods=['GET'])
def list_roles():
    pass

@APP.route('/roles/<string:role>/<string:arguments>', methods=['GET'])
def fetch_role_info():
    pass

@APP.route('/roles/by_username/<string:username>', methods=['GET'])
def list_user_roles():
    pass

@APP.route('/groups/addrole', methods=['POST'])
def add_role():
    pass
