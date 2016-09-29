#from . import CommonTable, CommonSchema
from . import validators

from sqlalchemy import (
        Column,
        String,
        Integer,
        ForeignKey,
        DateTime,
        func )

from marshmallow import fields, Schema, post_load

from flask import request, abort
from . import CommonAPI


class BoardsAPI(CommonAPI):
    def __init__(self, app):
        super(BoardsAPI, self).__init__(app)

        #self.app = app

        api_endpoints = [
            ('/boards/new', self.create_board, {'methods':['POST']}) ]

        self.register_endpoints(api_endpoints)

        class Boards(app.CommonTable):
            __tablename__ = 'boards'

            #id = None
            title = Column(String, unique=True)
            description = Column(String)

        class BoardsSchema(app.CommonSchema):
            title = fields.Str(validate=validators.board_title)
            description = fields.Str(validate=validators.board_description)

            @post_load
            def make_board(self, data):
                return Boards(**data)
        self.Boards = Boards
        self.BoardsSchema = BoardsSchema

    #@app.route('/boards/new', methods=['POST'])
    def create_board():
        required_fields = ['title', 'description']

        board_data = all_required_fields_dict(required_fields, request.form)

        if not board_data:
            abort(400)

        new_board = BoardsSchema(many=False).load(board_data).data
        app.db.session.add(new_board)
        app.db.session.commit()
