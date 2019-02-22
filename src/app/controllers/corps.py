from flask import Blueprint, request, abort, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

corps = Blueprint("corps", __name__)


@corps.route("/c/<list:corp_ids>/predicates", methods=['GET'])
def get_predicates(corp_ids):
    return jsonify({"msg": "ok"})
