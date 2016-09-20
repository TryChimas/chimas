
from core import APP, ROOT_PATH, ETC_PATH

import click
import toml

from functools import wraps

DEFAULT_CONFIG_FILEPATH = ETC_PATH + "chimas-default.conf"
USER_CONFIG_FILEPATH = ROOT_PATH + "chimas.conf"

@click.command()
@click.option('--config', '-c', default=USER_CONFIG_FILEPATH, help="Selects user configuration filename.")
def set_configuration_file(config):
    DEFAULT_CONFIG_FILEPATH = config

print("Opening default config file: {0}".format(DEFAULT_CONFIG_FILEPATH))
with open(DEFAULT_CONFIG_FILEPATH) as default_config_file:
    default_config = toml.loads(default_config_file.read())

print("Opening user config file: {0}".format(USER_CONFIG_FILEPATH))
with open(USER_CONFIG_FILEPATH) as user_config_file:
    user_config = toml.loads(user_config_file.read())
#def parse_config(self, app, config):
#     if 'listen' in config and 'port' in config:
#         app.config['SERVER_NAME'] = "{0}:{1}".format(config['listen'], config['port'])

chimas_config = default_config
chimas_config.update(user_config)

def parse_args(required_args=[], optional_args=[], config_dict=chimas_config, app_config=APP.config):
    def actual_decorator(configuration_parser_function):
        @wraps(configuration_parser_function)
        def actual_function(*args, **kwargs):
            required = {}
            optional = {}

            for required_arg in required_args:
                if not required_arg in config_dict:
                    return False
                else:
                    required.update({required_arg : config_dict[required_arg]})

            for optional_arg in optional_args:
                if optional_arg in config_dict:
                    optional.update({optional_arg : config_dict[optional_arg]})

            return configuration_parser_function(required, optional, *args, **kwargs)
        return actual_function
    return actual_decorator

@parse_args(required_args=['listen','port'],config_dict=chimas_config)
#def parse_server_name( listen=config_dict['listen'], port=config_dict['port'],app_config=app_config):
def parse_server_name( req_args, opt_args ):

    APP.config['SERVER_NAME'] = ":".join( [str(req_args['listen']), str(req_args['port'])])

parse_server_name()

# cliparser = argparse.ArgumentParser(description = "Chimas Server")
# cliparser.add_argument(
#     '-c', '--config',
#         action='store',
#         dest='config_filename',
#         default=USER_CONFIG_FILEPATH,
#         help="Selects user configuration filename." )
#
# args = cliparser.parse_args()

# class ConfigParser:
#
#     def __init__(self, app):
#
# print("Opening default config file: {0}".format(DEFAULT_CONFIG_FILEPATH))
# with open(DEFAULT_CONFIG_FILEPATH) as default_config_file:
#     default_config = toml.loads(default_config_file.read())
#
#         if args.config_filename:
#             print("Opening config file: {0}".format(args.config_filename))
#             with open(args.config_filename) as user_config_file:
#                 user_config = toml.loads(user_config_file.read())
#         else:
#             print("Opening config file: {0}".format(USER_CONFIG_FILEPATH))
#             with open(USER_CONFIG_FILEPATH) as user_config_file:
#                 user_config = toml.loads(user_config_file.read())
#
#         chimas_config = default_config
#         chimas_config.update(user_config)
#
#         self.parse_config(app, chimas_config)
#
#     def parse_config(self, app, config):
#
#         if 'listen' in config and 'port' in config:
#             app.config['SERVER_NAME'] = "{0}:{1}".format(config['listen'], config['port'])
