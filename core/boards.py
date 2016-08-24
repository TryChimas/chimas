from . import APP, DB, CommonTable

from flask import request, abort
from flask.views import MethodView

from sqlalchemy import (
        Column,
        String,
        Integer,
        ForeignKey,
        DateTime )

from sqlalchemy import func

class Boards(CommonTable):
    __tablename__ = 'boards'

    id = None
    title = Column(String, primary_key=True, unique=True)
    description = Column(String)

class BoardsAPI(MethodView):

    def get(self):
        print('posts API [get]')

    def post(self):
        print('posts API [post]')

boards_view = BoardsAPI.as_view('boards_api')
APP.add_url_rule('/boards/', view_func=boards_view, methods=['GET', 'POST'])
