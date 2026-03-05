"""Marshmallow schemas for assessment submission validation."""
from marshmallow import Schema, fields, validate, validates_schema, ValidationError

class DemographicsSchema(Schema):
    date_of_assessment = fields.Date(required=True)
    full_name = fields.String(required=True)
    location = fields.String(required=True)
    design_or_execution = fields.String(required=True, validate=validate.OneOf(["Design", "Execution"]))
    global_process_id = fields.Integer(required=True)
    process_level_id = fields.Integer(required=True)
    asset_crown_jewels_id = fields.Integer(required=True)
    geography_market_contract = fields.String(allow_none=True)
    other_details = fields.String(allow_none=True)

class PolicySchema(Schema):
    policy_regulation_id = fields.Integer(required=True)
    is_applicable = fields.Boolean(required=True)
    section_details = fields.String(allow_none=True)

class VulnerabilitySchema(Schema):
    vulnerability_id = fields.Integer(required=True)
    perceived_vulnerability = fields.String(allow_none=True)
    five_whys = fields.String(allow_none=True)

class ThreatSchema(Schema):
    threat_source_id = fields.Integer(required=True)
    main_threat_event = fields.String(required=True)
    mitigation_summary = fields.String(allow_none=True)

class ThreatProbabilitySchema(Schema):
    # Frontend sends threat_source_id; the service resolves the DB assessment_threat_id
    # via the threat_id_map built during threat insertion.
    threat_source_id = fields.Integer(required=True)
    probability = fields.String(required=True)
    justification = fields.String(allow_none=True)
    impact_probability = fields.String(required=True)
    impact_justification = fields.String(allow_none=True)

class ImpactSchema(Schema):
    impact_category_id = fields.Integer(required=True)
    adverse_effect = fields.String(required=True)
    value = fields.String(required=True)
    justification = fields.String(allow_none=True)

class InitialRiskSchema(Schema):
    probability = fields.String(required=True)
    impact = fields.String(required=True)
    risk_statement = fields.String(required=True)
    risk_response_id = fields.Integer(required=True)
    justification = fields.String(allow_none=True)

class AssessmentSubmissionSchema(Schema):
    demographics = fields.Nested(DemographicsSchema, required=True)
    policies = fields.List(fields.Nested(PolicySchema), required=False)
    vulnerabilities = fields.List(fields.Nested(VulnerabilitySchema), required=False)
    threats = fields.List(fields.Nested(ThreatSchema), required=False)
    threat_probabilities = fields.List(fields.Nested(ThreatProbabilitySchema), required=False)
    impacts = fields.List(fields.Nested(ImpactSchema), required=False)
    initial_risk = fields.Nested(InitialRiskSchema, required=True)
