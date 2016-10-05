#!/usr/bin/env python

from core import ROOT_PATH, Chimas

import core

Chimas = core.Chimas

from werkzeug.wsgi import DispatcherMiddleware

# run by script
if __name__ == "__main__":
    from werkzeug.serving import run_simple

    #if os.path(ROOT_PATH)
    app1 = Chimas(instance='bbs1')
    app2 = Chimas(instance='bbs2')

    #app.run()
    bbs_dispatcher =\
        DispatcherMiddleware(
            None,
            {
                '/um' : app1,
                '/two' : app2
            })

    run_simple('127.0.0.1', 41345, bbs_dispatcher)
