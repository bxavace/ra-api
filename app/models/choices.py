"""Lookup tables for choice fields in assessments."""
from app.models.base import BaseModel, db


class GlobalProcess(BaseModel):
    """Available global process options for assessments."""
    __tablename__ = "global_process"

    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)

    # Relationship
    assessments = db.relationship("Demographics", backref="global_process", lazy=True)

    def __repr__(self):
        return f"<GlobalProcess {self.name}>"


class ProcessLevel(BaseModel):
    """Available process level options for assessments."""
    __tablename__ = "process_level"

    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)

    # Relationship
    assessments = db.relationship("Demographics", backref="process_level", lazy=True)

    def __repr__(self):
        return f"<ProcessLevel {self.name}>"


class AssetCrownJewels(BaseModel):
    """Available asset crown jewels status options for assessments."""
    __tablename__ = "asset_crown_jewels"

    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)

    # Relationship
    assessments = db.relationship("Demographics", backref="asset_crown_jewels", lazy=True)

    def __repr__(self):
        return f"<AssetCrownJewels {self.name}>"
