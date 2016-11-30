from flask import json

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

class ErrorHandlingAPI:
    def __init__(self, app):
        self.app = app

        error_handlers = [
            (400, self.bad_request),
            (401, self.unauthorized),
            (403, self.forbidden),
            (404, self.not_found),
            (405, self.method_not_allowed),
            (500, self.internal_server_error) ]

        for error_code, error_function in error_handlers:
            app.register_error_handler(error_code, error_function)

    def bad_request(self, error):
        return json_error_response(400, 'BadRequest')

    def unauthorized(self, error):
        return json_error_response(401, 'Unauthorized')

    def forbidden(self, error):
        return json_error_response(403, 'Forbidden')

    def not_found(self, error):
        return json_error_response(404, 'NotFound')

    def method_not_allowed(self, error):
        return json_error_response(405, 'MethodNotAllowed')

    def internal_server_error(self, error):
        return json_error_response(500, 'InternalServerError')
