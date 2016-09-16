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

class Groups(CommonTable):
    __tablename__ = 'groups'

    #id = None
    role = Column(String, primary_key=True, unique=True)
    arguments = Column(String) # FIXME: arguments is best if a json/dict,eg. {'board_id':'41'}
    username = Column(String)

@APP.route('/groups', methods=['GET'])
def list_groups():
    pass

@APP.route('/groups/<string:role>/<string:arguments>', methods=['GET'])
def fetch_group_info():
    pass

@APP.route('/groups/by_username/<string:username>', methods=['GET'])
def list_user_groups():
    pass

@APP.route('/groups/addrole', methods=['POST'])
def add_role():
    pass
