from flask import current_app


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app()
    flask_app.config.from_object('config.TestingConfig')

    # Create a test client using the Flask application configured for testing
    testing_client = flask_app.test_client()

    # Establish an application context
    ctx = flask_app.app_context()
    ctx.push()

    current_app.logger.info('In the test_client() fixture...')

    # Pop the application context from the stack
    ctx.pop()

    yield testing_client  # this is where the testing happens!
