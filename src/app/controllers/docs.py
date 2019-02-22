from flask import Blueprint, request, abort, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

docs = Blueprint("docs", __name__)


@docs.route("/doc/<list:doc_ids>/predicates", methods=['GET'])
def get_predicates(doc_ids):
    return jsonify({"msg": "ok"})
