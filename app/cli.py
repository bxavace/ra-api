"""Flask CLI commands."""
import click
from flask.cli import with_appcontext
from app.seeders.seed_choices import seed_choices
from app.seeders.seed_policies import seed_policies


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


def register_cli_commands(app):
    """Register all CLI commands with the Flask app."""
    app.cli.add_command(seed_choices_command)
    app.cli.add_command(seed_policies_command)
