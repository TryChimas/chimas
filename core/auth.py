from eve.auth import BasicAuth
from flask import current_app as app
from flask import request as current_request

from core import Base
from core import Posts
from core import Users
from core import Roles

#from core import get_class_by_tablename

# this will be based on roles
# http://python-eve.org/authentication.html#role-based-access-control

class ChimasAuth(BasicAuth):

    def check_auth(self, login, password, allowed_roles, resource, method):

        if 'public' in allowed_roles:
            return True
            
        is_authenticated = False

        try:
            lookup = current_request.view_args
            (lookup_key, lookup_value) = lookup.popitem()
        except KeyError:
            lookup = None

        user = Users.query.filter(Users.login == login).first()

        if 'anonymous' in allowed_roles and login == "anon":
            return True

        if user and user.password == password:
            is_authenticated = True

        if 'registered' in allowed_roles and is_authenticated:
            if is_authenticated:
                return True

        if 'owner' in allowed_roles and is_authenticated and lookup != None:

            print(allowed_roles)

            #owner_column_name = 'author_id'

            posts = Posts.query.filter(Posts.author_id == login, Posts.id == lookup_value).first()

            if posts!= None:
                return True

            if login == 'admin' and is_authenticated:
                return True

        return False
