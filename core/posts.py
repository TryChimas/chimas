#from . import CommonTable, CommonSchema
from . import validators

from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship

from marshmallow import fields, Schema, post_load

from flask import request, abort, g
#from flask import current_app as app

#from .authorization import auth

from .utils import all_required_fields_dict

from . import CommonAPI

class PostsAPI(CommonAPI):

    def __init__(self, app):
        super(PostsAPI, self).__init__(app)

        #self.app = app

        api_endpoints = [
            ('/posts/<string:post_id>', self.fetch_post_only, {'methods':['GET']}),
            ('/posts/<string:post_id>/reply', self.reply_to_post, {'methods':['POST']}),
            ('/posts/<string:post_id>/edit', self.edit_post, {'methods':['POST']}),
            ('/posts/<string:post_id>/delete', self.delete_post, {'methods':['POST']}) ]

        self.register_endpoints(api_endpoints)

        class Posts(app.CommonTable):
            __tablename__ = 'posts'

            topic_id = Column(String)
            reply_to_id = Column(String, ForeignKey('posts.id'), default='0')

            board_id = Column(String)
            author_id = Column(String)
            title = Column(String)
            post_text = Column(String)
            hash_id = Column(String)

            #children = relationship("Posts", lazy='noload')

        class PostsSchema(app.CommonSchema):
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

        self.Posts = Posts
        self.PostsSchema = PostsSchema

    # get post
    #@app.route('/posts/<string:post_id>', methods=['GET'])
    def fetch_post_only(self, post_id):

        post = self.Posts.query.filter_by( id=post_id ).first()
        if not post:
            abort(404)

        post_data_json = self.PostsSchema().dumps(post).data

        return post_data_json

    # reply to post
    #@app.route('/posts/<string:post_id>/reply', methods=['POST'])
    def reply_to_post(self, post_id):

        post_to_reply_to = self.Posts.query.filter_by( id=post_id ).first()
        if not post_to_reply_to:
            abort(404)

        parent_post_data = self.PostsSchema().dump(post_to_reply_to).data

        # let's see if we reached max threading deepness or we can reply to the post
        # FIXME: write a better algorithm for this recursion

        MAX_THREADING_LEVEL = 3

        parent_id = parent_post_data['reply_to_id']
        count = 1

        # FIXME: write threading routines like this in utils.py
        while parent_id != 0:
            parent_id = self.PostsSchema().dump( self.Posts.query.filter_by( id=parent_id ).first() ).data['reply_to_id']
            if count >= MAX_THREADING_LEVEL:
                abort(400)
            count += 1

        required_fields = ['post_text']

        new_post_data = all_required_fields_dict(required_fields, request.form)

        if not new_post_data:
            abort(400)

        new_post_data.update({
            'title': 're {0}'.format(parent_post_data['title']),
            'topic_id': parent_post_data['topic_id'],
            'reply_to_id': parent_post_data['id'],
            'board_id': parent_post_data['board_id'],
            'author_id': g.username,
            'hash_id': 'dUmMyHash'
        })

        new_reply_post = self.PostsSchema(many=False).load(new_post_data).data
        self.db.session.add(new_reply_post)
        self.db.session.commit()

    # edit post #FIXME its not working
    #@auth.verify_authorization()
    #@app.route('/posts/<string:post_id>/edit', methods=['POST'])
    def edit_post(self, post_id):
        post_to_edit = self.Posts.query.filter_by( id=post_id ).first()
        if not post_to_edit:
            abort(404)

        post_dump = self.PostsSchema().dump(post_to_edit).data
        print(post_dump)
        required_fields = ['post_text']

        post_data = all_required_fields_dict(required_fields, request.form)

        if not post_data:
            abort(400)

        post_dump.update(post_data)
        print(post_dump)

        edited_post_obj = self.PostsSchema(many=False).load(post_dump).data
        self.db.session.add(edited_post_obj)
        self.db.session.commit()

        #return "editing post '{0}'\n".format(post_id)

    # delete post
    # FIXME: MEYBE DELETE THREAD, OR ONLY OBSCURATES THE DELETED POST
    # (soft delete)
    #@app.route('/posts/<string:post_id>/delete', methods=['POST'])
    def delete_post(self, post_id):
        post_to_be_deleted = self.Posts.query.filter_by( id=post_id ).first()
        if not post_to_be_deleted:
            abort(404)

        post_to_be_deleted.post_text = ""
        post_to_be_deleted.deleted = g.username

        self.db.session.add(post_to_be_deleted)
        self.db.session.commit()
        return "deleting post '{0}'\n".format(post_id)
