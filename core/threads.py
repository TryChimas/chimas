from . import APP, DB, CommonTable

from marshmallow import fields, Schema

from flask import request

from .posts import Posts

@APP.route('/threads/<string:post_id>', methods=['GET'])
def get_thread(board_id):
    return "getting thread posts for post id '{0}'\n".format(post_id)

@APP.route('/threads/<string:post_id>/tree', methods=['GET'])
def get_thread_tree(board_id):
    return "getting thread tree for post id '{0}'\n".format(post_id)
