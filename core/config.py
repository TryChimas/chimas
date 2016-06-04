import toml

from core import ROOT_PATH, ETC_PATH

import argparse

DEFAULT_CONFIG_FILEPATH = ETC_PATH + "chimas-default.conf"
USER_CONFIG_FILEPATH = ROOT_PATH + "chimas.conf"

cliparser = argparse.ArgumentParser(description = "Chimas Server")
cliparser.add_argument(
    '-c', '--config',
        action='store',
        dest='config_filename',
        default=USER_CONFIG_FILEPATH,
        help="Selects user configuration filename." )

args = cliparser.parse_args()

class ConfigParser:

    def __init__(self, app):

        #print("Opening default config...")
        with open(DEFAULT_CONFIG_FILEPATH) as default_config_file:
            default_config = toml.loads(default_config_file.read())

        if args.config_filename:
            #print("Opening config file: [filename]...")
            with open(args.config_filename) as user_config_file:
                user_config = toml.loads(user_config_file.read())
        else:
            #print("Opening user config file: [filename]...")
            with open(USER_CONFIG_FILEPATH) as user_config_file:
                user_config = toml.loads(user_config_file.read())

        chimas_config = default_config
        chimas_config.update(user_config)

        self.parse_config(app, chimas_config)

    def parse_config(self, app, config):

        if 'listen' in config and 'port' in config:
            app.config['SERVER_NAME'] = "{0}:{1}".format(config['listen'], config['port'])
