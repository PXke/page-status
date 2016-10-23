import click
from flask.cli import FlaskGroup
from pageStatus.database import init_db, drop_db


"""
Contains features for the database administration
"""

# Import the application
def import_app(info):
    from run_server import app
    return app

# Generate a cli (Command Line Interface) group to add features to the manage.py
@click.group(cls=FlaskGroup, create_app=import_app)
def cli():
    pass

# Features
@cli.command()
def initdb():
    """
    Initialize the database
    """
    init_db()
    click.echo('Initialized the database')

@cli.command()
def dropdb():
    """
    Drop the database
    """
    drop_db()
    click.echo('Dropped the database')

if __name__ == '__main__':
    cli()
