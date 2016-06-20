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
