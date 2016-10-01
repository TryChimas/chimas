#from . import app
from flask import make_response, json
from flask import current_app as app

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

    #@app.errorhandler(400)
    def bad_request(self, error):
        return json_error_response(400, 'BadRequest')

    #@app.errorhandler(401)
    def unauthorized(self, error):
        return json_error_response(401, 'Unauthorized')

    #@app.errorhandler(403)
    def forbidden(self, error):
        return json_error_response(403, 'Forbidden')

    #@app.errorhandler(404)
    def not_found(self, error):
        return json_error_response(404, 'NotFound')

    #@app.errorhandler(405)
    def method_not_allowed(self, error):
        return json_error_response(405, 'MethodNotAllowed')

    #@app.errorhandler(500)
    def internal_server_error(self, error):
        return json_error_response(500, 'InternalServerError')
