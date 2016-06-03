import toml

from core import ROOT_PATH, ETC_PATH

#import argparse

DEFAULT_CONFIG_FILEPATH = ETC_PATH + "/chimas-default.conf"
USER_CONFIG_FILEPATH = ROOT_PATH + "/chimas.conf"

class CliParser:

    def __init__():
        self.parser = argparse(description = "Chimas Server")
        parser.add_argument('-c', '--config', action='store', default=USER_CONFIG_FILEPATH)

    def servername(listen,port):
        return listen:port

        # this function will allow to write directly to flask/eve app.config from user config
        def configLiteral():
            pass

class ConfigParser:

    def __init__(self):

        with open(DEFAULT_CONFIG_FILEPATH) as default_config_file:
            default_config = toml.loads(default_config_file.read())

        with open(USER_CONFIG_FILEPATH) as user_config_file:
            user_config = toml.loads(user_config_file.read())

        chimas_config = default_config
        chimas_config.update(user_config)

        self.parse(chimas_config)
