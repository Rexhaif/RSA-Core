from flask import Flask, jsonify
from .utils import ListConverter

from .controllers import *

application = Flask("rsa-core")

application.url_map.converters['list'] = ListConverter

application.register_blueprint(docs)
application.register_blueprint(corps)
application.register_blueprint(read)
application.register_blueprint(manage)
application.register_blueprint(admin)


@application.route("/")
def index():
    return jsonify({"msg": "ok"})


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=8888)
