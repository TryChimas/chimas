import sys
sys.path.insert(1, sys.path[0]+'/inc/')


#print(sys.path)

#from eve import Eve

#from eve_sqlalchemy import SQL
#from eve_sqlalchemy.validation import ValidatorSQL

#from core.auth import ChimasAuth
#from core import Base as Base

#from core import CommonTable
#from core import Users, Boards, Posts

#from core.config import ConfigParser

#app = Eve(settings='etc/eve-settings.py', auth=ChimasAuth, validator=ValidatorSQL, data=SQL)
#ConfigParser(app)

#print(app.config)
#import pprint
#pprint.pprint(app.config, width=1)

from core import APP

#Base.metadata.bind = app.data.driver.engine
#app.data.driver.Model = Base
#app.data.driver.create_all()

#Base.query = app.data.driver.session.query_property()

if __name__ == "__main__":

    APP.run();
