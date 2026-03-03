"""Seeder for threat sources."""
from app.models import db, ThreatSource

def seed_threats():
    """Populate threat source table with user-provided values and mappings."""
    if ThreatSource.query.first() is not None:
        print("Threat sources already seeded. Skipping...")
        return
    # User-provided threat sources and mappings
    sources = [
        {
            "name": "Accidental Insider (Includes Errors)",
            "description": "<placeholder>",
            "threat_category": "Non-adversarial",
            "initiation_type": "Threat Event Occurrence",
            "actor": "Error/Accident/Act of Nature",
            "action": "occured",
        },
        {
            "name": "Adversarial Insider",
            "description": "<placeholder>",
            "threat_category": "Adversarial",
            "initiation_type": "Threat Event Initiation",
            "actor": "Adversary",
            "action": "initiated",
        },
        {
            "name": "Adversarial Outsider",
            "description": "<placeholder>",
            "threat_category": "Adversarial",
            "initiation_type": "Threat Event Initiation",
            "actor": "Adversary",
            "action": "initiated",
        },
        {
            "name": "Environmental",
            "description": "<placeholder>",
            "threat_category": "Non-adversarial",
            "initiation_type": "Threat Event Occurrence",
            "actor": "Error/Accident/Act of Nature",
            "action": "occured",
        },
        {
            "name": "Structural",
            "description": "<placeholder>",
            "threat_category": "Non-adversarial",
            "initiation_type": "Threat Event Occurrence",
            "actor": "Error/Accident/Act of Nature",
            "action": "occured",
        },
    ]
    for src in sources:
        db.session.add(ThreatSource(**src))
    db.session.commit()
    print("✓ Threat sources seeded (user values and mappings). Edit descriptions as needed.")
