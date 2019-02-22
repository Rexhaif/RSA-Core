from flask import Blueprint, request, abort, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

read = Blueprint("read", __name__)


@read.route("/corp", methods=['GET'])
def get_corps():
    return jsonify({"msg": "ok"})
