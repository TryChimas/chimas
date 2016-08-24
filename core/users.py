from . import APP, DB, CommonTable

from flask.views import MethodView

from sqlalchemy import (
        Column,
        String,
        Integer,
        ForeignKey,
        DateTime )

from sqlalchemy import func

class Users(CommonTable):
    __tablename__ = 'users'

    id = None
    login = Column(String, primary_key=True, unique=True)
    email = Column(String, unique=True)
    password = Column(String)

class UsersAPI(MethodView):
    def get(self):
        print('users API [get]')

    def post(self):
        print('users API [post]')

users_view = UsersAPI.as_view('users_api')
APP.add_url_rule('/topics/<string:board_id>', view_func=users_view, methods=['GET', 'POST'])
