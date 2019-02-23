from .security import *
import json


class InvalidConfigError(Exception):

    def __init__(self, msg):
        self.msg = msg

    def to_json(self):
        return {"msg": self.msg}


config = {

    "security_provider": DefaultSecurityProvider(None),
    "port": 8888,
    "jwt_key": "aXPnPKjBhl17Qxlo",
    "access_token_lifetime": 7,
    "refresh_token_lifetime": 180,
    "admin_token_lifetime": 9999

}


def load_from_json(path):
    with open(path, "r") as f:
        config_loaded = json.load(f)

    try:
        validate_config(config_loaded)
        config = config_loaded
    except InvalidConfigError as e:
        print(e)


def validate_config(config):
    pass
