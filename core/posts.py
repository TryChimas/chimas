from . import APP, DB, CommonTable, CommonSchema
from . import validators

from sqlalchemy import (
        Column,
        String,
        Integer,
        ForeignKey,
        DateTime,
        func )

from marshmallow import fields, Schema, post_load

from flask import request, abort

class Posts(CommonTable):
    __tablename__ = 'posts'

    #id = Column(Integer, primary_key=True, autoincrement=True)
    topic_id = Column(String)
    reply_to_id = Column(String, default='0')

    board_id = Column(String)
    author_id = Column(String)
    title = Column(String)
    post_text = Column(String)
    hash_id = Column(String)

@APP.route('/posts/<string:post_id>/reply', methods=['POST'])
def reply_to_post(post_id):
    return "replying to post '{0}'\n".format(post_id)

@APP.route('/posts/<string:post_id>/edit', methods=['POST'])
def edit_post(post_id):
    return "editing post '{0}'\n".format(post_id)

@APP.route('/posts/<string:post_id>/delete', methods=['POST'])
def delete_post(post_id):
    return "deleting post '{0}'\n".format(post_id)
