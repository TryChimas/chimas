from . import APP, DB, CommonTable

from marshmallow import fields, Schema

from flask import request

from .posts import Posts

@APP.route('/boards/<string:board_id>/topics/', methods=['GET'])
def list_board_topics(board_id):
    return "listing posts for '{0}'\n".format(board_id)

@APP.route('/boards/<string:board_id>/topics/<string:topic_id>', methods=['GET'])
def show_topic(board_id, topic_id):
    return "Showing topic '{0}' from board '{1}'\n".format(topic_id, board_id)

@APP.route('/boards/<string:board_id>/topics/', methods=['POST'])
def new_topic(board_id):
    return "Posting new topic to board '{0}'\n".format(board_id)
