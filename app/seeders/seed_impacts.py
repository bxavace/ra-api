"""Seeder for impact categories."""
from app.models import db, ImpactCategory

def seed_impacts():
    """Populate impact categories with standard values."""
    if ImpactCategory.query.first() is not None:
        print("Impact categories already seeded. Skipping...")
        return
    # Impact categories
    categories = [
        {"name": "Degradation", "description": "Loss or reduction in quality or performance."},
        {"name": "Damage", "description": "Physical or logical damage to assets."},
        {"name": "Financial Loss", "description": "Direct or indirect financial impact."},
        {"name": "Reputation", "description": "Damage to reputation or public trust."},
    ]
    for cat in categories:
        db.session.add(ImpactCategory(**cat))
    db.session.commit()
    print("✓ Impact categories seeded.")
