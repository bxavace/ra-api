"""Assessment model for demographic details."""
from app.models.base import BaseModel, db


class Demographics(BaseModel):
    """Demographics and assessment details for users conducting risk assessments."""
    __tablename__ = "demographics"

    # Mandatory fields
    date_of_assessment = db.Column(db.DateTime, nullable=False)
    full_name = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    design_or_execution = db.Column(db.String(50), nullable=False)  # "Design" or "Execution"
    
    # Foreign keys to choice tables
    global_process_id = db.Column(db.Integer, db.ForeignKey("global_process.id"), nullable=False)
    process_level_id = db.Column(db.Integer, db.ForeignKey("process_level.id"), nullable=False)
    asset_crown_jewels_id = db.Column(db.Integer, db.ForeignKey("asset_crown_jewels.id"), nullable=False)
    
    # Optional fields
    geography_market_contract = db.Column(db.String(255), nullable=True)
    
    # Free text
    other_details = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<Assessment {self.full_name} - {self.date_of_assessment}>"
