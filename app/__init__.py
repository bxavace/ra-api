from flask import Flask
from flask_migrate import Migrate
from config import Config
from app.models.base import db

migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

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
    )

    # from app import routes
    # app.register_blueprint(routes.bp)

    from app.cli import register_cli_commands
    register_cli_commands(app)

    return app