"""Initial risk and risk response models."""
from app.models.base import BaseModel, db

class RiskResponse(BaseModel):
    """Master list of risk response options and guidance statements."""
    __tablename__ = "risk_response"

    name = db.Column(db.String(50), unique=True, nullable=False)
    guidance = db.Column(db.Text, nullable=False)

    # Relationship
    initial_risks = db.relationship("InitialRisk", backref="risk_response", lazy=True)

    def __repr__(self):
        return f"<RiskResponse {self.name}>"

class InitialRisk(BaseModel):
    """Initial risk record per assessment, with probability, impact, statement, and selected response."""
    __tablename__ = "initial_risk"

    demographics_id = db.Column(db.Integer, db.ForeignKey("demographics.id"), nullable=False)
    probability = db.Column(db.String(50), nullable=False)  # e.g., Low, Medium, High
    impact = db.Column(db.String(50), nullable=False)  # e.g., Minor, Significant, High
    risk_statement = db.Column(db.Text, nullable=False)
    risk_response_id = db.Column(db.Integer, db.ForeignKey("risk_response.id"), nullable=False)
    justification = db.Column(db.Text, nullable=True)

    # Relationship
    demographics = db.relationship("Demographics", backref="initial_risks", lazy=True)

    def __repr__(self):
        return f"<InitialRisk assessment={self.demographics_id} response={self.risk_response_id}>"
