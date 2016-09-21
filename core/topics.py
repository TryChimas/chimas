from . import APP, DB, CommonTable

from sqlalchemy.orm import relationship, noload, joinedload
from marshmallow import fields, Schema

from flask import request, abort
from flask import make_response as response

from .boards import Boards, BoardsSchema
from .posts import Posts, PostsSchema

from .authorization import auth

from .utils import board_id_exists, all_required_fields_dict

class Topics(Posts):
    __tablename__ = 'posts'

    children = relationship("Topics", lazy='joined', join_depth=5)

# list topics
@APP.route('/boards/<string:board_id>/topics/', methods=['GET'])
def list_board_topics(board_id):

    #board_exists = Boards.query.filter_by( id=board_id ).first()
    if not board_id_exists(board_id):
        abort(404)

    board_topics = Topics.query.\
            filter_by( board_id=board_id, reply_to_id='0' ).\
            order_by(Topics.created.desc()).\
            options(noload('children')).\
            limit(3).\
            all()

    topics_dump_json = PostsSchema(many=True).dumps(board_topics).data
    return response(topics_dump_json, 200)

# show topic
@APP.route('/boards/<string:board_id>/topics/<string:topic_id>', methods=['GET'])
#@authorization.verify_authorization(context="GET:boards.topics")
@auth.verify_authorization()
def show_topic(board_id, topic_id):

    if not board_id_exists(board_id):
        abort(404)

    topic = Topics.query.\
        filter_by( board_id=board_id, id=topic_id, reply_to_id='0' ).\
        order_by(Topics.created).\
        options(joinedload('children')).\
        enable_eagerloads(True).\
        first()
        #enable_eagerloads(True).\

    if not topic:
        abort(404)

    topic_dump_json = PostsSchema().dumps(topic).data
    return topic_dump_json

# FIXME: maybe change this endpoint to /topics/<boardname>
# as the board name is an abstraction into which topics (at least should)
# fit perfectly ?
# new topic
@APP.route('/boards/<string:board_id>/topics/', methods=['POST'])
def new_topic(board_id):

    if not board_id_exists(board_id):
        abort(404)

    required_fields = ['title', 'post_text']

    post_data = all_required_fields_dict(required_fields, request.form)
    if not post_data:
        abort(400)

    #post_data = {}
    #for field in required_fields:
    #    if not request.form[field]:
    #        abort(400)
    #    else:
    #        post_data.update( { field : request.form[field] })

    post_data.update({
        'topic_id': '0',
        'reply_to_id': '0',
        'board_id': board_id,
        'author_id': 'admin',
        'hash_id': 'dUmMyHash'
    })

    new_post = PostsSchema(many=False).load(post_data).data
    DB.session.add(new_post)
    DB.session.commit()
    new_post.topic_id = new_post.id
    DB.session.add(new_post)
    DB.session.commit()

    #return "Posting new topic to board '{0}'\n".format(board_id)
