"""Seeder for choice lookup tables."""
from app.models import db, GlobalProcess, ProcessLevel, AssetCrownJewels

GLOBAL_PROCESSES = [
    {"name": "Backup and Restore", "description": "Processes related to data backup and restoration"},
    {"name": "Configuration Item Build and Decommission", "description": "Processes for building and decommissioning configuration items"},
    {"name": "Configuration Management and Security Inventory Management", "description": "Processes for managing configuration and security inventory"},
    {"name": "Disaster Recovery Management", "description": "Processes for managing disaster recovery"},
    {"name": "Identity and Access Management", "description": "Processes for managing identity and access"},
    {"name": "Integrated Service Management", "description": "Processes for integrated service management"},
    {"name": "IT Risk Management", "description": "Processes for managing IT risk"},
    {"name": "Patch Management", "description": "Processes for managing software patches"},
    {"name": "Physical Security", "description": "Processes for managing physical security"},
    {"name": "Portable Storage Media Ops", "description": "Processes for managing portable storage media"},
    {"name": "Security Management", "description": "Processes for managing security"},
    {"name": "None - End of Life / End of Service", "description": "No applicable process - end of life or end of service"},
    {"name": "None - Nonstandard Liability Engagement", "description": "No applicable process - nonstandard liability engagement"},
    {"name": "None - Offering / Solution", "description": "No applicable process - offering or solution"},
    {"name": "Other", "description": "Other process not listed"},
]

PROCESS_LEVELS = [
    {"name": "Global Process (as-is adoption)", "description": "Adoption of global process as-is"},
    {"name": "Geography Variation", "description": "Variation of global process based on geography"},
    {"name": "Geography Exception", "description": "Exception to global process based on geography"},
    {"name": "Market Variation", "description": "Variation of global process based on market"},
    {"name": "Market Exception", "description": "Exception to global process based on market"},
    {"name": "Contract Variation", "description": "Variation of global process based on contract"},
    {"name": "Contract Exception", "description": "Exception to global process based on contract"},
    {"name": "Policy Deviation", "description": "Deviation from global process based on policy"},
]

ASSET_CROWN_JEWELS = [
    {"name": "Regulated Asset", "description": "Asset subject to regulatory requirements"},
    {"name": "Crown Jewel", "description": "Critical business asset"},
    {"name": "Both", "description": "Both regulated and crown jewel asset"},
    {"name": "Neither", "description": "Neither regulated nor crown jewel"},
]


def seed_choices():
    """Populate choice lookup tables."""
    
    # Check if data already exists to avoid duplicates
    if GlobalProcess.query.first() is not None:
        print("Choice tables already seeded. Skipping...")
        return
    
    try:
        # Seed GlobalProcess
        for process in GLOBAL_PROCESSES:
            db.session.add(GlobalProcess(**process))
        
        # Seed ProcessLevel
        for level in PROCESS_LEVELS:
            db.session.add(ProcessLevel(**level))
        
        # Seed AssetCrownJewels
        for asset in ASSET_CROWN_JEWELS:
            db.session.add(AssetCrownJewels(**asset))
        
        db.session.commit()
        print("✓ Choice tables seeded successfully!")
        
    except Exception as e:
        db.session.rollback()
        print(f"✗ Error seeding choices: {e}")
        raise
