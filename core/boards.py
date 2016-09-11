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

class Boards(CommonTable):
    __tablename__ = 'boards'

    id = None
    title = Column(String, primary_key=True, unique=True)
    description = Column(String)

@APP.route('/boards/new', methods=['POST'])
def create_board():
    if request.form['title'] and request.form['description']:
            newboard = Boards(title=request.form['title'], description=request.form['description'])
            DB.session.add(newboard)
            DB.session.commit()
