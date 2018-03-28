"""
Configuration of shared pytest fixtures
"""
import pytest

from api import create_app

@pytest.yield_fixture(scope='session')
def app():
    # load 'TestConfig' from config.py
    app = create_app(config_name='test')
    from api.extensions import db

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()


@pytest.yield_fixture(scope='session')
def db(app):
    from api.extensions import db as db_instance
    yield db_instance


@pytest.fixture(scope='session')
def test_client(app):
    return app.test_client()

