from flask import Blueprint, request, jsonify
from app.services.assessment_service import create_assessment

bp = Blueprint("api", __name__, url_prefix="/api")

@bp.route("/assessments", methods=["POST"])
def submit_assessment():
    data = request.get_json()
    result = create_assessment(data)
    if result["success"]:
        return jsonify({"message": "Assessment submitted successfully.", "assessment_id": result["assessment_id"]}), 201
    else:
        return jsonify({"error": result["error"]}), 400
