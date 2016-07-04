from . import APP, MA, CommonTable

from sqlalchemy import (
        Column,
        String,
        Integer,
        ForeignKey,
        DateTime )

from sqlalchemy import func

class Users(CommonTable):
    __tablename__ = 'users'

    #id = Column(Integer, autoincrement=True, unique=True)
    id = None
    login = Column(String, primary_key=True, unique=True)
    email = Column(String, unique=True)
    password = Column(String)

class UsersSchema(MA.ModelSchema):
    class Meta:
        model = Users

    @validates_schema
    def my_func(self):
        pass

    @pre_load
    def preload_values(self):
        pass

class UsersAPI(MethodView):
    def get(self):
        pass

    def post(self):
        pass

#posts_view = PostsAPI.as_view('posts_api')
#APP.add_url_rule('/topics/<string:board_id>', view_func=posts_view, methods=['GET', 'POST'])
