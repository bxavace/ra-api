"""Policy and regulation models."""
from app.models.base import BaseModel, db


class PolicyRegulation(BaseModel):
    """Master list of policies and regulations available for assessments."""
    __tablename__ = "policy_regulation"

    name = db.Column(db.String(150), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    
    # Relationship
    assessment_policies = db.relationship(
        "AssessmentPolicyRegulation",
        backref="policy_regulation",
        lazy=True,
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<PolicyRegulation {self.name}>"


class AssessmentPolicyRegulation(BaseModel):
    """Track which policies/regulations are applicable to each assessment with specific details."""
    __tablename__ = "assessment_policy_regulation"

    # Foreign keys
    demographics_id = db.Column(db.Integer, db.ForeignKey("demographics.id"), nullable=False)
    policy_regulation_id = db.Column(db.Integer, db.ForeignKey("policy_regulation.id"), nullable=False)
    
    # Applicability status
    is_applicable = db.Column(db.Boolean, nullable=False, default=False)
    
    # Optional section details
    section_details = db.Column(db.Text, nullable=True)
    
    # Relationship
    demographics = db.relationship("Demographics", backref="policy_regulations", lazy=True)
    
    # Unique constraint: one policy per assessment
    __table_args__ = (
        db.UniqueConstraint("demographics_id", "policy_regulation_id", name="uq_assessment_policy"),
    )

    def __repr__(self):
        return f"<AssessmentPolicyRegulation assessment={self.demographics_id}, policy={self.policy_regulation_id}>"
