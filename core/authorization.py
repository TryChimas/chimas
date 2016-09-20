from . import APP, DB, CommonTable, CommonSchema

from sqlalchemy import (
        Column,
        String,
        Integer,
        ForeignKey,
        DateTime,
        func )

from functools import wraps

from flask import request, abort, make_response, g
from werkzeug.datastructures import Authorization

from .users import Users
from .boards import Boards
from .roles import Roles

import re

class ChimasAuthorization:

    def __init__(self):
        self.function_map = {}

    def verify_authorization(self):
        def actual_decorator(endpoint_function):
            @wraps(endpoint_function)
            def actual_function(*args, **kwargs):

                context = self.parse_request_context_data()

                has_authorization = self.verify_context(context)

                if not has_authorization:
                    abort(401)

                return endpoint_function(*args, **kwargs)

            return actual_function

        return actual_decorator

    def parse_request_context_data(self):
        # this function creates a uri for a endpoint's url rule.
        # this uri has the format "METHOD:dir1.dir2." where the
        # dots (.) mean variable, for example GET to /boards/1/topics/1000
        # has the context boards.topics. and GET /boards/1/topics/ has the
        # uri boards.topics. The context uri made by method+simplified_uri
        # makes it simple and deductible what the context refers to.
        #
        # we have 3 useful flask.request properties to use here:
        # request.endpoint, request.view_args and request.method
        # also we have g.is_authenticated and g.username

        # this transforms a GET to /boards/<string:board_id>/topics/<string:topic_id>
        # in a context string like "GET:boards.topics." DOT here means item/variable

        method = request.method.upper()
        endpoint_url_rule = request.url_rule.rule

        endpoint_uri = endpoint_url_rule.replace('/','')
        endpoint_uri = re.sub(r'\<.*?\>', '.', endpoint_uri)
        self.context = ":".join([ method, endpoint_uri ])

        return self.context

    def context(self, context):
        def function_wrapper(f):
            self.function_map[context] = f
            return f
        return function_wrapper

    def verify_context(self, context):
        func = self.function_map.get(context, None)
        if not func:
            abort(500)

        else:
            return func()

auth = ChimasAuthorization()

# read topic item
@auth.context('GET:boards.topics.')
def verify_boards_topics_item():
    return True

@auth.context('POST:posts.edit')
def edit_post():
    post_id = request.view_args['post_id']
    if Posts.query.filter_by( id=parent_id, author=g.username ).first():
        return True
    else:
        return False
