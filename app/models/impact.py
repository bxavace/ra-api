"""Impact category and assessment impact models."""
from app.models.base import BaseModel, db

class ImpactCategory(BaseModel):
    """Fixed categories of impact (degradation, damage, etc)."""
    __tablename__ = "impact_category"

    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)

    # Relationship
    assessment_impacts = db.relationship("AssessmentImpact", backref="impact_category", lazy=True)

    def __repr__(self):
        return f"<ImpactCategory {self.name}>"

class AssessmentImpact(BaseModel):
    """User-selected impact and justification per assessment and category."""
    __tablename__ = "assessment_impact"

    demographics_id = db.Column(db.Integer, db.ForeignKey("demographics.id"), nullable=False)
    impact_category_id = db.Column(db.Integer, db.ForeignKey("impact_category.id"), nullable=False)
    adverse_effect = db.Column(db.String(100), nullable=False)
    value = db.Column(db.String(50), nullable=False)
    justification = db.Column(db.Text, nullable=True)

    # Relationship
    demographics = db.relationship("Demographics", backref="assessment_impacts", lazy=True)

    __table_args__ = (
        db.UniqueConstraint("demographics_id", "impact_category_id", name="uq_assessment_impact"),
    )

    def __repr__(self):
        return f"<AssessmentImpact assessment={self.demographics_id} category={self.impact_category_id}>"
