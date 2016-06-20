from . import APP, MA, CommonTable

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

#class BoardsSchema(CommonSchema):
class BoardsSchema(MA.ModelSchema):
    class Meta:
        model = Boards

@APP.route('/boards', methods=['GET'])
def list_boards():
    boards_schema = BoardsSchema(many=True)
    boards = Boards().query.all()
    return boards_schema.dumps(boards).data

@APP.route('/boards', methods=['POST'])
def new_boards_item():
    print(request.data)
    boards_schema = BoardsSchema()
    boards = Boards().query.all()
    return boards_schema.dumps(boards).data
