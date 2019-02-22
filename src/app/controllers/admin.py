from flask import Blueprint, request, abort, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

admin = Blueprint("admin", __name__)


@admin.route("/org", methods=['GET'])
def get_orgs():
    return jsonify({"msg": "ok"})
