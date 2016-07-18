from . import APP, DB, MA, CommonTable

from flask import request, abort
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

class Boards(CommonTable):
    __tablename__ = 'boards'

    id = None
    title = Column(String, primary_key=True, unique=True)
    description = Column(String)

class BoardsSchema(MA.ModelSchema):
    class Meta:
        model = Boards

class BoardsAPI(MethodView):

    def get(self):
        boards_schema = BoardsSchema(many=True)
        boards = Boards().query.all()
        return boards_schema.dumps(boards).data

    def post(self):
        pass

boards_view = BoardsAPI.as_view('boards_api')
APP.add_url_rule('/boards/', view_func=boards_view, methods=['GET', 'POST'])
