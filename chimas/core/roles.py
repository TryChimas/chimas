import sqlalchemy as sqla

from marshmallow import fields, Schema

from flask import request

from . import CommonAPI

def rolestable_factory(commontable):
    class Roles(commontable):
        __tablename__ = 'roles'

        #id = None
        role = sqla.Column(sqla.String)
        arguments = sqla.Column(sqla.String) # FIXME: arguments is best if a json/dict,eg. {'board_id':'41'}
        username = sqla.Column(sqla.String)
    return Roles
    
class RolesAPI(CommonAPI):
    def __init__(self, app):
        super(RolesAPI, self).__init__(app)

        self.app = app

        api_endpoints = [
            ('/roles', self.list_roles, {'methods':['GET']}),
            ('/roles/<string:role>/<string:arguments>', self.fetch_role_info, {'methods':['GET']}),
            ('/roles/by_username/<string:username>', self.list_user_roles, {'methods':['GET']}) ]

        self.register_endpoints(api_endpoints)

        self.Roles = rolestable_factory(app.CommonTable)

    #@app.route('/roles', methods=['GET'])
    def list_roles(self):
        pass

    #@app.route('/roles/<string:role>/<string:arguments>', methods=['GET'])
    def fetch_role_info(self):
        pass

    #@app.route('/roles/by_username/<string:username>', methods=['GET'])
    def list_user_roles():
        pass

    #@app.route('/groups/addrole', methods=['POST']) # FIXME: PORTME!
    def add_role(self):
        pass
