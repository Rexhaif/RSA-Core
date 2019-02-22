from flask import Blueprint, request, abort, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

manage = Blueprint("manage", __name__)


@manage.route("/corp", methods=['POST'])
def create_corp():
    return jsonify({"msg": "ok"})
