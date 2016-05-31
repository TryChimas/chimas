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
