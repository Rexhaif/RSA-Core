from flask import Flask, jsonify
from flask_jwt_extended import JWTManager

from .config import config
from .controllers import *
from .utils import ListConverter
from .security import *

application = Flask("rsa-core")

application.config['JWT_SECRET_KEY'] = config['jwt_key']

jwt = JWTManager(application)

application.url_map.converters['list'] = ListConverter

application.register_blueprint(docs)
application.register_blueprint(corps)
application.register_blueprint(read)
application.register_blueprint(manage)
application.register_blueprint(admin)

security_provider = config['security_provider']


@application.route("/")
def index():
    return jsonify({"msg": "ok"})


#@application.route("/tokens")
#def tokens():
#    return jsonify(security_provider.create_temp_tokens())


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=config['port'])
