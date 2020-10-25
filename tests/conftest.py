from project import create_app
import pytest
from flask import current_app
from project.models import Stock, User
from project import database
from datetime import datetime


@pytest.fixture(scope='module')
def new_stock():
    stock = Stock('AAPL', '16', '406.78')
    return stock

@pytest.fixture(scope='module')
def new_user():
    user = User('leegay@oregonstate.edu', 'CS561SoftwareEngineering')
    return user

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app()
    flask_app.config.from_object('config.TestingConfig')
    flask_app.extensions['mail'].suppress = True

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context before accessing the logger and database
        with flask_app.app_context():
            flask_app.logger.info('Creating database tables in test_client fixture...')

            # Create the database and the database table(s)
            database.create_all()

        yield testing_client  # this is where the testing happens!

        with flask_app.app_context():
            database.drop_all()

@pytest.fixture(scope='module')
def register_default_user(test_client):
    user = User('leegay@oregonstate.edu', 'CS561SoftwareEngineering')
    database.session.add(user)
    database.session.commit()
    return user

@pytest.fixture(scope='function')
def log_in_default_user(test_client, register_default_user):
    # Log in the user
    test_client.post('/users/login',
                     data={'email': 'leegay@oregonstate.edu',
                           'password': 'CS561SoftwareEngineering'},
                     follow_redirects=True)

    yield register_default_user  # this is where the testing happens!

    # Log out the user
    test_client.get('/users/logout', follow_redirects=True)

@pytest.fixture(scope='function')
def confirm_email_default_user(test_client, log_in_default_user):
    # Mark the user as having their email address confirmed
    user = User.query.filter_by(email='leegay@oregonstate.edu').first()
    user.email_confirmed = True
    user.email_confirmed_on = datetime(2020, 7, 8)
    database.session.add(user)
    database.session.commit()

    yield user  # this is where the testing happens!

    # Mark the user as not having their email address confirmed (clean up)
    user = User.query.filter_by(email='leegay@oregonstate.edu').first()
    user.email_confirmed = False
    user.email_confirmed_on = None
    database.session.add(user)
    database.session.commit()
