import toml

from core import ROOT_PATH, ETC_PATH

DEFAULT_CONFIG_FILEPATH = ETC_PATH + "/chimas-default.conf"
USER_CONFIG_FILEPATH = ROOT_PATH + "/chimas.conf"

with open(DEFAULT_CONFIG_FILEPATH) as default_config_file:
    default_config = toml.loads(default_config_file.read())

with open(USER_CONFIG_FILEPATH) as user_config_file:
    user_config = toml.loads(user_config_file.read())

chimas_config = default_config
chimas_config.update(user_config)

#class ConfigParser:
#    def __init__(self, config_file = USER_CONFIG_FILE):
#        pass
