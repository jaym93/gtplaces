import pytest

from places import create_app, database
from places.database import create_tables


@pytest.yield_fixture(scope='session')
def app():
    # load 'TestConfig' from config.py
    app = create_app(config_name='test')
    from places.extensions import db

    with app.app_context():
        create_tables()
        yield app
        db.drop_all()


@pytest.yield_fixture(scope='session')
def db(app):
    from places.extensions import db as db_instance
    yield db_instance


@pytest.fixture(scope='session')
def test_client(app):
    return app.test_client()

