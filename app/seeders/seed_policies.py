"""Seeder for policy and regulation data."""
from app.models import db, PolicyRegulation


POLICIES = [
    {"name": "ITSS/ITCS104", "description": "Internal IT Service Standards"},
    {"name": "CSD, GSD, ISeC", "description": "Corporate Service Design, Global Service Design, IT Service Control"},
    {"name": "ITCS300", "description": "IT Control Standards 300"},
    {"name": "GSNI", "description": "Global Service and Naming Infrastructure"},
    {"name": "Cloud Security Policy", "description": "Cloud security standards and policies"},
    {"name": "ISO", "description": "International Organization for Standardization standards"},
    {"name": "FDA", "description": "Food and Drug Administration regulations"},
    {"name": "FFIEC", "description": "Federal Financial Institutions Examination Council regulations"},
    {"name": "GDPR", "description": "General Data Protection Regulation"},
    {"name": "HIPAA", "description": "Health Insurance Portability and Accountability Act"},
    {"name": "PCISSC", "description": "Payment Card Industry Security Standards Council"},
    {"name": "Other", "description": "Other policies or regulations not listed above"},
]


def seed_policies():
    """Populate policy and regulation lookup table."""
    
    # Check if data already exists to avoid duplicates
    if PolicyRegulation.query.first() is not None:
        print("Policy tables already seeded. Skipping...")
        return
    
    try:
        # Seed PolicyRegulation
        for policy in POLICIES:
            db.session.add(PolicyRegulation(**policy))
        
        db.session.commit()
        print("✓ Policy tables seeded successfully!")
        
    except Exception as e:
        db.session.rollback()
        print(f"✗ Error seeding policies: {e}")
        raise
