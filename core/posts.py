from . import APP, DB, MA, CommonTable

from .boards import Boards

from flask import request, abort
from flask.views import MethodView

from marshmallow.validate import Validator
from marshmallow import post_load

from sqlalchemy import (
        Column,
        String,
        Integer,
        ForeignKey,
        DateTime )

from sqlalchemy import func

class Posts(CommonTable):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    topic_id = Column(String) # FIXME: int is returning 422 when using python's requests
    reply_to_id = Column(String, default='0') # FIXME: int is returning 422 when using python's requests

    board_id = Column(String)
    author_id = Column(String)
    title = Column(String)
    post_text = Column(String)
    hash_id = Column(String)

#class PostsValidator(object):
#    def reply_to_id():


class PostsSchema(MA.ModelSchema):
    class Meta:
        model = Posts

        #    @validates_schema()
        #    def validate_schema(self, data):
        #        pass

#    @post_load
#    def return_obj(self, data):
#        return Posts(**data)

class PostsAPI(MethodView):

    def get(self, board_id):
        posts_schema = PostsSchema(many=True)
        from urllib.parse import unquote
        bid = unquote(board_id)
        posts = Posts().query.filter_by(board_id=bid, reply_to_id=0).all()

        from flask import jsonify
        return posts_schema.dumps(posts).data
        #pass

    def post(self, board_id):
        board = Boards().query.filter_by(title=board_id).first()
        if board == None:
            abort(404)

        from pprint import pprint
        print(request.form)
        if request.form['reply_to_id'] == '0':
            print("hello")

            data = {
                #'id':
                #'topic_id':
                'reply_to_id': '0',
                'board_id' : board_id,
                'author_id': 'TEST1NGAUTHOR',

                'title' : request.form['title'],
                'post_text' : request.form['text'],
                'hash_id': 'testinghash'
            }

            schema = PostsSchema()
            #result = schema.loads(request.form)
            result = schema.load(data)


            pprint(result.data)

            DB.session.add(result.data)
            DB.session.commit()

        return "hey"
        pass

posts_view = PostsAPI.as_view('posts_api')
APP.add_url_rule('/topics/<string:board_id>', view_func=posts_view, methods=['GET', 'POST'])
