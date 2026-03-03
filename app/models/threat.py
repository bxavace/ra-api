"""Threat source and assessment threat models."""
from app.models.base import BaseModel, db


class ThreatSource(BaseModel):
    """Master list of threat sources."""
    __tablename__ = "threat_source"

    name = db.Column(db.String(150), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)

    # Relationship
    assessment_threats = db.relationship("AssessmentThreat", backref="threat_source", lazy=True)

    def __repr__(self):
        return f"<ThreatSource {self.name}>"


class AssessmentThreat(BaseModel):
    """Threat event and mitigation details per assessment."""
    __tablename__ = "assessment_threat"

    demographics_id = db.Column(db.Integer, db.ForeignKey("demographics.id"), nullable=False)
    threat_source_id = db.Column(db.Integer, db.ForeignKey("threat_source.id"), nullable=False)
    main_threat_event = db.Column(db.Text, nullable=False)
    mitigation_summary = db.Column(db.Text, nullable=True)

    # Relationship
    demographics = db.relationship("Demographics", backref="assessment_threats", lazy=True)

    def __repr__(self):
        return f"<AssessmentThreat assessment={self.demographics_id}, threat_source={self.threat_source_id}>"
