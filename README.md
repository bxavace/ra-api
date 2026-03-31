# ra-api

A Flask-based REST API for conducting and storing risk assessments. It provides endpoints for submitting structured assessment data and retrieving lookup metadata used to populate assessment forms.

## Table of Contents

- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Configuration Reference](#configuration-reference)
- [Database Migrations](#database-migrations)
- [CLI Seed Commands](#cli-seed-commands)
- [Contributing](#contributing)

---

## Project Overview

`ra-api` supports a multi-step risk assessment workflow that captures:

- **Demographics** – assessor details, process context, and asset classification
- **Policies & Regulations** – applicability of policy and regulatory controls
- **Vulnerabilities** – identified weaknesses and root-cause analysis
- **Threats** – threat sources, events, and mitigations
- **Threat Probabilities** – likelihood and impact ratings per threat
- **Impacts** – adverse effects across defined impact categories
- **Initial Risk** – overall probability, impact, risk statement, and chosen risk response

---

## Project Structure

```
ra-api/
├── app/
│   ├── __init__.py          # Application factory (create_app)
│   ├── cli.py               # Flask CLI seed commands
│   ├── routes.py            # API route definitions
│   ├── schema.py            # Marshmallow validation schemas
│   ├── utils.py             # Shared utility helpers
│   ├── constants/           # Static lookup tables (impact matrix, risk table, probability table)
│   ├── models/              # SQLAlchemy ORM models
│   │   ├── base.py          # Shared BaseModel and db instance
│   │   ├── choices.py       # GlobalProcess, ProcessLevel, AssetCrownJewels
│   │   ├── demographics.py  # Demographics model
│   │   ├── impact.py        # ImpactCategory, AssessmentImpact
│   │   ├── policy.py        # PolicyRegulation, AssessmentPolicyRegulation
│   │   ├── probability.py   # AssessmentThreatProbability
│   │   ├── risk.py          # RiskResponse, InitialRisk
│   │   ├── threat.py        # ThreatSource, AssessmentThreat
│   │   └── vulnerability.py # Vulnerability, AssessmentVulnerability
│   ├── seeders/             # Scripts to populate lookup tables
│   └── services/
│       └── assessment_service.py  # Business logic for creating assessments
├── migrations/              # Alembic/Flask-Migrate migration files
├── config.py                # Configuration classes (Development, Production)
├── main.py                  # Application entry point
├── pyproject.toml           # Project metadata and dependencies
├── requirements.txt         # Pinned runtime dependencies
├── .env.example             # Example environment variable file
└── .python-version          # Required Python version (3.14)
```

---

## Prerequisites

| Requirement | Version  | Notes                                                     |
|-------------|----------|-----------------------------------------------------------|
| Python      | 3.14+    | Defined in `.python-version`                              |
| uv          | latest   | Recommended package/environment manager                   |

Install `uv` by following the [official installation guide](https://docs.astral.sh/uv/getting-started/installation/).

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/bxavace/ra-api.git
cd ra-api
```

### 2. Set up environment variables

Copy the example file and fill in your values:

```bash
cp .env.example .env
```

Edit `.env` as needed (see [Configuration Reference](#configuration-reference) for all available variables).

### 3. Install dependencies

Using `uv` (recommended):

```bash
uv sync
```

Or with `pip`:

```bash
pip install -r requirements.txt
```

### 4. Set up the database

Run the existing migrations to create all tables:

```bash
flask db upgrade
```

### 5. Seed the database

Populate all lookup tables in the correct order:

```bash
flask seed:all
```

---

## Running the Application

### Development

```bash
flask run
```

The server starts at `http://127.0.0.1:5000` by default. You can override the host and port via the `HOST` and `PORT` environment variables.

Alternatively, run directly through Python:

```bash
python main.py
```

### Environment selection

Set `APP_ENV` to control which configuration class is loaded:

| `APP_ENV` value        | Configuration used  |
|------------------------|---------------------|
| `development` / `dev`  | `DevelopmentConfig` |
| `production` / `prod`  | `ProductionConfig`  |

---

## API Endpoints

### `GET /api/metadata`

Returns all lookup data needed to populate an assessment form.

**Response (200)**

```json
{
  "global_processes": [...],
  "process_levels": [...],
  "asset_crown_jewels": [...],
  "policies": [...],
  "vulnerabilities": [...],
  "threat_sources": [...],
  "impact_categories": [...],
  "risk_responses": [...],
  "impact_matrix": {...},
  "ordinal_effect_description": {...},
  "risk_table": {...},
  "impact_statement": {...},
  "probability_table": {...}
}
```

---

### `POST /api/assessments`

Submits a complete risk assessment.

**Request body**

```json
{
  "demographics": {
    "date_of_assessment": "2025-01-15",
    "full_name": "Jane Doe",
    "location": "Manila",
    "design_or_execution": "Design",
    "global_process_id": 1,
    "process_level_id": 2,
    "asset_crown_jewels_id": 3,
    "geography_market_contract": "PH",
    "other_details": null
  },
  "policies": [
    { "policy_regulation_id": 1, "is_applicable": true, "section_details": "Section 3.2" }
  ],
  "vulnerabilities": [
    { "vulnerability_id": 1, "perceived_vulnerability": "Weak access controls", "five_whys": "..." }
  ],
  "threats": [
    { "threat_source_id": 1, "main_threat_event": "Unauthorized access", "mitigation_summary": "MFA enforced" }
  ],
  "threat_probabilities": [
    {
      "threat_source_id": 1,
      "probability": "Medium",
      "justification": "Historical incidents",
      "impact_probability": "High",
      "impact_justification": "Data sensitivity"
    }
  ],
  "impacts": [
    { "impact_category_id": 1, "adverse_effect": "Data breach", "value": "High", "justification": "PII exposed" }
  ],
  "initial_risk": {
    "probability": "Medium",
    "impact": "High",
    "risk_statement": "Risk of unauthorized data access due to weak controls.",
    "risk_response_id": 2,
    "justification": "Mitigate through MFA rollout"
  }
}
```

**Success response (201)**

```json
{
  "message": "Assessment submitted successfully.",
  "assessment_id": 42
}
```

**Error response (400)**

```json
{
  "error": "<validation or database error message>"
}
```

---

## Configuration Reference

All configuration is driven by environment variables. Copy `.env.example` to `.env` to get started.

| Variable                 | Default                                     | Description                                                                 |
|--------------------------|---------------------------------------------|-----------------------------------------------------------------------------|
| `APP_ENV`                | `development`                               | Runtime environment: `development` or `production`                          |
| `SECRET_KEY`             | `dev-only-change-me` *(dev only)*           | Flask secret key. **Required in production.** Generate with `openssl rand -hex 32` |
| `DATABASE_URL`           | `sqlite:///app.db`                          | SQLAlchemy database connection string                                       |
| `CORS_ORIGINS`           | `http://localhost:5173,http://127.0.0.1:5173` | Comma-separated list of allowed frontend origins for `/api/*` CORS          |
| `CORS_SUPPORTS_CREDENTIALS` | `false`                                  | Whether to allow credentials in CORS responses                              |
| `HOST`                   | `127.0.0.1`                                 | Host for `python main.py`                                                   |
| `PORT`                   | `5000`                                      | Port for `python main.py`                                                   |

---

## Database Migrations

This project uses [Flask-Migrate](https://flask-migrate.readthedocs.io/) (Alembic) to manage schema changes.

```bash
# Apply all pending migrations
flask db upgrade

# Roll back the last migration
flask db downgrade

# Generate a new migration after model changes
flask db migrate -m "describe your change"

# Show current migration state
flask db current
```

> **Note:** Always run `flask db upgrade` after pulling changes that include new migration files in `migrations/versions/`.

---

## CLI Seed Commands

Seeders populate the lookup tables that the metadata endpoint and assessment submission depend on. Run them after the initial `flask db upgrade`.

| Command                 | Description                                         |
|-------------------------|-----------------------------------------------------|
| `flask seed:all`        | Run all seeders in the correct order *(recommended)*|
| `flask seed:choices`    | Populate GlobalProcess, ProcessLevel, AssetCrownJewels |
| `flask seed:policies`   | Populate PolicyRegulation lookup table              |
| `flask seed:vulnerabilities` | Populate Vulnerability lookup table            |
| `flask seed:threats`    | Populate ThreatSource lookup table                  |
| `flask seed:impacts`    | Populate ImpactCategory lookup table                |
| `flask seed:risks`      | Populate RiskResponse lookup table                  |

---

## Contributing

1. **Fork** the repository and create a feature branch from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Install dependencies** and set up your local environment (see [Getting Started](#getting-started)).

3. **Follow the existing code style** – keep models in `app/models/`, business logic in `app/services/`, and validation schemas in `app/schema.py`.

4. **Add a migration** if you change any SQLAlchemy model:
   ```bash
   flask db migrate -m "describe your model change"
   flask db upgrade
   ```

5. **Update seeders** in `app/seeders/` if your changes introduce new lookup data.

6. **Open a Pull Request** against `main` with a clear description of your changes.
