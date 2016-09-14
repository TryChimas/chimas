from . import APP, DB, CommonTable

from marshmallow import fields, Schema

from flask import request, abort

from .boards import Boards
from .posts import Posts, PostsSchema


#    topic_id = fields.Str()
#     reply_to_id = fields.Str()
#
#     board_id = fields.Str()
#     author_id = fields.Str()
#     title = fields.Str(validate=validators.post_title)
#     post_text = fields.Str(validate=validators.post_text)
#     hash_id = fields.Str()

@APP.route('/boards/<string:board_id>/topics/', methods=['GET'])
def list_board_topics(board_id):

    board_exists = Boards.query.filter_by( id=board_id ).first()
    if not board_exists:
        abort(404)

    board_topics = Posts.query.filter_by( board_id=board_id, reply_to_id='0' ).limit(3).all()

    topics_dump_json = PostsSchema(many=True).dumps(board_topics).data
    return topics_dump_json

@APP.route('/boards/<string:board_id>/topics/<string:topic_id>', methods=['GET'])
def show_topic(board_id, topic_id):

    board_exists = Boards.query.filter_by( id=board_id ).first()
    if not board_exists:
        abort(404)

    topic = Posts.query.filter_by( board_id=board_id, id=topic_id, reply_to_id='0' ).first()
    if not topic:
        abort(404)

    topic_dump_json = PostsSchema().dumps(topic).data
    return topic_dump_json

    #return "Showing topic '{0}' from board '{1}'\n".format(topic_id, board_id)

@APP.route('/boards/<string:board_id>/topics/', methods=['POST'])
def new_topic(board_id):

    board_exists = Boards.query.filter_by( id=board_id ).first()
    if not board_exists:
        abort(404)

    required_fields = ['title', 'post_text']

    post_data = {}
    for field in required_fields:
        if not request.form[field]:
            abort(400)
        else:
            post_data.update( { field : request.form[field] })

    post_data.update({
        'topic_id': '0',
        'reply_to_id': '0',
        'board_id': board_id,
        'author_id': 'admin',
        'hash_id': 'dUmMyHash'
    })

    newpost = PostsSchema(many=False).load(post_data).data
    DB.session.add(newpost)
    DB.session.commit()

    #return "Posting new topic to board '{0}'\n".format(board_id)
