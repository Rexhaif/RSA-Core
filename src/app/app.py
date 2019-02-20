from flask import Flask, jsonify
application = Flask("rsa-core")


@application.route("/")
def index():
    return jsonify({"msg": "ok"})


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=8888)
