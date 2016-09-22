import sys
#sys.path.insert(1, sys.path[0]+'/inc/')

from core import Chimas
from werkzeug.wsgi import DispatcherMiddleware

if __name__ == "__main__":
    #import pprint
    #pprint.pprint(app.config, width=1)
    from werkzeug.serving import run_simple

    import copy
    app = Chimas()
    #app.run()
    dmid = DispatcherMiddleware( None, {'/iagoo' : app} );
    run_simple('127.0.0.1', 41345, dmid)
