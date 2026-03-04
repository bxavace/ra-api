"""Service layer for creating assessments and related records."""
from app.models import (
    db, Demographics, AssessmentPolicyRegulation, AssessmentVulnerability,
    AssessmentThreat, AssessmentThreatProbability, AssessmentImpact, InitialRisk
)
from sqlalchemy.exc import SQLAlchemyError
from app.schema import AssessmentSubmissionSchema

def create_assessment(data):
    # Validate input
    schema = AssessmentSubmissionSchema()
    errors = schema.validate(data)
    if errors:
        return {"success": False, "error": errors}
    try:
        # 1. Demographics
        demo_data = data["demographics"]
        demographics = Demographics(**demo_data)
        db.session.add(demographics)
        db.session.flush()  # get demographics.id

        # 2. Policies
        for p in data.get("policies", []):
            db.session.add(AssessmentPolicyRegulation(
                demographics_id=demographics.id,
                policy_regulation_id=p["policy_regulation_id"],
                is_applicable=p["is_applicable"],
                section_details=p.get("section_details")
            ))

        # 3. Vulnerabilities
        for v in data.get("vulnerabilities", []):
            db.session.add(AssessmentVulnerability(
                demographics_id=demographics.id,
                vulnerability_id=v["vulnerability_id"],
                perceived_vulnerability=v.get("perceived_vulnerability"),
                five_whys=v.get("five_whys")
            ))

        # 4. Threats
        threat_id_map = {}
        for t in data.get("threats", []):
            threat = AssessmentThreat(
                demographics_id=demographics.id,
                threat_source_id=t["threat_source_id"],
                main_threat_event=t["main_threat_event"],
                mitigation_summary=t.get("mitigation_summary")
            )
            db.session.add(threat)
            db.session.flush()
            threat_id_map[t["threat_source_id"]] = threat.id

        # 5. Threat Probabilities
        for tp in data.get("threat_probabilities", []):
            db.session.add(AssessmentThreatProbability(
                assessment_threat_id=tp["assessment_threat_id"],
                probability=tp["probability"],
                justification=tp.get("justification"),
                impact_probability=tp["impact_probability"],
                impact_justification=tp.get("impact_justification")
            ))

        # 6. Impacts
        for i in data.get("impacts", []):
            db.session.add(AssessmentImpact(
                demographics_id=demographics.id,
                impact_category_id=i["impact_category_id"],
                adverse_effect=i["adverse_effect"],
                value=i["value"],
                justification=i.get("justification")
            ))

        # 7. Initial Risk
        ir = data["initial_risk"]
        db.session.add(InitialRisk(
            demographics_id=demographics.id,
            probability=ir["probability"],
            impact=ir["impact"],
            risk_statement=ir["risk_statement"],
            risk_response_id=ir["risk_response_id"],
            justification=ir.get("justification")
        ))

        db.session.commit()
        return {"success": True, "assessment_id": demographics.id}
    except (KeyError, SQLAlchemyError) as e:
        db.session.rollback()
        return {"success": False, "error": str(e)}
