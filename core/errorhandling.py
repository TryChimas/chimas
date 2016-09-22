from . import APP
from flask import make_response, json

#from werkzeug.exceptions import HTTPException

# this may be of interest:
# http://werkzeug.pocoo.org/docs/0.11/exceptions/#werkzeug.exceptions.HTTPException
# http://werkzeug.pocoo.org/docs/0.11/exceptions/#werkzeug.exceptions.BadRequest
# http://jsonapi.org/format/#errors
# http://flask.pocoo.org/docs/0.11/api/#flask.Flask.errorhandler

def json_error_response(code, title):
    errors_json = json.dumps({
    'errors': {
        'status': code,
        'title': title
        }
    })

    return (errors_json, code, None)

@APP.errorhandler(400)
def bad_request(error):
    return json_error_response(400, 'BadRequest')

@APP.errorhandler(401)
def unauthorized(error):
    return json_error_response(401, 'Unauthorized')

@APP.errorhandler(403)
def unauthorized(error):
    return json_error_response(403, 'Forbidden')

@APP.errorhandler(404)
def not_found(error):
    return json_error_response(404, 'NotFound')

@APP.errorhandler(405)
def method_not_allowed(error):
    return json_error_response(405, 'MethodNotAllowed')

@APP.errorhandler(500)
def internal_server_error(error):
    return json_error_response(500, 'InternalServerError')