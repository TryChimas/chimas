from . import APP, MA, CommonTable

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
    reply_to_id = Column(String) # FIXME: int is returning 422 when using python's requests

    board_id = Column(String)
    author_id = Column(String)
    title = Column(String)
    post_text = Column(String)
    hash_id = Column(String)

class PostsSchema(MA.ModelSchema):
    class Meta:
        model = Posts

#class PostsSchema(MA.ModelSchema):

#    id = fields.Integer()
#    topic_id = fields.Integer()
#    reply_to_id = fields.Integer()

#    board_id = fields.String
#    author_id = fields.String
#    title = fields.String
#    post_text = fields.String
#    hash_id = fields.String

#@APP.route('/boards/<string:board_id>')
@APP.route('/topics/<string:board_id>', methods=['GET'])
def list_topics(board_id):
    posts_schema = PostsSchema(many=True)
    from urllib.parse import unquote
    bid = unquote(board_id)
    posts = Posts().query.filter_by(board_id=bid, reply_to_id=0).all()

    from flask import jsonify
    return posts_schema.dumps(posts).data


@APP.route('/topics/<string:board_id>', methods=['POST'])
def post_topic(board_id):
    posts_schema = PostsSchema()
    from urllib.parse import unquote
    bid = unquote(board_id)
    posts = Posts().query.filter_by(board_id=bid, reply_to_id=0).all()

    from flask import jsonify
    return posts_schema.dumps(posts).data

@APP.route('/posts/<int:topic_id>', methods=['GET'])
def get_topic(topic_id):
    posts_schema = PostsSchema(many=True)
    posts = Posts().query.filter_by(topic_id=topic_id).first()
    return posts
