#from . import, CommonTable

from sqlalchemy import (
        Column,
        String,
        Integer,
        ForeignKey,
        DateTime,
        func )

from marshmallow import fields, Schema

from flask import request
from flask import current_app as app

class Roles(app.CommonTable):
    __tablename__ = 'roles'

    #id = None
    role = Column(String)
    arguments = Column(String) # FIXME: arguments is best if a json/dict,eg. {'board_id':'41'}
    username = Column(String)

@app.route('/roles', methods=['GET'])
def list_roles():
    pass

@app.route('/roles/<string:role>/<string:arguments>', methods=['GET'])
def fetch_role_info():
    pass

@app.route('/roles/by_username/<string:username>', methods=['GET'])
def list_user_roles():
    pass

@app.route('/groups/addrole', methods=['POST'])
def add_role():
    pass
