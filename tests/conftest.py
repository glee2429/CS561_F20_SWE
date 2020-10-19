from flask import current_app
from project.models import Stock, User

@pytest.fixture(scope='module')
def new_stock():
    stock = Stock('AAPL', '16', '406.78')
    return stock

def new_user():
    user = User('patrick@email.com', 'FlaskIsAwesome123')
    return user

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app()
    flask_app.config.from_object('config.TestingConfig')

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

    # Establish an application context
    ctx = flask_app.app_context()
    ctx.push()

    current_app.logger.info('In the test_client() fixture...')

    # Pop the application context from the stack
    ctx.pop()

    yield testing_client  # this is where the testing happens!
