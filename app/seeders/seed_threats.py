"""Seeder for threat sources."""
from app.models import db, ThreatSource

def seed_threats():
    """Populate threat source table with user-provided values."""
    if ThreatSource.query.first() is not None:
        print("Threat sources already seeded. Skipping...")
        return
    # User-provided threat sources
    sources = [
        "Accidental Insider (Includes Errors)",
        "Adversarial Insider",
        "Adversarial Outsider",
        "Environmental",
        "Structural",
    ]
    for name in sources:
        db.session.add(ThreatSource(name=name, description="<placeholder>"))
    db.session.commit()
    print("✓ Threat sources seeded (user values). Edit descriptions as needed.")
