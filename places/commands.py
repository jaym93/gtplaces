"""
Custom 'Click' commands for the Flask CLI.

Execute with 'flask <command> <options>'
"""
import click
from flask import current_app
from flask.cli import with_appcontext

from places import database


@click.command()
@with_appcontext
def create_db_tables():
    """
    Create the required database tables if they do not exist.
    """

    if click.confirm('Create tables in this DB? : ' + current_app.config["SQLALCHEMY_DATABASE_URI"]):
        database.create_tables()
        click.echo('Done.')
    else:
        click.echo('Canceled.')
