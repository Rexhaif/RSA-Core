from flask_jwt_extended import create_access_token, create_refresh_token
import datetime as dt


class SecurityProvider(object):

    def __init__(self, config):
        self.config = config

    def validate_request(self, identity, operation_id, subject):
        pass


class DefaultSecurityProvider(SecurityProvider):

    def __init__(self, config):
        SecurityProvider.__init__(self, config)

    def validate_request(self, identity, operation_id, subject):
        pass

    @staticmethod
    def create_temp_tokens():
        return {
            "access_token": create_access_token("temp", expires_delta=dt.timedelta(days=9999)),
            "refresh_token": create_refresh_token("temp", expires_delta=dt.timedelta(days=9999))
        }
