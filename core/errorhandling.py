from . import APP
from flask import make_response, json

#from werkzeug.exceptions import HTTPException

# this may be of interest:
# http://werkzeug.pocoo.org/docs/0.11/exceptions/#werkzeug.exceptions.HTTPException
# http://werkzeug.pocoo.org/docs/0.11/exceptions/#werkzeug.exceptions.BadRequest
# http://jsonapi.org/format/#errors
# http://flask.pocoo.org/docs/0.11/api/#flask.Flask.errorhandler

@APP.errorhandler(400)
def bad_request(error):
    errors_obj = { 'errors': {
        'status': '400',
        'title': 'BadRequest'
        }
    }
    return json.dumps(errors_obj), 400

@APP.errorhandler(401)
def unauthorized(error):
    errors_obj = { 'errors': {
        'status': '401',
        'title': 'Unauthorized'
        }
    }
    return json.dumps(errors_obj), 401

@APP.errorhandler(403)
def unauthorized(error):
    errors_obj = { 'errors': {
        'status': '403',
        'title': 'Unauthorized'
        }
    }
    return json.dumps(errors_obj), 403

@APP.errorhandler(404)
def not_found(error):
    errors_obj = { 'errors': {
        'status': '404',
        'title': 'NotFound'
        }
    }
    return json.dumps(errors_obj), 404

@APP.errorhandler(405)
def method_not_allowed(error):
    errors_obj = { 'errors': {
        'status': '405',
        'title': 'MethodNotAllowed'
        }
    }
    return json.dumps(errors_obj), 405

@APP.errorhandler(500)
def internal_server_error(error):
    errors_obj = { 'errors': {
        'status': '404',
        'title': 'InternalServerError'
        }
    }
    return json.dumps(errors_obj), 500
