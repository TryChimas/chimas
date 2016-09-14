from . import APP, DB, CommonTable, CommonSchema
from . import validators

from sqlalchemy import (
        Column,
        String,
        Integer,
        ForeignKey,
        DateTime,
        func )
from sqlalchemy.orm import relationship

from marshmallow import fields, Schema, post_load

from flask import request, abort

class Posts(CommonTable):
    __tablename__ = 'posts'

    topic_id = Column(String)
    reply_to_id = Column(String, ForeignKey('posts.id'), default='0')

    board_id = Column(String)
    author_id = Column(String)
    title = Column(String)
    post_text = Column(String)
    hash_id = Column(String)

    children = relationship("Posts", lazy='noload')

class PostsSchema(CommonSchema):
    topic_id = fields.Int()
    reply_to_id = fields.Int()

    board_id = fields.Str()
    author_id = fields.Str()
    title = fields.Str(validate=validators.post_title)
    post_text = fields.Str(validate=validators.post_text)
    hash_id = fields.Str()

    children = fields.Nested('PostsSchema', many=True)

    @post_load
    def make_post(self, data):
        return Posts(**data)

# reply to post
@APP.route('/posts/<string:post_id>/reply', methods=['POST'])
def reply_to_post(post_id):

    post_to_reply_to = Posts.query.filter_by( id=post_id ).first()
    if not post_to_reply_to:
        abort(404)

    post_dump = PostsSchema().dump(post_to_reply_to).data

    # let's see if we reached max threading deepness or we can reply to the post
    # FIXME: write a better algorithm for this recursion

    MAX_THREADING_LEVEL = 3

    parent_id = post_dump['reply_to_id']
    count = 1

    while parent_id != 0:
        parent_id = PostsSchema().dump( Posts.query.filter_by( id=parent_id ).first() ).data['reply_to_id']
        if count >= MAX_THREADING_LEVEL:
            abort(400)
        count += 1


    required_fields = ['post_text']

    post_data = {}
    for field in required_fields:
        if not request.form[field]:
            abort(400)
        else:
            post_data.update( { field : request.form[field] })

    if post_dump['reply_to_id'] == 0:
        this_topic_id = post_dump['id']
    else:
        this_topic_id = post_dump['topic_id']

    post_data.update({
        'title': 're {0}'.format(post_dump['title']),
        'topic_id': this_topic_id,
        'reply_to_id': post_dump['id'],
        'board_id': post_dump['board_id'],
        'author_id': 'admin',
        'hash_id': 'dUmMyHash'
    })

    newpost = PostsSchema(many=False).load(post_data).data
    DB.session.add(newpost)
    DB.session.commit()

# edit post
@APP.route('/posts/<string:post_id>/edit', methods=['POST'])
def edit_post(post_id):
    return "editing post '{0}'\n".format(post_id)

# delete post
@APP.route('/posts/<string:post_id>/delete', methods=['POST'])
def delete_post(post_id):
    return "deleting post '{0}'\n".format(post_id)
