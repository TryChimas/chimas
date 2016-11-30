from flask import request, abort

from sqlalchemy.orm import relationship
from marshmallow import fields, Schema

from . import CommonAPI

def threadstable_factory(poststable):
    class Threads(poststable):
        children = relationship("Threads", lazy='joined', join_depth=2)
    return Threads

def threadsschema_factory(postsschema):
    class ThreadsSchema(postsschema):
        children = fields.Nested('ThreadsSchema', many=True)
    return ThreadsSchema

class ThreadsAPI(CommonAPI):
    def __init__(self, app):
        super(ThreadsAPI, self).__init__(app)

        self.app = app

        api_endpoints = [
            ('/threads/<string:post_id>', self.get_thread, {'methods':['GET']}),
            ('/threads/<string:post_id>/tree', self.get_thread_tree, {'methods':['GET']}) ]

        self.register_endpoints(api_endpoints)

        # class Threads(self.app.posts.Posts):
        #     children = relationship("Threads", lazy='joined', join_depth=2)
        #
        # class ThreadsSchema(self.app.posts.PostsSchema):
        #     children = fields.Nested('ThreadsSchema', many=True)

        self.Threads = threadstable_factory(app.posts.Posts)
        self.ThreadsSchema = threadsschema_factory(app.posts.PostsSchema)

    #@app.route('/threads/<string:post_id>', methods=['GET'])
    def get_thread(self, post_id):
        parent_post = self.Threads.query.filter_by( id=post_id ).first()
        if not parent_post:
            abort(404)

        post_dump_json = self.ThreadsSchema().dumps(parent_post).data

        return post_dump_json

    #@app.route('/threads/<string:post_id>/tree', methods=['GET'])
    def get_thread_tree(self, post_id):
        return "getting thread tree for post id '{0}'\n".format(post_id)
