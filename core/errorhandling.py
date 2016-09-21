from . import APP
from flask import make_response

from werkzeug.exceptions import HTTPException

# this may be of interest:
# http://werkzeug.pocoo.org/docs/0.11/exceptions/#werkzeug.exceptions.HTTPException

@APP.errorhandler(404)
def not_found(error):
    return "sorry buddy, not found", 404
