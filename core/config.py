
from core import APP, ROOT_PATH, ETC_PATH

import click
import toml

DEFAULT_CONFIG_FILEPATH = ETC_PATH + "chimas-default.conf"
USER_CONFIG_FILEPATH = ROOT_PATH + "chimas.conf"

@click.command()
@click.option('--config', '-c', default=USER_CONFIG_FILEPATH, help="Selects user configuration filename.")
def set_configuration_file(config):
    DEFAULT_CONFIG_FILEPATH = config

print("Opening default config file: {0}".format(DEFAULT_CONFIG_FILEPATH))
with open(DEFAULT_CONFIG_FILEPATH) as default_config_file:
    default_config_params = toml.loads(default_config_file.read())

print("Opening user config file: {0}".format(USER_CONFIG_FILEPATH))
with open(USER_CONFIG_FILEPATH) as user_config_file:
    user_config_params = toml.loads(user_config_file.read())

config_params = default_config_params.update(user_config_params)

app_config = {}
chimas_config = {}

class ChimasConfig:
    def __init__(self):
        self.function_map = {}
        self.context_map = {}
        self.option_map = {}

    def opt(self, option, short, descripton, default):
        self.option_map[option].update({
        option:{
            'option' :option,
            'short' : short,
            'description': description,
            'default': default
        }})

    def parser(self, context, required_args):
        def function_wrapper(f):
            self.function_map[context] = f
            self.context_map[context] = { 'required_args': required_args }

            return f
        return function_wrapper

    def parse_config(self, context):
        func = self.function_map.get(context, None)
        if not func:
            pass
        return func()

config_parser = ChimasConfig()

@config_parser.parser(context='servername', args=['listen','port'])
def parse_server_name(listen=None, port=None):
    app_config['SERVER_NAME'] = req['listen'] + ":" + str(req['port'])

config_parser.parse_config()
