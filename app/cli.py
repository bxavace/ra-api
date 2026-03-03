"""Flask CLI commands."""
import click
from flask.cli import with_appcontext
from app.seeders.seed_choices import seed_choices
from app.seeders.seed_policies import seed_policies
from app.seeders.seed_vulnerabilities import seed_vulnerabilities


@click.command("seed:choices")
@with_appcontext
def seed_choices_command():
    """Populate choice lookup tables."""
    seed_choices()


@click.command("seed:policies")
@with_appcontext
def seed_policies_command():
    """Populate policy and regulation lookup table."""
    seed_policies()


@click.command("seed:vulnerabilities")
@with_appcontext
def seed_vulnerabilities_command():
    """Populate vulnerabilities table with placeholder data."""
    seed_vulnerabilities()


@click.command("seed:all")
@with_appcontext
def seed_all_command():
    """Run all seeders in order."""
    seed_choices()
    seed_policies()
    seed_vulnerabilities()
    print("✓ All seeders executed.")


def register_cli_commands(app):
    """Register all CLI commands with the Flask app."""
    app.cli.add_command(seed_choices_command)
    app.cli.add_command(seed_policies_command)
    app.cli.add_command(seed_vulnerabilities_command)
    app.cli.add_command(seed_all_command)
