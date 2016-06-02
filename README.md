# CHIMAS BBS API

This project has in mind to develop a modularized, extensible and easily maintainable API-based forum, so that it can be used with standalone clients for example: command line interface, tui, telnet and web.

### Dependencies:

* Python EVE ([docs](http://python-eve.org/))
* Eve SQLAlchemy extension ([docs](https://eve-sqlalchemy.readthedocs.io/))
* SQLAlchemy ([website](http://www.sqlalchemy.org/) / [docs](http://docs.sqlalchemy.org/en/rel_1_0/))
* Cerberus ([website](http://python-cerberus.org/) / [github](https://github.com/nicolaiarocci/cerberus))
* Flask ([website](http://flask.pocoo.org/) / [github](https://github.com/pallets/flask))

### Good to know

Default port is 41345 (ximas)

### License

Licensed Under GPL v.3

tree:

```.
├── 000-standards-philosophy.md
├── 001-layer-sketching.md
├── 002-preparing-readme.md
├── 004-versioning-and-development.md
├── 005-protocol-design.md
├── 006-multiple-forums.md
├── 007-roles.md
├── 008-post-formatting.md
├── chimas
│   ├── app.py
│   ├── core
│   │   ├── auth.py
│   │   ├── db.py
│   │   ├── __init__.py
│   │   └── schemas
│   │       ├── boards.py
│   │       ├── posts.py
│   │       └── users.py
│   └── etc
│       └── eve-settings.py
├── MANIFEST
├── README.md
├── setup.py
└── utils
    └── populate-sqlite.py
5 directories, 20 files
```
.
├── app.py
├── core
│   ├── auth.py
│   ├── config.py
│   ├── db.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── auth.cpython-35.pyc
│   │   └── __init__.cpython-35.pyc
│   └── schemas
│       ├── boards.py
│       ├── posts.py
│       ├── __pycache__
│       │   ├── boards.cpython-35.pyc
│       │   ├── posts.cpython-35.pyc
│       │   └── users.cpython-35.pyc
│       └── users.py
├── dummy.sqlite3-autocreate
├── etc
│   ├── chimas-default.conf
│   ├── eve-settings.py
│   └── eve-settings.py-UPDATEE-THE-NEW
├── inc
│   ├── bson
│   │   ├── binary.py
│   │   ├── buffer.c
│   │   ├── buffer.h
│   │   ├── _cbsonmodule.c
│   │   ├── _cbsonmodule.h
│   │   ├── codec_options.py
│   │   ├── code.py
│   │   ├── dbref.py
│   │   ├── encoding_helpers.c
│   │   ├── encoding_helpers.h
│   │   ├── errors.py
│   │   ├── __init__.py
│   │   ├── int64.py
│   │   ├── json_util.py
│   │   ├── max_key.py
│   │   ├── min_key.py
│   │   ├── objectid.py
│   │   ├── py3compat.py
│   │   ├── __pycache__
│   │   │   ├── binary.cpython-35.pyc
│   │   │   ├── codec_options.cpython-35.pyc
│   │   │   ├── code.cpython-35.pyc
│   │   │   ├── dbref.cpython-35.pyc
│   │   │   ├── errors.cpython-35.pyc
│   │   │   ├── __init__.cpython-35.pyc
│   │   │   ├── int64.cpython-35.pyc
│   │   │   ├── json_util.cpython-35.pyc
│   │   │   ├── max_key.cpython-35.pyc
│   │   │   ├── min_key.cpython-35.pyc
│   │   │   ├── objectid.cpython-35.pyc
│   │   │   ├── py3compat.cpython-35.pyc
│   │   │   ├── raw_bson.cpython-35.pyc
│   │   │   ├── regex.cpython-35.pyc
│   │   │   ├── son.cpython-35.pyc
│   │   │   ├── timestamp.cpython-35.pyc
│   │   │   └── tz_util.cpython-35.pyc
│   │   ├── raw_bson.py
│   │   ├── regex.py
│   │   ├── son.py
│   │   ├── time64.c
│   │   ├── time64_config.h
│   │   ├── time64.h
│   │   ├── time64_limits.h
│   │   ├── timestamp.py
│   │   └── tz_util.py
│   ├── cerberus
│   │   ├── cerberus.py
│   │   ├── errors.py
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── cerberus.cpython-35.pyc
│   │   │   ├── errors.cpython-35.pyc
│   │   │   └── __init__.cpython-35.pyc
│   │   └── tests
│   │       ├── __init__.py
│   │       └── tests.py
│   ├── click
│   │   ├── _bashcomplete.py
│   │   ├── _compat.py
│   │   ├── core.py
│   │   ├── decorators.py
│   │   ├── exceptions.py
│   │   ├── formatting.py
│   │   ├── globals.py
│   │   ├── __init__.py
│   │   ├── parser.py
│   │   ├── __pycache__
│   │   │   ├── _compat.cpython-35.pyc
│   │   │   ├── core.cpython-35.pyc
│   │   │   ├── decorators.cpython-35.pyc
│   │   │   ├── exceptions.cpython-35.pyc
│   │   │   ├── formatting.cpython-35.pyc
│   │   │   ├── globals.cpython-35.pyc
│   │   │   ├── __init__.cpython-35.pyc
│   │   │   ├── parser.cpython-35.pyc
│   │   │   ├── termui.cpython-35.pyc
│   │   │   ├── types.cpython-35.pyc
│   │   │   ├── _unicodefun.cpython-35.pyc
│   │   │   └── utils.cpython-35.pyc
│   │   ├── _termui_impl.py
│   │   ├── termui.py
│   │   ├── testing.py
│   │   ├── _textwrap.py
│   │   ├── types.py
│   │   ├── _unicodefun.py
│   │   ├── utils.py
│   │   └── _winconsole.py
│   ├── eve
│   │   ├── auth.py
│   │   ├── default_settings.py
│   │   ├── defaults.py
│   │   ├── endpoints.py
│   │   ├── exceptions.py
│   │   ├── flaskapp.py
│   │   ├── __init__.py
│   │   ├── io
│   │   │   ├── base.py
│   │   │   ├── __init__.py
│   │   │   ├── media.py
│   │   │   ├── mongo
│   │   │   │   ├── geo.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── media.py
│   │   │   │   ├── mongo.py
│   │   │   │   ├── parser.py
│   │   │   │   ├── __pycache__
│   │   │   │   │   ├── geo.cpython-35.pyc
│   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   ├── media.cpython-35.pyc
│   │   │   │   │   ├── mongo.cpython-35.pyc
│   │   │   │   │   ├── parser.cpython-35.pyc
│   │   │   │   │   └── validation.cpython-35.pyc
│   │   │   │   └── validation.py
│   │   │   └── __pycache__
│   │   │       ├── base.cpython-35.pyc
│   │   │       ├── __init__.cpython-35.pyc
│   │   │       └── media.cpython-35.pyc
│   │   ├── logging.py
│   │   ├── methods
│   │   │   ├── common.py
│   │   │   ├── delete.py
│   │   │   ├── get.py
│   │   │   ├── __init__.py
│   │   │   ├── patch.py
│   │   │   ├── post.py
│   │   │   ├── put.py
│   │   │   └── __pycache__
│   │   │       ├── common.cpython-35.pyc
│   │   │       ├── delete.cpython-35.pyc
│   │   │       ├── get.cpython-35.pyc
│   │   │       ├── __init__.cpython-35.pyc
│   │   │       ├── patch.cpython-35.pyc
│   │   │       ├── post.cpython-35.pyc
│   │   │       └── put.cpython-35.pyc
│   │   ├── __pycache__
│   │   │   ├── auth.cpython-35.pyc
│   │   │   ├── defaults.cpython-35.pyc
│   │   │   ├── default_settings.cpython-35.pyc
│   │   │   ├── endpoints.cpython-35.pyc
│   │   │   ├── exceptions.cpython-35.pyc
│   │   │   ├── flaskapp.cpython-35.pyc
│   │   │   ├── __init__.cpython-35.pyc
│   │   │   ├── logging.cpython-35.pyc
│   │   │   ├── render.cpython-35.pyc
│   │   │   ├── utils.cpython-35.pyc
│   │   │   ├── validation.cpython-35.pyc
│   │   │   └── versioning.cpython-35.pyc
│   │   ├── render.py
│   │   ├── tests
│   │   │   ├── auth.py
│   │   │   ├── config.py
│   │   │   ├── default_values.py
│   │   │   ├── endpoints.py
│   │   │   ├── __init__.py
│   │   │   ├── io
│   │   │   │   ├── __init__.py
│   │   │   │   ├── media.py
│   │   │   │   ├── mongo.py
│   │   │   │   └── multi_mongo.py
│   │   │   ├── logging.py
│   │   │   ├── methods
│   │   │   │   ├── common.py
│   │   │   │   ├── delete.py
│   │   │   │   ├── get.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── patch.py
│   │   │   │   ├── post.py
│   │   │   │   ├── put.py
│   │   │   │   └── ratelimit.py
│   │   │   ├── renders.py
│   │   │   ├── response.py
│   │   │   ├── test.db
│   │   │   ├── test_prefix.py
│   │   │   ├── test_prefix_version.py
│   │   │   ├── test_settings.py
│   │   │   ├── test_version.py
│   │   │   ├── utils.py
│   │   │   └── versioning.py
│   │   ├── utils.py
│   │   ├── validation.py
│   │   └── versioning.py
│   ├── events
│   │   ├── events.py
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── events.cpython-35.pyc
│   │   │   └── __init__.cpython-35.pyc
│   │   └── tests
│   │       ├── __init__.py
│   │       └── tests.py
│   ├── eve_sqlalchemy
│   │   ├── decorators.py
│   │   ├── __init__.py
│   │   ├── media.py
│   │   ├── parser.py
│   │   ├── __pycache__
│   │   │   ├── decorators.cpython-35.pyc
│   │   │   ├── __init__.cpython-35.pyc
│   │   │   ├── parser.cpython-35.pyc
│   │   │   ├── structures.cpython-35.pyc
│   │   │   ├── utils.cpython-35.pyc
│   │   │   └── validation.cpython-35.pyc
│   │   ├── structures.py
│   │   ├── tests
│   │   │   ├── delete.py
│   │   │   ├── get.py
│   │   │   ├── __init__.py
│   │   │   ├── patch.py
│   │   │   ├── post.py
│   │   │   ├── put.py
│   │   │   ├── sql.py
│   │   │   ├── test_association_proxy.py
│   │   │   ├── test_settings_sql.py
│   │   │   ├── test_sql_tables.py
│   │   │   ├── test_validation_allow_unknown.py
│   │   │   ├── test_validation.py
│   │   │   └── utils.py
│   │   ├── utils.py
│   │   └── validation.py
│   ├── flask
│   │   ├── app.py
│   │   ├── blueprints.py
│   │   ├── _compat.py
│   │   ├── config.py
│   │   ├── ctx.py
│   │   ├── debughelpers.py
│   │   ├── ext
│   │   │   ├── __init__.py
│   │   │   └── __pycache__
│   │   │       └── __init__.cpython-35.pyc
│   │   ├── exthook.py
│   │   ├── globals.py
│   │   ├── helpers.py
│   │   ├── __init__.py
│   │   ├── json.py
│   │   ├── logging.py
│   │   ├── module.py
│   │   ├── __pycache__
│   │   │   ├── app.cpython-35.pyc
│   │   │   ├── blueprints.cpython-35.pyc
│   │   │   ├── cli.cpython-35.pyc
│   │   │   ├── _compat.cpython-35.pyc
│   │   │   ├── config.cpython-35.pyc
│   │   │   ├── ctx.cpython-35.pyc
│   │   │   ├── debughelpers.cpython-35.pyc
│   │   │   ├── exthook.cpython-35.pyc
│   │   │   ├── globals.cpython-35.pyc
│   │   │   ├── helpers.cpython-35.pyc
│   │   │   ├── __init__.cpython-35.pyc
│   │   │   ├── json.cpython-35.pyc
│   │   │   ├── logging.cpython-35.pyc
│   │   │   ├── module.cpython-35.pyc
│   │   │   ├── sessions.cpython-35.pyc
│   │   │   ├── signals.cpython-35.pyc
│   │   │   ├── templating.cpython-35.pyc
│   │   │   └── wrappers.cpython-35.pyc
│   │   ├── sessions.py
│   │   ├── signals.py
│   │   ├── templating.py
│   │   ├── testing.py
│   │   ├── testsuite
│   │   │   ├── appctx.py
│   │   │   ├── basic.py
│   │   │   ├── blueprints.py
│   │   │   ├── config.py
│   │   │   ├── deprecations.py
│   │   │   ├── examples.py
│   │   │   ├── ext.py
│   │   │   ├── helpers.py
│   │   │   ├── __init__.py
│   │   │   ├── regression.py
│   │   │   ├── reqctx.py
│   │   │   ├── signals.py
│   │   │   ├── static
│   │   │   │   └── index.html
│   │   │   ├── subclassing.py
│   │   │   ├── templates
│   │   │   │   ├── context_template.html
│   │   │   │   ├── escaping_template.html
│   │   │   │   ├── _macro.html
│   │   │   │   ├── mail.txt
│   │   │   │   ├── nested
│   │   │   │   │   └── nested.txt
│   │   │   │   ├── simple_template.html
│   │   │   │   ├── template_filter.html
│   │   │   │   └── template_test.html
│   │   │   ├── templating.py
│   │   │   ├── test_apps
│   │   │   │   ├── blueprintapp
│   │   │   │   │   ├── apps
│   │   │   │   │   │   ├── admin
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── static
│   │   │   │   │   │   │   │   ├── css
│   │   │   │   │   │   │   │   │   └── test.css
│   │   │   │   │   │   │   │   └── test.txt
│   │   │   │   │   │   │   └── templates
│   │   │   │   │   │   │       └── admin
│   │   │   │   │   │   │           └── index.html
│   │   │   │   │   │   ├── frontend
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   └── templates
│   │   │   │   │   │   │       └── frontend
│   │   │   │   │   │   │           └── index.html
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   └── __init__.py
│   │   │   │   ├── config_module_app.py
│   │   │   │   ├── config_package_app
│   │   │   │   │   └── __init__.py
│   │   │   │   ├── flask_broken
│   │   │   │   │   ├── b.py
│   │   │   │   │   └── __init__.py
│   │   │   │   ├── flaskext
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── oldext_package
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   └── submodule.py
│   │   │   │   │   └── oldext_simple.py
│   │   │   │   ├── flask_newext_package
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   └── submodule.py
│   │   │   │   ├── flask_newext_simple.py
│   │   │   │   ├── importerror.py
│   │   │   │   ├── lib
│   │   │   │   │   └── python2.5
│   │   │   │   │       └── site-packages
│   │   │   │   │           ├── site_app.py
│   │   │   │   │           ├── SiteEgg.egg
│   │   │   │   │           └── site_package
│   │   │   │   │               └── __init__.py
│   │   │   │   ├── main_app.py
│   │   │   │   ├── moduleapp
│   │   │   │   │   ├── apps
│   │   │   │   │   │   ├── admin
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── static
│   │   │   │   │   │   │   │   ├── css
│   │   │   │   │   │   │   │   │   └── test.css
│   │   │   │   │   │   │   │   └── test.txt
│   │   │   │   │   │   │   └── templates
│   │   │   │   │   │   │       └── index.html
│   │   │   │   │   │   ├── frontend
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   └── templates
│   │   │   │   │   │   │       └── index.html
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   └── __init__.py
│   │   │   │   ├── path
│   │   │   │   │   └── installed_package
│   │   │   │   │       └── __init__.py
│   │   │   │   └── subdomaintestmodule
│   │   │   │       ├── __init__.py
│   │   │   │       └── static
│   │   │   │           └── hello.txt
│   │   │   ├── testing.py
│   │   │   └── views.py
│   │   ├── views.py
│   │   └── wrappers.py
│   ├── flask_pymongo
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-35.pyc
│   │   │   └── wrappers.cpython-35.pyc
│   │   └── wrappers.py
│   ├── flask_sqlalchemy
│   │   ├── _compat.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── _compat.cpython-35.pyc
│   │       └── __init__.cpython-35.pyc
│   ├── gridfs
│   │   ├── errors.py
│   │   ├── grid_file.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── errors.cpython-35.pyc
│   │       ├── grid_file.cpython-35.pyc
│   │       └── __init__.cpython-35.pyc
│   ├── itsdangerous.py
│   ├── jinja2
│   │   ├── bccache.py
│   │   ├── _compat.py
│   │   ├── compiler.py
│   │   ├── constants.py
│   │   ├── debug.py
│   │   ├── defaults.py
│   │   ├── environment.py
│   │   ├── exceptions.py
│   │   ├── ext.py
│   │   ├── filters.py
│   │   ├── __init__.py
│   │   ├── lexer.py
│   │   ├── loaders.py
│   │   ├── meta.py
│   │   ├── nodes.py
│   │   ├── optimizer.py
│   │   ├── parser.py
│   │   ├── __pycache__
│   │   │   ├── bccache.cpython-35.pyc
│   │   │   ├── _compat.cpython-35.pyc
│   │   │   ├── compiler.cpython-35.pyc
│   │   │   ├── defaults.cpython-35.pyc
│   │   │   ├── environment.cpython-35.pyc
│   │   │   ├── exceptions.cpython-35.pyc
│   │   │   ├── filters.cpython-35.pyc
│   │   │   ├── __init__.cpython-35.pyc
│   │   │   ├── lexer.cpython-35.pyc
│   │   │   ├── loaders.cpython-35.pyc
│   │   │   ├── nodes.cpython-35.pyc
│   │   │   ├── optimizer.cpython-35.pyc
│   │   │   ├── parser.cpython-35.pyc
│   │   │   ├── runtime.cpython-35.pyc
│   │   │   ├── _stringdefs.cpython-35.pyc
│   │   │   ├── tests.cpython-35.pyc
│   │   │   ├── utils.cpython-35.pyc
│   │   │   └── visitor.cpython-35.pyc
│   │   ├── runtime.py
│   │   ├── sandbox.py
│   │   ├── _stringdefs.py
│   │   ├── tests.py
│   │   ├── utils.py
│   │   └── visitor.py
│   ├── markupsafe
│   │   ├── _compat.py
│   │   ├── _constants.py
│   │   ├── __init__.py
│   │   ├── _native.py
│   │   ├── __pycache__
│   │   │   ├── _compat.cpython-35.pyc
│   │   │   ├── __init__.cpython-35.pyc
│   │   │   └── _native.cpython-35.pyc
│   │   ├── _speedups.c
│   │   └── tests.py
│   ├── __pycache__
│   │   └── itsdangerous.cpython-35.pyc
│   ├── pymongo
│   │   ├── auth.py
│   │   ├── bulk.py
│   │   ├── client_options.py
│   │   ├── _cmessagemodule.c
│   │   ├── collection.py
│   │   ├── command_cursor.py
│   │   ├── common.py
│   │   ├── cursor_manager.py
│   │   ├── cursor.py
│   │   ├── database.py
│   │   ├── errors.py
│   │   ├── helpers.py
│   │   ├── __init__.py
│   │   ├── ismaster.py
│   │   ├── message.py
│   │   ├── mongo_client.py
│   │   ├── mongo_replica_set_client.py
│   │   ├── monitoring.py
│   │   ├── monitor.py
│   │   ├── monotonic.py
│   │   ├── network.py
│   │   ├── operations.py
│   │   ├── periodic_executor.py
│   │   ├── pool.py
│   │   ├── __pycache__
│   │   │   ├── auth.cpython-35.pyc
│   │   │   ├── bulk.cpython-35.pyc
│   │   │   ├── client_options.cpython-35.pyc
│   │   │   ├── collection.cpython-35.pyc
│   │   │   ├── command_cursor.cpython-35.pyc
│   │   │   ├── common.cpython-35.pyc
│   │   │   ├── cursor.cpython-35.pyc
│   │   │   ├── cursor_manager.cpython-35.pyc
│   │   │   ├── database.cpython-35.pyc
│   │   │   ├── errors.cpython-35.pyc
│   │   │   ├── helpers.cpython-35.pyc
│   │   │   ├── __init__.cpython-35.pyc
│   │   │   ├── ismaster.cpython-35.pyc
│   │   │   ├── message.cpython-35.pyc
│   │   │   ├── mongo_client.cpython-35.pyc
│   │   │   ├── mongo_replica_set_client.cpython-35.pyc
│   │   │   ├── monitor.cpython-35.pyc
│   │   │   ├── monitoring.cpython-35.pyc
│   │   │   ├── monotonic.cpython-35.pyc
│   │   │   ├── network.cpython-35.pyc
│   │   │   ├── operations.cpython-35.pyc
│   │   │   ├── periodic_executor.cpython-35.pyc
│   │   │   ├── pool.cpython-35.pyc
│   │   │   ├── read_concern.cpython-35.pyc
│   │   │   ├── read_preferences.cpython-35.pyc
│   │   │   ├── response.cpython-35.pyc
│   │   │   ├── results.cpython-35.pyc
│   │   │   ├── server.cpython-35.pyc
│   │   │   ├── server_description.cpython-35.pyc
│   │   │   ├── server_selectors.cpython-35.pyc
│   │   │   ├── server_type.cpython-35.pyc
│   │   │   ├── settings.cpython-35.pyc
│   │   │   ├── son_manipulator.cpython-35.pyc
│   │   │   ├── ssl_support.cpython-35.pyc
│   │   │   ├── thread_util.cpython-35.pyc
│   │   │   ├── topology.cpython-35.pyc
│   │   │   ├── topology_description.cpython-35.pyc
│   │   │   ├── uri_parser.cpython-35.pyc
│   │   │   └── write_concern.cpython-35.pyc
│   │   ├── read_concern.py
│   │   ├── read_preferences.py
│   │   ├── response.py
│   │   ├── results.py
│   │   ├── server_description.py
│   │   ├── server.py
│   │   ├── server_selectors.py
│   │   ├── server_type.py
│   │   ├── settings.py
│   │   ├── son_manipulator.py
│   │   ├── ssl_context.py
│   │   ├── ssl_match_hostname.py
│   │   ├── ssl_support.py
│   │   ├── thread_util.py
│   │   ├── topology_description.py
│   │   ├── topology.py
│   │   ├── uri_parser.py
│   │   └── write_concern.py
│   ├── pytz
│   │   ├── __init__.py
│   │   ├── locales
│   │   │   └── pytz.pot
│   │   ├── reference.py
│   │   ├── tests
│   │   │   ├── __init__.py
│   │   │   ├── test_docs.py
│   │   │   └── test_tzinfo.py
│   │   ├── tzinfo.py
│   │   ├── zoneinfo
│   │   │   ├── Africa
│   │   │   │   ├── Abidjan.py
│   │   │   │   ├── Accra.py
│   │   │   │   ├── Addis_Ababa.py
│   │   │   │   ├── Algiers.py
│   │   │   │   ├── Asmera.py
│   │   │   │   ├── Bamako.py
│   │   │   │   ├── Bangui.py
│   │   │   │   ├── Banjul.py
│   │   │   │   ├── Bissau.py
│   │   │   │   ├── Blantyre.py
│   │   │   │   ├── Brazzaville.py
│   │   │   │   ├── Bujumbura.py
│   │   │   │   ├── Cairo.py
│   │   │   │   ├── Casablanca.py
│   │   │   │   ├── Ceuta.py
│   │   │   │   ├── Conakry.py
│   │   │   │   ├── Dakar.py
│   │   │   │   ├── Dar_es_Salaam.py
│   │   │   │   ├── Djibouti.py
│   │   │   │   ├── Douala.py
│   │   │   │   ├── El_Aaiun.py
│   │   │   │   ├── Freetown.py
│   │   │   │   ├── Gaborone.py
│   │   │   │   ├── Harare.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── Johannesburg.py
│   │   │   │   ├── Kampala.py
│   │   │   │   ├── Khartoum.py
│   │   │   │   ├── Kigali.py
│   │   │   │   ├── Kinshasa.py
│   │   │   │   ├── Lagos.py
│   │   │   │   ├── Libreville.py
│   │   │   │   ├── Lome.py
│   │   │   │   ├── Luanda.py
│   │   │   │   ├── Lubumbashi.py
│   │   │   │   ├── Lusaka.py
│   │   │   │   ├── Malabo.py
│   │   │   │   ├── Maputo.py
│   │   │   │   ├── Maseru.py
│   │   │   │   ├── Mbabane.py
│   │   │   │   ├── Mogadishu.py
│   │   │   │   ├── Monrovia.py
│   │   │   │   ├── Nairobi.py
│   │   │   │   ├── Ndjamena.py
│   │   │   │   ├── Niamey.py
│   │   │   │   ├── Nouakchott.py
│   │   │   │   ├── Ouagadougou.py
│   │   │   │   ├── Porto_minus_Novo.py
│   │   │   │   ├── Sao_Tome.py
│   │   │   │   ├── Timbuktu.py
│   │   │   │   ├── Tripoli.py
│   │   │   │   ├── Tunis.py
│   │   │   │   └── Windhoek.py
│   │   │   ├── America
│   │   │   │   ├── Adak.py
│   │   │   │   ├── Anchorage.py
│   │   │   │   ├── Anguilla.py
│   │   │   │   ├── Antigua.py
│   │   │   │   ├── Araguaina.py
│   │   │   │   ├── Argentina
│   │   │   │   │   ├── Buenos_Aires.py
│   │   │   │   │   ├── Catamarca.py
│   │   │   │   │   ├── ComodRivadavia.py
│   │   │   │   │   ├── Cordoba.py
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── Jujuy.py
│   │   │   │   │   ├── La_Rioja.py
│   │   │   │   │   ├── Mendoza.py
│   │   │   │   │   ├── Rio_Gallegos.py
│   │   │   │   │   ├── San_Juan.py
│   │   │   │   │   ├── Tucuman.py
│   │   │   │   │   └── Ushuaia.py
│   │   │   │   ├── Aruba.py
│   │   │   │   ├── Asuncion.py
│   │   │   │   ├── Atikokan.py
│   │   │   │   ├── Atka.py
│   │   │   │   ├── Bahia.py
│   │   │   │   ├── Barbados.py
│   │   │   │   ├── Belem.py
│   │   │   │   ├── Belize.py
│   │   │   │   ├── Blanc_minus_Sablon.py
│   │   │   │   ├── Boa_Vista.py
│   │   │   │   ├── Bogota.py
│   │   │   │   ├── Boise.py
│   │   │   │   ├── Buenos_Aires.py
│   │   │   │   ├── Cambridge_Bay.py
│   │   │   │   ├── Campo_Grande.py
│   │   │   │   ├── Cancun.py
│   │   │   │   ├── Caracas.py
│   │   │   │   ├── Catamarca.py
│   │   │   │   ├── Cayenne.py
│   │   │   │   ├── Cayman.py
│   │   │   │   ├── Chicago.py
│   │   │   │   ├── Chihuahua.py
│   │   │   │   ├── Coral_Harbour.py
│   │   │   │   ├── Cordoba.py
│   │   │   │   ├── Costa_Rica.py
│   │   │   │   ├── Cuiaba.py
│   │   │   │   ├── Curacao.py
│   │   │   │   ├── Danmarkshavn.py
│   │   │   │   ├── Dawson_Creek.py
│   │   │   │   ├── Dawson.py
│   │   │   │   ├── Denver.py
│   │   │   │   ├── Detroit.py
│   │   │   │   ├── Dominica.py
│   │   │   │   ├── Edmonton.py
│   │   │   │   ├── Eirunepe.py
│   │   │   │   ├── El_Salvador.py
│   │   │   │   ├── Ensenada.py
│   │   │   │   ├── Fortaleza.py
│   │   │   │   ├── Fort_Wayne.py
│   │   │   │   ├── Glace_Bay.py
│   │   │   │   ├── Godthab.py
│   │   │   │   ├── Goose_Bay.py
│   │   │   │   ├── Grand_Turk.py
│   │   │   │   ├── Grenada.py
│   │   │   │   ├── Guadeloupe.py
│   │   │   │   ├── Guatemala.py
│   │   │   │   ├── Guayaquil.py
│   │   │   │   ├── Guyana.py
│   │   │   │   ├── Halifax.py
│   │   │   │   ├── Havana.py
│   │   │   │   ├── Hermosillo.py
│   │   │   │   ├── Indiana
│   │   │   │   │   ├── Indianapolis.py
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── Knox.py
│   │   │   │   │   ├── Marengo.py
│   │   │   │   │   ├── Petersburg.py
│   │   │   │   │   ├── Vevay.py
│   │   │   │   │   └── Vincennes.py
│   │   │   │   ├── Indianapolis.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── Inuvik.py
│   │   │   │   ├── Iqaluit.py
│   │   │   │   ├── Jamaica.py
│   │   │   │   ├── Jujuy.py
│   │   │   │   ├── Juneau.py
│   │   │   │   ├── Kentucky
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── Louisville.py
│   │   │   │   │   └── Monticello.py
│   │   │   │   ├── Knox_IN.py
│   │   │   │   ├── La_Paz.py
│   │   │   │   ├── Lima.py
│   │   │   │   ├── Los_Angeles.py
│   │   │   │   ├── Louisville.py
│   │   │   │   ├── Maceio.py
│   │   │   │   ├── Managua.py
│   │   │   │   ├── Manaus.py
│   │   │   │   ├── Martinique.py
│   │   │   │   ├── Mazatlan.py
│   │   │   │   ├── Mendoza.py
│   │   │   │   ├── Menominee.py
│   │   │   │   ├── Merida.py
│   │   │   │   ├── Mexico_City.py
│   │   │   │   ├── Miquelon.py
│   │   │   │   ├── Moncton.py
│   │   │   │   ├── Monterrey.py
│   │   │   │   ├── Montevideo.py
│   │   │   │   ├── Montreal.py
│   │   │   │   ├── Montserrat.py
│   │   │   │   ├── Nassau.py
│   │   │   │   ├── New_York.py
│   │   │   │   ├── Nipigon.py
│   │   │   │   ├── Nome.py
│   │   │   │   ├── Noronha.py
│   │   │   │   ├── North_Dakota
│   │   │   │   │   ├── Center.py
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   └── New_Salem.py
│   │   │   │   ├── Panama.py
│   │   │   │   ├── Pangnirtung.py
│   │   │   │   ├── Paramaribo.py
│   │   │   │   ├── Phoenix.py
│   │   │   │   ├── Port_minus_au_minus_Prince.py
│   │   │   │   ├── Porto_Acre.py
│   │   │   │   ├── Port_of_Spain.py
│   │   │   │   ├── Porto_Velho.py
│   │   │   │   ├── Puerto_Rico.py
│   │   │   │   ├── Rainy_River.py
│   │   │   │   ├── Rankin_Inlet.py
│   │   │   │   ├── Recife.py
│   │   │   │   ├── Regina.py
│   │   │   │   ├── Rio_Branco.py
│   │   │   │   ├── Rosario.py
│   │   │   │   ├── Santiago.py
│   │   │   │   ├── Santo_Domingo.py
│   │   │   │   ├── Sao_Paulo.py
│   │   │   │   ├── Scoresbysund.py
│   │   │   │   ├── Shiprock.py
│   │   │   │   ├── St_Johns.py
│   │   │   │   ├── St_Kitts.py
│   │   │   │   ├── St_Lucia.py
│   │   │   │   ├── St_Thomas.py
│   │   │   │   ├── St_Vincent.py
│   │   │   │   ├── Swift_Current.py
│   │   │   │   ├── Tegucigalpa.py
│   │   │   │   ├── Thule.py
│   │   │   │   ├── Thunder_Bay.py
│   │   │   │   ├── Tijuana.py
│   │   │   │   ├── Toronto.py
│   │   │   │   ├── Tortola.py
│   │   │   │   ├── Vancouver.py
│   │   │   │   ├── Virgin.py
│   │   │   │   ├── Whitehorse.py
│   │   │   │   ├── Winnipeg.py
│   │   │   │   ├── Yakutat.py
│   │   │   │   └── Yellowknife.py
│   │   │   ├── Antarctica
│   │   │   │   ├── Casey.py
│   │   │   │   ├── Davis.py
│   │   │   │   ├── DumontDUrville.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── Mawson.py
│   │   │   │   ├── McMurdo.py
│   │   │   │   ├── Palmer.py
│   │   │   │   ├── Rothera.py
│   │   │   │   ├── South_Pole.py
│   │   │   │   ├── Syowa.py
│   │   │   │   └── Vostok.py
│   │   │   ├── Arctic
│   │   │   │   ├── __init__.py
│   │   │   │   └── Longyearbyen.py
│   │   │   ├── Asia
│   │   │   │   ├── Aden.py
│   │   │   │   ├── Almaty.py
│   │   │   │   ├── Amman.py
│   │   │   │   ├── Anadyr.py
│   │   │   │   ├── Aqtau.py
│   │   │   │   ├── Aqtobe.py
│   │   │   │   ├── Ashgabat.py
│   │   │   │   ├── Ashkhabad.py
│   │   │   │   ├── Baghdad.py
│   │   │   │   ├── Bahrain.py
│   │   │   │   ├── Baku.py
│   │   │   │   ├── Bangkok.py
│   │   │   │   ├── Beirut.py
│   │   │   │   ├── Bishkek.py
│   │   │   │   ├── Brunei.py
│   │   │   │   ├── Calcutta.py
│   │   │   │   ├── Choibalsan.py
│   │   │   │   ├── Chongqing.py
│   │   │   │   ├── Chungking.py
│   │   │   │   ├── Colombo.py
│   │   │   │   ├── Dacca.py
│   │   │   │   ├── Damascus.py
│   │   │   │   ├── Dhaka.py
│   │   │   │   ├── Dili.py
│   │   │   │   ├── Dubai.py
│   │   │   │   ├── Dushanbe.py
│   │   │   │   ├── Gaza.py
│   │   │   │   ├── Harbin.py
│   │   │   │   ├── Hong_Kong.py
│   │   │   │   ├── Hovd.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── Irkutsk.py
│   │   │   │   ├── Istanbul.py
│   │   │   │   ├── Jakarta.py
│   │   │   │   ├── Jayapura.py
│   │   │   │   ├── Jerusalem.py
│   │   │   │   ├── Kabul.py
│   │   │   │   ├── Kamchatka.py
│   │   │   │   ├── Karachi.py
│   │   │   │   ├── Kashgar.py
│   │   │   │   ├── Katmandu.py
│   │   │   │   ├── Krasnoyarsk.py
│   │   │   │   ├── Kuala_Lumpur.py
│   │   │   │   ├── Kuching.py
│   │   │   │   ├── Kuwait.py
│   │   │   │   ├── Macao.py
│   │   │   │   ├── Macau.py
│   │   │   │   ├── Magadan.py
│   │   │   │   ├── Makassar.py
│   │   │   │   ├── Manila.py
│   │   │   │   ├── Muscat.py
│   │   │   │   ├── Nicosia.py
│   │   │   │   ├── Novosibirsk.py
│   │   │   │   ├── Omsk.py
│   │   │   │   ├── Oral.py
│   │   │   │   ├── Phnom_Penh.py
│   │   │   │   ├── Pontianak.py
│   │   │   │   ├── Pyongyang.py
│   │   │   │   ├── Qatar.py
│   │   │   │   ├── Qyzylorda.py
│   │   │   │   ├── Rangoon.py
│   │   │   │   ├── Riyadh.py
│   │   │   │   ├── Saigon.py
│   │   │   │   ├── Sakhalin.py
│   │   │   │   ├── Samarkand.py
│   │   │   │   ├── Seoul.py
│   │   │   │   ├── Shanghai.py
│   │   │   │   ├── Singapore.py
│   │   │   │   ├── Taipei.py
│   │   │   │   ├── Tashkent.py
│   │   │   │   ├── Tbilisi.py
│   │   │   │   ├── Tehran.py
│   │   │   │   ├── Tel_Aviv.py
│   │   │   │   ├── Thimbu.py
│   │   │   │   ├── Thimphu.py
│   │   │   │   ├── Tokyo.py
│   │   │   │   ├── Ujung_Pandang.py
│   │   │   │   ├── Ulaanbaatar.py
│   │   │   │   ├── Ulan_Bator.py
│   │   │   │   ├── Urumqi.py
│   │   │   │   ├── Vientiane.py
│   │   │   │   ├── Vladivostok.py
│   │   │   │   ├── Yakutsk.py
│   │   │   │   ├── Yekaterinburg.py
│   │   │   │   └── Yerevan.py
│   │   │   ├── Atlantic
│   │   │   │   ├── Azores.py
│   │   │   │   ├── Bermuda.py
│   │   │   │   ├── Canary.py
│   │   │   │   ├── Cape_Verde.py
│   │   │   │   ├── Faeroe.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── Jan_Mayen.py
│   │   │   │   ├── Madeira.py
│   │   │   │   ├── Reykjavik.py
│   │   │   │   ├── South_Georgia.py
│   │   │   │   ├── Stanley.py
│   │   │   │   └── St_Helena.py
│   │   │   ├── Australia
│   │   │   │   ├── ACT.py
│   │   │   │   ├── Adelaide.py
│   │   │   │   ├── Brisbane.py
│   │   │   │   ├── Broken_Hill.py
│   │   │   │   ├── Canberra.py
│   │   │   │   ├── Currie.py
│   │   │   │   ├── Darwin.py
│   │   │   │   ├── Hobart.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── LHI.py
│   │   │   │   ├── Lindeman.py
│   │   │   │   ├── Lord_Howe.py
│   │   │   │   ├── Melbourne.py
│   │   │   │   ├── North.py
│   │   │   │   ├── NSW.py
│   │   │   │   ├── Perth.py
│   │   │   │   ├── Queensland.py
│   │   │   │   ├── South.py
│   │   │   │   ├── Sydney.py
│   │   │   │   ├── Tasmania.py
│   │   │   │   ├── Victoria.py
│   │   │   │   ├── West.py
│   │   │   │   └── Yancowinna.py
│   │   │   ├── Brazil
│   │   │   │   ├── Acre.py
│   │   │   │   ├── DeNoronha.py
│   │   │   │   ├── East.py
│   │   │   │   ├── __init__.py
│   │   │   │   └── West.py
│   │   │   ├── Canada
│   │   │   │   ├── Atlantic.py
│   │   │   │   ├── Central.py
│   │   │   │   ├── Eastern.py
│   │   │   │   ├── East_minus_Saskatchewan.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── Mountain.py
│   │   │   │   ├── Newfoundland.py
│   │   │   │   ├── Pacific.py
│   │   │   │   ├── Saskatchewan.py
│   │   │   │   └── Yukon.py
│   │   │   ├── CET.py
│   │   │   ├── Chile
│   │   │   │   ├── Continental.py
│   │   │   │   ├── EasterIsland.py
│   │   │   │   └── __init__.py
│   │   │   ├── CST6CDT.py
│   │   │   ├── Cuba.py
│   │   │   ├── EET.py
│   │   │   ├── Egypt.py
│   │   │   ├── Eire.py
│   │   │   ├── EST5EDT.py
│   │   │   ├── EST.py
│   │   │   ├── Etc
│   │   │   │   ├── GMT0.py
│   │   │   │   ├── GMT_minus_0.py
│   │   │   │   ├── GMT_minus_10.py
│   │   │   │   ├── GMT_minus_11.py
│   │   │   │   ├── GMT_minus_12.py
│   │   │   │   ├── GMT_minus_13.py
│   │   │   │   ├── GMT_minus_14.py
│   │   │   │   ├── GMT_minus_1.py
│   │   │   │   ├── GMT_minus_2.py
│   │   │   │   ├── GMT_minus_3.py
│   │   │   │   ├── GMT_minus_4.py
│   │   │   │   ├── GMT_minus_5.py
│   │   │   │   ├── GMT_minus_6.py
│   │   │   │   ├── GMT_minus_7.py
│   │   │   │   ├── GMT_minus_8.py
│   │   │   │   ├── GMT_minus_9.py
│   │   │   │   ├── GMT_plus_0.py
│   │   │   │   ├── GMT_plus_10.py
│   │   │   │   ├── GMT_plus_11.py
│   │   │   │   ├── GMT_plus_12.py
│   │   │   │   ├── GMT_plus_1.py
│   │   │   │   ├── GMT_plus_2.py
│   │   │   │   ├── GMT_plus_3.py
│   │   │   │   ├── GMT_plus_4.py
│   │   │   │   ├── GMT_plus_5.py
│   │   │   │   ├── GMT_plus_6.py
│   │   │   │   ├── GMT_plus_7.py
│   │   │   │   ├── GMT_plus_8.py
│   │   │   │   ├── GMT_plus_9.py
│   │   │   │   ├── GMT.py
│   │   │   │   ├── Greenwich.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── UCT.py
│   │   │   │   ├── Universal.py
│   │   │   │   ├── UTC.py
│   │   │   │   └── Zulu.py
│   │   │   ├── Europe
│   │   │   │   ├── Amsterdam.py
│   │   │   │   ├── Andorra.py
│   │   │   │   ├── Athens.py
│   │   │   │   ├── Belfast.py
│   │   │   │   ├── Belgrade.py
│   │   │   │   ├── Berlin.py
│   │   │   │   ├── Bratislava.py
│   │   │   │   ├── Brussels.py
│   │   │   │   ├── Bucharest.py
│   │   │   │   ├── Budapest.py
│   │   │   │   ├── Chisinau.py
│   │   │   │   ├── Copenhagen.py
│   │   │   │   ├── Dublin.py
│   │   │   │   ├── Gibraltar.py
│   │   │   │   ├── Guernsey.py
│   │   │   │   ├── Helsinki.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── Isle_of_Man.py
│   │   │   │   ├── Istanbul.py
│   │   │   │   ├── Jersey.py
│   │   │   │   ├── Kaliningrad.py
│   │   │   │   ├── Kiev.py
│   │   │   │   ├── Lisbon.py
│   │   │   │   ├── Ljubljana.py
│   │   │   │   ├── London.py
│   │   │   │   ├── Luxembourg.py
│   │   │   │   ├── Madrid.py
│   │   │   │   ├── Malta.py
│   │   │   │   ├── Mariehamn.py
│   │   │   │   ├── Minsk.py
│   │   │   │   ├── Monaco.py
│   │   │   │   ├── Moscow.py
│   │   │   │   ├── Nicosia.py
│   │   │   │   ├── Oslo.py
│   │   │   │   ├── Paris.py
│   │   │   │   ├── Podgorica.py
│   │   │   │   ├── Prague.py
│   │   │   │   ├── Riga.py
│   │   │   │   ├── Rome.py
│   │   │   │   ├── Samara.py
│   │   │   │   ├── San_Marino.py
│   │   │   │   ├── Sarajevo.py
│   │   │   │   ├── Simferopol.py
│   │   │   │   ├── Skopje.py
│   │   │   │   ├── Sofia.py
│   │   │   │   ├── Stockholm.py
│   │   │   │   ├── Tallinn.py
│   │   │   │   ├── Tirane.py
│   │   │   │   ├── Tiraspol.py
│   │   │   │   ├── Uzhgorod.py
│   │   │   │   ├── Vaduz.py
│   │   │   │   ├── Vatican.py
│   │   │   │   ├── Vienna.py
│   │   │   │   ├── Vilnius.py
│   │   │   │   ├── Volgograd.py
│   │   │   │   ├── Warsaw.py
│   │   │   │   ├── Zagreb.py
│   │   │   │   ├── Zaporozhye.py
│   │   │   │   └── Zurich.py
│   │   │   ├── GB_minus_Eire.py
│   │   │   ├── GB.py
│   │   │   ├── GMT0.py
│   │   │   ├── GMT_minus_0.py
│   │   │   ├── GMT_plus_0.py
│   │   │   ├── GMT.py
│   │   │   ├── Greenwich.py
│   │   │   ├── Hongkong.py
│   │   │   ├── HST.py
│   │   │   ├── Iceland.py
│   │   │   ├── Indian
│   │   │   │   ├── Antananarivo.py
│   │   │   │   ├── Chagos.py
│   │   │   │   ├── Christmas.py
│   │   │   │   ├── Cocos.py
│   │   │   │   ├── Comoro.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── Kerguelen.py
│   │   │   │   ├── Mahe.py
│   │   │   │   ├── Maldives.py
│   │   │   │   ├── Mauritius.py
│   │   │   │   ├── Mayotte.py
│   │   │   │   └── Reunion.py
│   │   │   ├── __init__.py
│   │   │   ├── Iran.py
│   │   │   ├── Israel.py
│   │   │   ├── Jamaica.py
│   │   │   ├── Japan.py
│   │   │   ├── Kwajalein.py
│   │   │   ├── Libya.py
│   │   │   ├── MET.py
│   │   │   ├── Mexico
│   │   │   │   ├── BajaNorte.py
│   │   │   │   ├── BajaSur.py
│   │   │   │   ├── General.py
│   │   │   │   └── __init__.py
│   │   │   ├── MST7MDT.py
│   │   │   ├── MST.py
│   │   │   ├── Navajo.py
│   │   │   ├── NZ_minus_CHAT.py
│   │   │   ├── NZ.py
│   │   │   ├── Pacific
│   │   │   │   ├── Apia.py
│   │   │   │   ├── Auckland.py
│   │   │   │   ├── Chatham.py
│   │   │   │   ├── Easter.py
│   │   │   │   ├── Efate.py
│   │   │   │   ├── Enderbury.py
│   │   │   │   ├── Fakaofo.py
│   │   │   │   ├── Fiji.py
│   │   │   │   ├── Funafuti.py
│   │   │   │   ├── Galapagos.py
│   │   │   │   ├── Gambier.py
│   │   │   │   ├── Guadalcanal.py
│   │   │   │   ├── Guam.py
│   │   │   │   ├── Honolulu.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── Johnston.py
│   │   │   │   ├── Kiritimati.py
│   │   │   │   ├── Kosrae.py
│   │   │   │   ├── Kwajalein.py
│   │   │   │   ├── Majuro.py
│   │   │   │   ├── Marquesas.py
│   │   │   │   ├── Midway.py
│   │   │   │   ├── Nauru.py
│   │   │   │   ├── Niue.py
│   │   │   │   ├── Norfolk.py
│   │   │   │   ├── Noumea.py
│   │   │   │   ├── Pago_Pago.py
│   │   │   │   ├── Palau.py
│   │   │   │   ├── Pitcairn.py
│   │   │   │   ├── Ponape.py
│   │   │   │   ├── Port_Moresby.py
│   │   │   │   ├── Rarotonga.py
│   │   │   │   ├── Saipan.py
│   │   │   │   ├── Samoa.py
│   │   │   │   ├── Tahiti.py
│   │   │   │   ├── Tarawa.py
│   │   │   │   ├── Tongatapu.py
│   │   │   │   ├── Truk.py
│   │   │   │   ├── Wake.py
│   │   │   │   ├── Wallis.py
│   │   │   │   └── Yap.py
│   │   │   ├── Poland.py
│   │   │   ├── Portugal.py
│   │   │   ├── posixrules.py
│   │   │   ├── PRC.py
│   │   │   ├── PST8PDT.py
│   │   │   ├── ROC.py
│   │   │   ├── ROK.py
│   │   │   ├── Singapore.py
│   │   │   ├── Turkey.py
│   │   │   ├── UCT.py
│   │   │   ├── Universal.py
│   │   │   ├── US
│   │   │   │   ├── Alaska.py
│   │   │   │   ├── Aleutian.py
│   │   │   │   ├── Arizona.py
│   │   │   │   ├── Central.py
│   │   │   │   ├── Eastern.py
│   │   │   │   ├── East_minus_Indiana.py
│   │   │   │   ├── Hawaii.py
│   │   │   │   ├── Indiana_minus_Starke.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── Michigan.py
│   │   │   │   ├── Mountain.py
│   │   │   │   ├── Pacific_minus_New.py
│   │   │   │   ├── Pacific.py
│   │   │   │   └── Samoa.py
│   │   │   ├── UTC.py
│   │   │   ├── WET.py
│   │   │   ├── W_minus_SU.py
│   │   │   └── Zulu.py
│   │   └── zone.tab
│   ├── simplejson
│   │   ├── compat.py
│   │   ├── decoder.py
│   │   ├── encoder.py
│   │   ├── __init__.py
│   │   ├── ordered_dict.py
│   │   ├── __pycache__
│   │   │   ├── compat.cpython-35.pyc
│   │   │   ├── decoder.cpython-35.pyc
│   │   │   ├── encoder.cpython-35.pyc
│   │   │   ├── __init__.cpython-35.pyc
│   │   │   └── scanner.cpython-35.pyc
│   │   ├── scanner.py
│   │   ├── _speedups.c
│   │   ├── tests
│   │   │   ├── __init__.py
│   │   │   ├── test_bigint_as_string.py
│   │   │   ├── test_bitsize_int_as_string.py
│   │   │   ├── test_check_circular.py
│   │   │   ├── test_decimal.py
│   │   │   ├── test_decode.py
│   │   │   ├── test_default.py
│   │   │   ├── test_dump.py
│   │   │   ├── test_encode_basestring_ascii.py
│   │   │   ├── test_encode_for_html.py
│   │   │   ├── test_errors.py
│   │   │   ├── test_fail.py
│   │   │   ├── test_float.py
│   │   │   ├── test_for_json.py
│   │   │   ├── test_indent.py
│   │   │   ├── test_item_sort_key.py
│   │   │   ├── test_iterable.py
│   │   │   ├── test_namedtuple.py
│   │   │   ├── test_pass1.py
│   │   │   ├── test_pass2.py
│   │   │   ├── test_pass3.py
│   │   │   ├── test_recursion.py
│   │   │   ├── test_scanstring.py
│   │   │   ├── test_separators.py
│   │   │   ├── test_speedups.py
│   │   │   ├── test_subclass.py
│   │   │   ├── test_tool.py
│   │   │   ├── test_tuple.py
│   │   │   └── test_unicode.py
│   │   └── tool.py
│   ├── six.py
│   ├── sqlalchemy
│   │   ├── cextension
│   │   │   ├── processors.c
│   │   │   ├── resultproxy.c
│   │   │   └── utils.c
│   │   ├── connectors
│   │   │   ├── __init__.py
│   │   │   ├── mxodbc.py
│   │   │   ├── __pycache__
│   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   └── zxJDBC.cpython-35.pyc
│   │   │   ├── pyodbc.py
│   │   │   └── zxJDBC.py
│   │   ├── databases
│   │   │   └── __init__.py
│   │   ├── dialects
│   │   │   ├── firebird
│   │   │   │   ├── base.py
│   │   │   │   ├── fdb.py
│   │   │   │   ├── __init__.py
│   │   │   │   └── kinterbasdb.py
│   │   │   ├── __init__.py
│   │   │   ├── mssql
│   │   │   │   ├── adodbapi.py
│   │   │   │   ├── base.py
│   │   │   │   ├── information_schema.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── mxodbc.py
│   │   │   │   ├── pymssql.py
│   │   │   │   ├── pyodbc.py
│   │   │   │   └── zxjdbc.py
│   │   │   ├── mysql
│   │   │   │   ├── base.py
│   │   │   │   ├── cymysql.py
│   │   │   │   ├── gaerdbms.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── mysqlconnector.py
│   │   │   │   ├── mysqldb.py
│   │   │   │   ├── oursql.py
│   │   │   │   ├── pymysql.py
│   │   │   │   ├── pyodbc.py
│   │   │   │   └── zxjdbc.py
│   │   │   ├── oracle
│   │   │   │   ├── base.py
│   │   │   │   ├── cx_oracle.py
│   │   │   │   ├── __init__.py
│   │   │   │   └── zxjdbc.py
│   │   │   ├── postgres.py
│   │   │   ├── postgresql
│   │   │   │   ├── base.py
│   │   │   │   ├── constraints.py
│   │   │   │   ├── hstore.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── json.py
│   │   │   │   ├── pg8000.py
│   │   │   │   ├── psycopg2cffi.py
│   │   │   │   ├── psycopg2.py
│   │   │   │   ├── __pycache__
│   │   │   │   │   ├── base.cpython-35.pyc
│   │   │   │   │   ├── constraints.cpython-35.pyc
│   │   │   │   │   ├── hstore.cpython-35.pyc
│   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   ├── json.cpython-35.pyc
│   │   │   │   │   ├── pg8000.cpython-35.pyc
│   │   │   │   │   ├── psycopg2cffi.cpython-35.pyc
│   │   │   │   │   ├── psycopg2.cpython-35.pyc
│   │   │   │   │   ├── pypostgresql.cpython-35.pyc
│   │   │   │   │   ├── ranges.cpython-35.pyc
│   │   │   │   │   └── zxjdbc.cpython-35.pyc
│   │   │   │   ├── pypostgresql.py
│   │   │   │   ├── ranges.py
│   │   │   │   └── zxjdbc.py
│   │   │   ├── __pycache__
│   │   │   │   └── __init__.cpython-35.pyc
│   │   │   ├── sqlite
│   │   │   │   ├── base.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── __pycache__
│   │   │   │   │   ├── base.cpython-35.pyc
│   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   ├── pysqlcipher.cpython-35.pyc
│   │   │   │   │   └── pysqlite.cpython-35.pyc
│   │   │   │   ├── pysqlcipher.py
│   │   │   │   └── pysqlite.py
│   │   │   ├── sybase
│   │   │   │   ├── base.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── mxodbc.py
│   │   │   │   ├── pyodbc.py
│   │   │   │   └── pysybase.py
│   │   │   └── type_migration_guidelines.txt
│   │   ├── engine
│   │   │   ├── base.py
│   │   │   ├── default.py
│   │   │   ├── __init__.py
│   │   │   ├── interfaces.py
│   │   │   ├── __pycache__
│   │   │   │   ├── base.cpython-35.pyc
│   │   │   │   ├── default.cpython-35.pyc
│   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   ├── interfaces.cpython-35.pyc
│   │   │   │   ├── reflection.cpython-35.pyc
│   │   │   │   ├── result.cpython-35.pyc
│   │   │   │   ├── strategies.cpython-35.pyc
│   │   │   │   ├── threadlocal.cpython-35.pyc
│   │   │   │   ├── url.cpython-35.pyc
│   │   │   │   └── util.cpython-35.pyc
│   │   │   ├── reflection.py
│   │   │   ├── result.py
│   │   │   ├── strategies.py
│   │   │   ├── threadlocal.py
│   │   │   ├── url.py
│   │   │   └── util.py
│   │   ├── event
│   │   │   ├── api.py
│   │   │   ├── attr.py
│   │   │   ├── base.py
│   │   │   ├── __init__.py
│   │   │   ├── legacy.py
│   │   │   ├── __pycache__
│   │   │   │   ├── api.cpython-35.pyc
│   │   │   │   ├── attr.cpython-35.pyc
│   │   │   │   ├── base.cpython-35.pyc
│   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   ├── legacy.cpython-35.pyc
│   │   │   │   └── registry.cpython-35.pyc
│   │   │   └── registry.py
│   │   ├── events.py
│   │   ├── exc.py
│   │   ├── ext
│   │   │   ├── associationproxy.py
│   │   │   ├── automap.py
│   │   │   ├── baked.py
│   │   │   ├── compiler.py
│   │   │   ├── declarative
│   │   │   │   ├── api.py
│   │   │   │   ├── base.py
│   │   │   │   ├── clsregistry.py
│   │   │   │   ├── __init__.py
│   │   │   │   └── __pycache__
│   │   │   │       ├── api.cpython-35.pyc
│   │   │   │       ├── base.cpython-35.pyc
│   │   │   │       ├── clsregistry.cpython-35.pyc
│   │   │   │       └── __init__.cpython-35.pyc
│   │   │   ├── horizontal_shard.py
│   │   │   ├── hybrid.py
│   │   │   ├── __init__.py
│   │   │   ├── instrumentation.py
│   │   │   ├── mutable.py
│   │   │   ├── orderinglist.py
│   │   │   ├── __pycache__
│   │   │   │   ├── associationproxy.cpython-35.pyc
│   │   │   │   ├── hybrid.cpython-35.pyc
│   │   │   │   └── __init__.cpython-35.pyc
│   │   │   └── serializer.py
│   │   ├── __init__.py
│   │   ├── inspection.py
│   │   ├── interfaces.py
│   │   ├── log.py
│   │   ├── orm
│   │   │   ├── attributes.py
│   │   │   ├── base.py
│   │   │   ├── collections.py
│   │   │   ├── dependency.py
│   │   │   ├── deprecated_interfaces.py
│   │   │   ├── descriptor_props.py
│   │   │   ├── dynamic.py
│   │   │   ├── evaluator.py
│   │   │   ├── events.py
│   │   │   ├── exc.py
│   │   │   ├── identity.py
│   │   │   ├── __init__.py
│   │   │   ├── instrumentation.py
│   │   │   ├── interfaces.py
│   │   │   ├── loading.py
│   │   │   ├── mapper.py
│   │   │   ├── path_registry.py
│   │   │   ├── persistence.py
│   │   │   ├── properties.py
│   │   │   ├── __pycache__
│   │   │   │   ├── attributes.cpython-35.pyc
│   │   │   │   ├── base.cpython-35.pyc
│   │   │   │   ├── collections.cpython-35.pyc
│   │   │   │   ├── dependency.cpython-35.pyc
│   │   │   │   ├── deprecated_interfaces.cpython-35.pyc
│   │   │   │   ├── descriptor_props.cpython-35.pyc
│   │   │   │   ├── dynamic.cpython-35.pyc
│   │   │   │   ├── evaluator.cpython-35.pyc
│   │   │   │   ├── events.cpython-35.pyc
│   │   │   │   ├── exc.cpython-35.pyc
│   │   │   │   ├── identity.cpython-35.pyc
│   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   ├── instrumentation.cpython-35.pyc
│   │   │   │   ├── interfaces.cpython-35.pyc
│   │   │   │   ├── loading.cpython-35.pyc
│   │   │   │   ├── mapper.cpython-35.pyc
│   │   │   │   ├── path_registry.cpython-35.pyc
│   │   │   │   ├── persistence.cpython-35.pyc
│   │   │   │   ├── properties.cpython-35.pyc
│   │   │   │   ├── query.cpython-35.pyc
│   │   │   │   ├── relationships.cpython-35.pyc
│   │   │   │   ├── scoping.cpython-35.pyc
│   │   │   │   ├── session.cpython-35.pyc
│   │   │   │   ├── state.cpython-35.pyc
│   │   │   │   ├── strategies.cpython-35.pyc
│   │   │   │   ├── strategy_options.cpython-35.pyc
│   │   │   │   ├── sync.cpython-35.pyc
│   │   │   │   ├── unitofwork.cpython-35.pyc
│   │   │   │   └── util.cpython-35.pyc
│   │   │   ├── query.py
│   │   │   ├── relationships.py
│   │   │   ├── scoping.py
│   │   │   ├── session.py
│   │   │   ├── state.py
│   │   │   ├── strategies.py
│   │   │   ├── strategy_options.py
│   │   │   ├── sync.py
│   │   │   ├── unitofwork.py
│   │   │   └── util.py
│   │   ├── pool.py
│   │   ├── processors.py
│   │   ├── __pycache__
│   │   │   ├── events.cpython-35.pyc
│   │   │   ├── exc.cpython-35.pyc
│   │   │   ├── __init__.cpython-35.pyc
│   │   │   ├── inspection.cpython-35.pyc
│   │   │   ├── interfaces.cpython-35.pyc
│   │   │   ├── log.cpython-35.pyc
│   │   │   ├── pool.cpython-35.pyc
│   │   │   ├── processors.cpython-35.pyc
│   │   │   ├── schema.cpython-35.pyc
│   │   │   └── types.cpython-35.pyc
│   │   ├── schema.py
│   │   ├── sql
│   │   │   ├── annotation.py
│   │   │   ├── base.py
│   │   │   ├── compiler.py
│   │   │   ├── crud.py
│   │   │   ├── ddl.py
│   │   │   ├── default_comparator.py
│   │   │   ├── dml.py
│   │   │   ├── elements.py
│   │   │   ├── expression.py
│   │   │   ├── functions.py
│   │   │   ├── __init__.py
│   │   │   ├── naming.py
│   │   │   ├── operators.py
│   │   │   ├── __pycache__
│   │   │   │   ├── annotation.cpython-35.pyc
│   │   │   │   ├── base.cpython-35.pyc
│   │   │   │   ├── compiler.cpython-35.pyc
│   │   │   │   ├── crud.cpython-35.pyc
│   │   │   │   ├── ddl.cpython-35.pyc
│   │   │   │   ├── default_comparator.cpython-35.pyc
│   │   │   │   ├── dml.cpython-35.pyc
│   │   │   │   ├── elements.cpython-35.pyc
│   │   │   │   ├── expression.cpython-35.pyc
│   │   │   │   ├── functions.cpython-35.pyc
│   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   ├── naming.cpython-35.pyc
│   │   │   │   ├── operators.cpython-35.pyc
│   │   │   │   ├── schema.cpython-35.pyc
│   │   │   │   ├── selectable.cpython-35.pyc
│   │   │   │   ├── sqltypes.cpython-35.pyc
│   │   │   │   ├── type_api.cpython-35.pyc
│   │   │   │   ├── util.cpython-35.pyc
│   │   │   │   └── visitors.cpython-35.pyc
│   │   │   ├── schema.py
│   │   │   ├── selectable.py
│   │   │   ├── sqltypes.py
│   │   │   ├── type_api.py
│   │   │   ├── util.py
│   │   │   └── visitors.py
│   │   ├── testing
│   │   │   ├── assertions.py
│   │   │   ├── assertsql.py
│   │   │   ├── config.py
│   │   │   ├── distutils_run.py
│   │   │   ├── engines.py
│   │   │   ├── entities.py
│   │   │   ├── exclusions.py
│   │   │   ├── fixtures.py
│   │   │   ├── __init__.py
│   │   │   ├── mock.py
│   │   │   ├── pickleable.py
│   │   │   ├── plugin
│   │   │   │   ├── bootstrap.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── noseplugin.py
│   │   │   │   ├── plugin_base.py
│   │   │   │   └── pytestplugin.py
│   │   │   ├── profiling.py
│   │   │   ├── provision.py
│   │   │   ├── replay_fixture.py
│   │   │   ├── requirements.py
│   │   │   ├── runner.py
│   │   │   ├── schema.py
│   │   │   ├── suite
│   │   │   │   ├── __init__.py
│   │   │   │   ├── test_ddl.py
│   │   │   │   ├── test_dialect.py
│   │   │   │   ├── test_insert.py
│   │   │   │   ├── test_reflection.py
│   │   │   │   ├── test_results.py
│   │   │   │   ├── test_select.py
│   │   │   │   ├── test_sequence.py
│   │   │   │   ├── test_types.py
│   │   │   │   └── test_update_delete.py
│   │   │   ├── util.py
│   │   │   └── warnings.py
│   │   ├── types.py
│   │   └── util
│   │       ├── _collections.py
│   │       ├── compat.py
│   │       ├── deprecations.py
│   │       ├── __init__.py
│   │       ├── langhelpers.py
│   │       ├── __pycache__
│   │       │   ├── _collections.cpython-35.pyc
│   │       │   ├── compat.cpython-35.pyc
│   │       │   ├── deprecations.cpython-35.pyc
│   │       │   ├── __init__.cpython-35.pyc
│   │       │   ├── langhelpers.cpython-35.pyc
│   │       │   ├── queue.cpython-35.pyc
│   │       │   └── topological.cpython-35.pyc
│   │       ├── queue.py
│   │       └── topological.py
│   ├── toml.py
│   └── werkzeug
│       ├── _compat.py
│       ├── contrib
│       │   ├── atom.py
│       │   ├── cache.py
│       │   ├── fixers.py
│       │   ├── __init__.py
│       │   ├── iterio.py
│       │   ├── jsrouting.py
│       │   ├── limiter.py
│       │   ├── lint.py
│       │   ├── profiler.py
│       │   ├── securecookie.py
│       │   ├── sessions.py
│       │   ├── testtools.py
│       │   └── wrappers.py
│       ├── datastructures.py
│       ├── debug
│       │   ├── console.py
│       │   ├── __init__.py
│       │   ├── __pycache__
│       │   │   ├── console.cpython-35.pyc
│       │   │   ├── __init__.cpython-35.pyc
│       │   │   ├── repr.cpython-35.pyc
│       │   │   └── tbtools.cpython-35.pyc
│       │   ├── repr.py
│       │   ├── shared
│       │   │   ├── console.png
│       │   │   ├── debugger.js
│       │   │   ├── FONT_LICENSE
│       │   │   ├── jquery.js
│       │   │   ├── less.png
│       │   │   ├── more.png
│       │   │   ├── source.png
│       │   │   ├── style.css
│       │   │   └── ubuntu.ttf
│       │   └── tbtools.py
│       ├── exceptions.py
│       ├── formparser.py
│       ├── http.py
│       ├── __init__.py
│       ├── _internal.py
│       ├── local.py
│       ├── posixemulation.py
│       ├── __pycache__
│       │   ├── _compat.cpython-35.pyc
│       │   ├── datastructures.cpython-35.pyc
│       │   ├── exceptions.cpython-35.pyc
│       │   ├── filesystem.cpython-35.pyc
│       │   ├── formparser.cpython-35.pyc
│       │   ├── http.cpython-35.pyc
│       │   ├── __init__.cpython-35.pyc
│       │   ├── _internal.cpython-35.pyc
│       │   ├── local.cpython-35.pyc
│       │   ├── _reloader.cpython-35.pyc
│       │   ├── routing.cpython-35.pyc
│       │   ├── security.cpython-35.pyc
│       │   ├── serving.cpython-35.pyc
│       │   ├── urls.cpython-35.pyc
│       │   ├── utils.cpython-35.pyc
│       │   ├── wrappers.cpython-35.pyc
│       │   └── wsgi.cpython-35.pyc
│       ├── routing.py
│       ├── script.py
│       ├── security.py
│       ├── serving.py
│       ├── testapp.py
│       ├── test.py
│       ├── testsuite
│       │   ├── compat.py
│       │   ├── contrib
│       │   │   ├── cache.py
│       │   │   ├── fixers.py
│       │   │   ├── __init__.py
│       │   │   ├── iterio.py
│       │   │   ├── securecookie.py
│       │   │   ├── sessions.py
│       │   │   └── wrappers.py
│       │   ├── datastructures.py
│       │   ├── debug.py
│       │   ├── exceptions.py
│       │   ├── formparser.py
│       │   ├── http.py
│       │   ├── __init__.py
│       │   ├── internal.py
│       │   ├── local.py
│       │   ├── multipart
│       │   │   ├── collect.py
│       │   │   ├── firefox3-2png1txt
│       │   │   │   ├── file1.png
│       │   │   │   ├── file2.png
│       │   │   │   ├── request.txt
│       │   │   │   └── text.txt
│       │   │   ├── firefox3-2pnglongtext
│       │   │   │   ├── file1.png
│       │   │   │   ├── file2.png
│       │   │   │   ├── request.txt
│       │   │   │   └── text.txt
│       │   │   ├── ie6-2png1txt
│       │   │   │   ├── file1.png
│       │   │   │   ├── file2.png
│       │   │   │   ├── request.txt
│       │   │   │   └── text.txt
│       │   │   ├── ie7_full_path_request.txt
│       │   │   ├── opera8-2png1txt
│       │   │   │   ├── file1.png
│       │   │   │   ├── file2.png
│       │   │   │   ├── request.txt
│       │   │   │   └── text.txt
│       │   │   └── webkit3-2png1txt
│       │   │       ├── file1.png
│       │   │       ├── file2.png
│       │   │       ├── request.txt
│       │   │       └── text.txt
│       │   ├── res
│       │   │   └── test.txt
│       │   ├── routing.py
│       │   ├── security.py
│       │   ├── serving.py
│       │   ├── test.py
│       │   ├── urls.py
│       │   ├── utils.py
│       │   ├── wrappers.py
│       │   └── wsgi.py
│       ├── urls.py
│       ├── useragents.py
│       ├── utils.py
│       ├── wrappers.py
│       └── wsgi.py
├── README.md
└── utils
    ├── auth-and-populate.py
    └── populate-sqlite.py

160 directories, 1488 files
