"""Assessment threat probability model."""
from app.models.base import BaseModel, db

class AssessmentThreatProbability(BaseModel):
    """Probability and justification for threat event and impact per assessment threat."""
    __tablename__ = "assessment_threat_probability"

    assessment_threat_id = db.Column(db.Integer, db.ForeignKey("assessment_threat.id"), nullable=False, unique=True)
    probability = db.Column(db.String(50), nullable=False)  # e.g., Low, Medium, High, or numeric
    justification = db.Column(db.Text, nullable=True)
    impact_probability = db.Column(db.String(50), nullable=False)  # e.g., Low, Medium, High, or numeric
    impact_justification = db.Column(db.Text, nullable=True)

    # Relationship
    assessment_threat = db.relationship("AssessmentThreat", backref=db.backref("probability_details", uselist=False))

    def __repr__(self):
        return f"<AssessmentThreatProbability assessment_threat={self.assessment_threat_id}>"
