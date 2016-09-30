#from flask import current_app as app

#from . import CommonTable, CommonSchema
from . import validators

from sqlalchemy import (
        Column,
        String,
        Integer,
        ForeignKey,
        DateTime,
        func )

from marshmallow import fields, Schema, post_load
import time, datetime

class TimeTokensAPI:
    def __init__(self, app):

        self.app = app

        class TimeTokens(app.CommonTable):
            __tablename__ = 'timetokens'

            tokentype = Column(String)
            value = Column(String)
            expires = Column(String) # seconds
            secret = Column(String)

        self.app.TimeTokens = TimeTokens

        # tokentypes can be:
        # 'validate_email_address', with 'value' == {'username':'myus3rname', 'mail':'mymail@host.fqdn'}
        # 'ip_can_register_again' with 'value' == "IP_ADDR" and 'expires' == 1 week (in seconds, 60*60*24*7)
        # 'ip_can_post_again' with 'value' == "IP_ADDR"
        # 'user_can_post_again' with 'value' == "username"
        # 'user_can_reply_again' with 'value' == "username"

        # may be of interest:
        # https://docs.python.org/3/library/datetime.html
        # https://docs.python.org/3/library/time.html
        # http://stackoverflow.com/questions/13370317/sqlalchemy-default-datetime

    def add_time_token(tokentype, value, expires):

            expires_datetime = datetime.fromtimestamp(time.time()+expires)
            TimeTokens.tokentype = tokentype
            TimeTokens.value = value
            TimeTokens.expires = expires_datetime
            TimeToken.secret = urandom(32).hex() # FIXME

            app.db.session.add(timetoken)
            app.db.session.commit()
