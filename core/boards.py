from . import APP, DB, CommonTable, CommonSchema
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

class Boards(CommonTable):
    __tablename__ = 'boards'

    #id = None
    title = Column(String, unique=True)
    description = Column(String)

class BoardsSchema(CommonSchema):
    title = fields.Str(validate=validators.board_title)
    description = fields.Str(validate=validators.board_description)

    @post_load
    def make_board(self, data):
        return Boards(**data)

@APP.route('/boards/new', methods=['POST'])
def create_board():
    required_fields = ['title', 'description']

    board_data = {}
    for field in required_fields:
        if not request.form[field]:
            abort(400)
        else:
            board_data.update( { field : request.form[field] })

    newboard = BoardsSchema(many=False).load(board_data).data
    DB.session.add(newboard)
    DB.session.commit()
