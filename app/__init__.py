from flask import Flask
from flask_migrate import Migrate
from config import Config
from app.models.base import db
from app.routes import bp as api_bp

migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(api_bp)

    # Import models so they're registered with db
    from app.models import (
        Demographics,
        GlobalProcess,
        ProcessLevel,
        AssetCrownJewels,
        PolicyRegulation,
        AssessmentPolicyRegulation,
        Vulnerability,
        AssessmentVulnerability,
        ThreatSource,
        AssessmentThreat,
        AssessmentThreatProbability,
        ImpactCategory,
        AssessmentImpact,
        RiskResponse,
        InitialRisk,
    )

    from app.cli import register_cli_commands
    register_cli_commands(app)

    return app