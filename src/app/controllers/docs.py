from flask import Blueprint, request, abort, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..config import config

docs = Blueprint("docs", __name__)
security_provider = config['security_provider']


@docs.route("/doc/<list:doc_ids>/predicates", methods=['GET'])
@jwt_required
def get_predicates(doc_ids):
    security_provider.validate_request(get_jwt_identity(), "get-predicates", doc_ids)
    return jsonify({"msg": "ok"})


@docs.route("/doc/<list:doc_ids>/lexics", methods=['GET'])
@jwt_required
def highlight_lexics(doc_ids):
    security_provider.validate_request(get_jwt_identity(), "highlight-lexics", doc_ids)
    return jsonify({"msg": "ok"})


@docs.route("/doc/<list:doc_ids>/stats", methods=['GET'])
@jwt_required
def analyze_docs(doc_ids):
    security_provider.validate_request(get_jwt_identity(), "analyze-docs", doc_ids)
    return jsonify({"msg": "ok"})


@docs.route("/doc/<list:doc_ids>/markers", methods=['GET'])
@jwt_required
def compute_markers(doc_ids):
    security_provider.validate_request(get_jwt_identity(), "compute-markers", doc_ids)
    return jsonify({"msg": "ok"})
