import os


def _split_csv(value: str | None) -> list[str]:
    if not value:
        return []
    return [item.strip() for item in value.split(",") if item.strip()]


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///app.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CORS_ORIGINS = _split_csv(os.environ.get("CORS_ORIGINS")) or [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ]
    CORS_SUPPORTS_CREDENTIALS = False

    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    SESSION_COOKIE_SECURE = False

    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_SECURE = False

    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = os.environ.get("SECRET_KEY") or "dev-only-change-me"


class ProductionConfig(Config):
    DEBUG = False
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True


CONFIG_BY_ENV = {
    "development": DevelopmentConfig,
    "dev": DevelopmentConfig,
    "production": ProductionConfig,
    "prod": ProductionConfig,
}