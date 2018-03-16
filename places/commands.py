"""
Custom 'Click' commands for the Flask CLI.

Execute with 'flask <command> <options>'
"""
from collections import defaultdict

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


@click.command()
@with_appcontext
def list_routes():
    """
    Print all Flask routes to the console

    From: http://ominian.com/2017/01/17/flask-list-routes-rake-equivalent/
    """

    format_str = lambda *x: "{:30s} {:40s} {}".format(*x)  # pylint: disable=W0108
    clean_map = defaultdict(list)

    for rule in current_app.url_map.iter_rules():
        methods = ",".join(rule.methods)
        clean_map[rule.endpoint].append((methods, str(rule),))

    print(format_str("View handler", "HTTP METHODS", "URL RULE"))
    print("-" * 80)
    for endpoint in sorted(clean_map.keys()):
        for rule, methods in sorted(clean_map[endpoint], key=lambda x: x[1]):
            print(format_str(endpoint, methods, rule))
