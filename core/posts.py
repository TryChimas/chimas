from . import APP, DB, CommonTable

from .auth import auth
from .boards import Boards

from flask import request, abort
from flask.views import MethodView

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
    topic_id = Column(String)
    reply_to_id = Column(String, default='0')

    board_id = Column(String)
    author_id = Column(String)
    title = Column(String)
    post_text = Column(String)
    hash_id = Column(String)

class PostsAPI(MethodView):

    @auth.login_required
    def get(self, board_id):
        print('posts API [get]')

    def post(self, board_id):
        print('posts API [post]')

posts_view = PostsAPI.as_view('posts_api')
APP.add_url_rule('/topics/<string:board_id>', view_func=posts_view, methods=['GET', 'POST'])
