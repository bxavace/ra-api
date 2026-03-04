from flask import Blueprint, request, jsonify
from app.services.assessment_service import create_assessment
from app.models import (
    GlobalProcess, ProcessLevel, AssetCrownJewels, PolicyRegulation, Vulnerability,
    ThreatSource, ImpactCategory, RiskResponse
)
from app.constants.impact_matrix import IMPACT_MATRIX, ORDINAL_EFFECT_DESC
from app.constants.risk_table import RISK_TABLE
from app.constants.probability_table import PROBABILITY_TABLE

bp = Blueprint("api", __name__, url_prefix="/api")

@bp.route("/assessments", methods=["POST"])
def submit_assessment():
    data = request.get_json()
    result = create_assessment(data)
    if result["success"]:
        return jsonify({"message": "Assessment submitted successfully.", "assessment_id": result["assessment_id"]}), 201
    else:
        return jsonify({"error": result["error"]}), 400

@bp.route("/metadata", methods=["GET"])
def get_metadata():
    return {
        "global_processes": [
            {"id": x.id, "name": x.name, "description": x.description} for x in GlobalProcess.query.all()
        ],
        "process_levels": [
            {"id": x.id, "name": x.name, "description": x.description} for x in ProcessLevel.query.all()
        ],
        "asset_crown_jewels": [
            {"id": x.id, "name": x.name, "description": x.description} for x in AssetCrownJewels.query.all()
        ],
        "policies": [
            {"id": x.id, "name": x.name, "description": x.description} for x in PolicyRegulation.query.all()
        ],
        "vulnerabilities": [
            {"id": x.id, "global_process_id": x.global_process_id, "description": x.description} for x in Vulnerability.query.all()
        ],
        "threat_sources": [
            {"id": x.id, "name": x.name, "description": x.description, "threat_category": x.threat_category, "initiation_type": x.initiation_type, "actor": x.actor, "action": x.action} for x in ThreatSource.query.all()
        ],
        "impact_categories": [
            {"id": x.id, "name": x.name, "description": x.description} for x in ImpactCategory.query.all()
        ],
        "risk_responses": [
            {"id": x.id, "name": x.name, "guidance": x.guidance} for x in RiskResponse.query.all()
        ],
        "impact_matrix": IMPACT_MATRIX,
        "ordinal_effect_description": ORDINAL_EFFECT_DESC,
        "risk_table": RISK_TABLE,
        "probability_table": PROBABILITY_TABLE
    }
