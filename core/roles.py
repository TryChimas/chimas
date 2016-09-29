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
#from flask import current_app as app

from . import CommonAPI

class RolesAPI(CommonAPI):
    def __init__(self, app):
        super(RolesAPI, self).__init__(app)

        #self.app = app
        self.register_endpoint('/roles', self.list_roles, methods=['GET'])
        self.register_endpoint('/roles/<string:role>/<string:arguments>', self.fetch_role_info, methods=['GET'])
        self.register_endpoint('/roles/by_username/<string:username>', self.list_user_roles, methods=['GET'])

        class Roles(app.CommonTable):
            __tablename__ = 'roles'

            #id = None
            role = Column(String)
            arguments = Column(String) # FIXME: arguments is best if a json/dict,eg. {'board_id':'41'}
            username = Column(String)

        self.Roles = Roles

    #@app.route('/roles', methods=['GET'])
    def list_roles():
        pass

    #@app.route('/roles/<string:role>/<string:arguments>', methods=['GET'])
    def fetch_role_info():
        pass

    #@app.route('/roles/by_username/<string:username>', methods=['GET'])
    def list_user_roles():
        pass

    @app.route('/groups/addrole', methods=['POST'])
    def add_role():
        pass
