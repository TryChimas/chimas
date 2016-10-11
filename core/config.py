#from core import app, ROOT_PATH, ETC_PATH
#from core import ROOT_PATH, ETC_PATH

#import click
#import toml
import configobj

# DEFAULT_CONFIG_FILEPATH = ETC_PATH + "chimas-default.conf"
# USER_CONFIG_FILEPATH = ROOT_PATH + "chimas.conf"
#
# @click.command()
# @click.option('--config', '-c', default=USER_CONFIG_FILEPATH, help="Selects user configuration filename.")
# def set_configuration_file(config):
#     DEFAULT_CONFIG_FILEPATH = config
#
# print("Opening default config file: {0}".format(DEFAULT_CONFIG_FILEPATH))
# with open(DEFAULT_CONFIG_FILEPATH) as default_config_file:
#     config_params = toml.loads(default_config_file.read())
#
# print("Opening user config file: {0}".format(USER_CONFIG_FILEPATH))
# with open(USER_CONFIG_FILEPATH) as user_config_file:
#     user_config_params = toml.loads(user_config_file.read())

#config_params.update(user_config_params)
#print(config_params)

app_config = {}
chimas_config = {}
# default_config = ImmutableDict({
#     'DEBUG':                                get_debug_flag(default=False),
#     'TESTING':                              False,
#     'PROPAGATE_EXCEPTIONS':                 None,
#     'PRESERVE_CONTEXT_ON_EXCEPTION':        None,
#     'SECRET_KEY':                           None,
#     'PERMANENT_SESSION_LIFETIME':           timedelta(days=31),
#     'USE_X_SENDFILE':                       False,
#     'LOGGER_NAME':                          None,
#     'LOGGER_HANDLER_POLICY':               'always',
#     'SERVER_NAME':                          None,
#     'APPLICATION_ROOT':                     None,
#     'SESSION_COOKIE_NAME':                  'session',
#     'SESSION_COOKIE_DOMAIN':                None,
#     'SESSION_COOKIE_PATH':                  None,
#     'SESSION_COOKIE_HTTPONLY':              True,
#     'SESSION_COOKIE_SECURE':                False,
#     'SESSION_REFRESH_EACH_REQUEST':         True,
#     'MAX_CONTENT_LENGTH':                   None,
#     'SEND_FILE_MAX_AGE_DEFAULT':            timedelta(hours=12),
#     'TRAP_BAD_REQUEST_ERRORS':              False,
#     'TRAP_HTTP_EXCEPTIONS':                 False,
#     'EXPLAIN_TEMPLATE_LOADING':             False,
#     'PREFERRED_URL_SCHEME':                 'http',
#     'JSON_AS_ASCII':                        True,
#     'JSON_SORT_KEYS':                       True,
#     'JSONIFY_PRETTYPRINT_REGULAR':          True,
#     'JSONIFY_MIMETYPE':                     'application/json',
#     'TEMPLATES_AUTO_RELOAD':                None,
# })

class ChimasConfig:
    def __init__(self, config_params):
        self.parser_function_map = {}
        self.context_data_map = {}

        self.config_params = config_params

    def parser(self, context, required_args=[]):
        """Decorator which registers a parser to be run by self.parse_config()."""

        def function_wrapper(f):
            self.parser_function_map[context] = f
            self.context_data_map[context] = { 'required_args': required_args }
            return f
        return function_wrapper

    def parse_config(self):
        """Executes all registered parsing functions."""

        for context in self.parser_function_map:

            required_args = {}
            for argument in self.context_data_map[context]['required_args']:
                 required_args.update({argument : self.config_params[argument]})

            self.parser_function_map[context](**required_args)

# config_parser = ChimasConfig(config_params)
#
# # maybe 'context' will be renamed to 'option' and passed seamlessly
# @config_parser.parser(context='servername', required_args=['listen','port'])
# def parse_server_name(listen=None, port=None):
#     #app_config['SERVER_NAME'] = listen + ":" + str(port)
#     pass
#
# config_parser.parse_config()
