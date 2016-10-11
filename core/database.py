class DB:
    def __init__(self, db_file):
        self.engine = sqla.create_engine(db_file, echo=True)
        self.Base = declarative_base()
        self.session_factory = scoped_session(sessionmaker(bind=self.engine))
        self.session = self.session_factory()

        self.register_models()

    def create_all(self):
        self.Base.metadata.create_all(self.engine)

    def register_models(self):

        class CommonTable(db.Base):
            __abstract__ =  True

            id = sqla.Column(sqla.Integer, primary_key=True, unique=True, autoincrement=True)
            created = sqla.Column(sqla.DateTime, default = datetime.datetime.now) # FIXME: use timestamp here
            updated = sqla.Column(sqla.DateTime, default = datetime.datetime.now, onupdate = datetime.datetime.now)
            deleted = sqla.Column(sqla.String, default = 0)

            query = db.session_factory.query_property()

        class AuthTokens(CommonTable):
            __tablename__ = 'authtokens'

            id = None
            username = sqla.Column(sqla.String)
            token = sqla.Column(sqla.String, primary_key=True, unique=True, autoincrement=True)
            expires = sqla.Column(sqla.String)

        class Boards(CommonTable):
            __tablename__ = 'boards'

            #id = None
            title = sqla.Column(sqla.String, unique=True)
            description = sqla.Column(sqla.String)


        class Posts(CommonTable):
            __tablename__ = 'posts'

            topic_id = Column(String)
            reply_to_id = Column(String, ForeignKey('posts.id'), default='0')

            board_id = Column(String)
            author_id = Column(String)
            title = Column(String)
            post_text = Column(String)
            hash_id = Column(String)

            #children = relationship("Posts", lazy='noload')

        class Roles(CommonTable):
            __tablename__ = 'roles'

            #id = None
            role = sqla.Column(sqla.String)
            arguments = sqla.Column(sqla.String) # FIXME: arguments is best if a json/dict,eg. {'board_id':'41'}
            username = sqla.Column(sqla.String)

        class Threads(Posts):
            children = relationship("Threads", lazy='joined', join_depth=2)

        class TimeTokens(CommonTable):
            __tablename__ = 'timetokens'

            tokentype = sqla.Column(sqla.String)
            value = sqla.Column(sqla.String)
            expires = sqla.Column(sqla.String) # seconds
            secret = sqla.Column(sqla.String)

        class Topics(Posts):
            __tablename__ = 'posts'

            children = relationship("Topics", lazy='joined', join_depth=5)

        class Users(CommonTable):
            __tablename__ = 'users'

            username = sqla.Column(sqla.String, unique=True)
            password = sqla.Column(sqla.String)

        self.CommonTable = CommonTable
        self.AuthTokens = AuthTokens
        self.Boards = Boards
        self.Posts = Posts
        self.Roles = Roles
        self.Threads = Threads
        self.TimeTokens = TimeTokens
        self.Topics = Topics
        self.Users = Users
