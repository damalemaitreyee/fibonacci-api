import os
import pytest
from app import create_app, db


@pytest.fixture()
def app():
    os.environ["CONFIG_TYPE"] = 'config.TestConfig'
    app = create_app()
    with app.app_context():
        db.create_all()
    # other setup can go here
    yield app
    # clean up / reset resources here
    with app.app_context():
        db.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
