import os
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from config import CONFIG_BY_ENV, DevelopmentConfig
from app.models.base import db
from app.routes import bp as api_bp

migrate = Migrate()

def create_app(config_name: str | None = None):
    app = Flask(__name__)

    env_name = (config_name or os.environ.get("APP_ENV") or "development").lower()
    config_class = CONFIG_BY_ENV.get(env_name, DevelopmentConfig)
    app.config.from_object(config_class)

    if env_name in {"production", "prod"} and not app.config.get("SECRET_KEY"):
        raise RuntimeError("SECRET_KEY must be set in production.")

    db.init_app(app)
    migrate.init_app(app, db)

    CORS(
        app,
        resources={r"/api/*": {"origins": app.config.get("CORS_ORIGINS", [])}},
        supports_credentials=app.config.get("CORS_SUPPORTS_CREDENTIALS", False),
    )

    @app.after_request
    def add_security_headers(response):
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        return response

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