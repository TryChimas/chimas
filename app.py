from eve import Eve

from eve_sqlalchemy import SQL
from eve_sqlalchemy.validation import ValidatorSQL

from core.auth import ChimasAuth
from core import Base as Base

from core import CommonTable
from core import Users, Boards, Posts


app = Eve(settings='etc/eve-settings.py', auth=ChimasAuth, validator=ValidatorSQL, data=SQL)

#print("app.root_path: {0}\n".format(app.instance_path))

#db = app.data.driver
#Base.metadata.bind = db.engine
#db.Model = Base
#db.create_all()

Base.metadata.bind = app.data.driver.engine
app.data.driver.Model = Base
app.data.driver.create_all()

Base.query = app.data.driver.session.query_property()

methods_list = [ 'GET', 'HEAD', 'PATCH', 'POST', 'PUT', 'DELETE' ]
resources_list = ['boards', 'posts', 'users']

# http://python-eve.org/features.html#database-event-hooks
dbevent_list = ['fetched_resource', 'fetched_item', 'on_insert', 'on_inserted']

for each_method in methods_list:
    setattr(app, 'on_pre_{0}'.format(each_method), CommonTable.do_pre_method)
    setattr(app, 'on_post_{0}'.format(each_method), CommonTable.do_post_method)

if __name__ == "__main__":


    app.run();
