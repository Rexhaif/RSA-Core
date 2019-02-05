from flask import Flask, request, send_from_directory, redirect
application = Flask("rsa_app")


@application.route("/")
def index():
    return redirect("/index.html")


@application.route("/<path:path>")
def main(path):

    return send_from_directory("static", path)


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=8888)
