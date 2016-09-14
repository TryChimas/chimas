from . import APP, DB, CommonTable

from marshmallow import fields, Schema

from flask import request

from .posts import Posts, PostsSchema

class ThreadSchema(CommonSchema):
    topic_id = fields.Int()
    reply_to_id = fields.Int()

    board_id = fields.Str()
    author_id = fields.Str()
    title = fields.Str(validate=validators.post_title)
    post_text = fields.Str(validate=validators.post_text)
    hash_id = fields.Str()

    replies = fields.Nested(PostsSchema, many=True)

    @post_load
    def make_post(self, data):
        return Posts(**data)

@APP.route('/threads/<string:post_id>', methods=['GET'])
def get_thread(board_id):
    return "getting thread posts for post id '{0}'\n".format(post_id)

@APP.route('/threads/<string:post_id>/tree', methods=['GET'])
def get_thread_tree(board_id):
    return "getting thread tree for post id '{0}'\n".format(post_id)
