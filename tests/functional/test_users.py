from itsdangerous import URLSafeTimedSerializer
from flask import current_app

def test_get_registration_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/users/register' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/users/register')
    assert response.status_code == 200
    assert b'Flask Stock Portfolio App' in response.data
    assert b'User Registration' in response.data
    assert b'Email:' in response.data
    assert b'Password:' in response.data

def test_valid_registration(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/users/register' page is posted to (POST) with valid data
    THEN check the response is valid and the user is registered
    """
    response = test_client.post('/users/register',
                                data={'email': 'leegay@oregonstate.edu',
                                      'password': 'CS561SoftwareEngineering'},
                                follow_redirects=True)
    assert response.status_code == 200
    assert b"Thanks for registering, leegay@oregonstate.edu!" in response.data
    assert b'Flask Stock Portfolio App' in response.data
    assert len(outbox) == 1
    assert outbox[0].subject == 'Flask Stock Portfolio App - Confirm Your Email Address'  # Updated!
    assert outbox[0].sender == 'cs561stockportfoliomanagement@gmail.com'
    assert outbox[0].recipients[0] == 'leegay@oregonstate.edu'
    assert 'http://localhost/users/confirm/' in outbox[0].html  # New!!

def test_invalid_registration(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/users/register' page is posted to (POST) with invalid data (missing password)
    THEN check an error message is returned to the user
    """
    response = test_client.post('/users/register',
                                data={'email': 'leegay@oregonstate.edu',
                                      'password': ''},   # Empty field is not allowed!
                                follow_redirects=True)
    assert response.status_code == 200
    assert b'Thanks for registering, leegay@oregonstate.edu!' not in response.data
    assert b'Flask Stock Portfolio App' in response.data
    assert b"[This field is required.]" in response.data

def test_duplicate_registration(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/users/register' page is posted to (POST) with the email address for an existing user
    THEN check an error message is returned to the user
    """
    test_client.post('/users/register',
                     data={'email': 'leegay@oregonstate.edu',
                           'password': 'CS561SoftwareEngineering'},
                     follow_redirects=True)
    response = test_client.post('/users/register',
                                data={'email': 'leegay@oregonstate.edu',   # Duplicate email address
                                      'password': 'CS561SoftwareEngineering'},
                                follow_redirects=True)
    assert response.status_code == 200
    assert b'Thanks for registering, leegay@oregonstate.edu!' not in response.data
    assert b'Flask Stock Portfolio App' in response.data
    assert b'ERROR! Email (leegay@oregonstate.edu) already exists.' in response.data

def test_get_login_page(test_client):
    """
    GIVEN a Flask application
    WHEN the '/users/login' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/users/login')
    assert response.status_code == 200
    assert b'Login' in response.data
    assert b'Email' in response.data
    assert b'Password' in response.data
    assert b'Login' in response.data

def test_valid_login_and_logout(test_client, register_default_user):
    """
    GIVEN a Flask application
    WHEN the '/users/login' page is posted to (POST) with valid credentials
    THEN check the response is valid
    """
    response = test_client.post('/users/login',
                                data={'email': 'leegay@oregonstate.edu',
                                      'password': 'CS561SoftwareEngineering'},
                                follow_redirects=True)
    assert response.status_code == 200
    assert b'Thanks for logging in, leegay@oregonstate.edu!' in response.data
    assert b'Flask Stock Portfolio App' in response.data
    assert b'Please log in to access this page.' not in response.data

    """
    GIVEN a Flask application
    WHEN the '/users/logout' page is requested (GET) for a logged in user
    THEN check the response is valid
    """
    response = test_client.get('/users/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b'Goodbye!' in response.data
    assert b'Flask Stock Portfolio App' in response.data
    assert b'Please log in to access this page.' not in response.data

def test_invalid_login(test_client, register_default_user):
    """
    GIVEN a Flask application
    WHEN the '/users/login' page is posted to (POST) with invalid credentials (incorrect password)
    THEN check an error message is returned to the user
    """
    response = test_client.post('/users/login',
                                data={'email': 'leegay@oregonstate.edu',
                                      'password': 'IncorrectPW'},  # Incorrect!
                                follow_redirects=True)
    assert response.status_code == 200
    assert b'ERROR! Incorrect login credentials.' in response.data
    assert b'Flask Stock Portfolio App' in response.data

def test_valid_login_when_logged_in_already(test_client, register_default_user):
    """
    GIVEN a Flask application
    WHEN the '/users/login' page is posted to (POST) with value credentials for a user already logged in
    THEN check a warning is returned to the user
    """
    test_client.post('/users/login',
                     data={'email': 'leegay@oregonstate.edu',
                           'password': 'CS561SoftwareEngineering'},
                     follow_redirects=True)
    response = test_client.post('/users/login',
                                data={'email': 'leegay@oregonstate.edu',
                                      'password': 'CS561SoftwareEngineering'},
                                follow_redirects=True)
    assert response.status_code == 200
    assert b'Already logged in!' in response.data
    assert b'Flask Stock Portfolio App' in response.data

def test_invalid_logout(test_client):
    """
    GIVEN a Flask application
    WHEN the '/users/logout' page is posted to (POST)
    THEN check that a 405 error is returned
    """
    response = test_client.post('/users/logout', follow_redirects=True)
    assert response.status_code == 405
    assert b'Goodbye!' not in response.data
    assert b'Flask Stock Portfolio App' in response.data
    assert b'Method Not Allowed' in response.data

def test_invalid_logout_not_logged_in(test_client):
    """
    GIVEN a Flask application
    WHEN the '/users/logout' page is requested (GET) when the user is not logged in
    THEN check that the user is redirected to the login page
    """
    test_client.get('/users/logout', follow_redirects=True)  # Double-check that there are no logged in users!
    response = test_client.get('/users/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b'Goodbye!' not in response.data
    assert b'Flask Stock Portfolio App' in response.data
    assert b'Login' in response.data
    assert b'Please log in to access this page.' in response.data

def test_user_profile_logged_in(test_client, log_in_default_user):
    """
    GIVEN a Flask application
    WHEN the '/users/profile' page is requested (GET) when the user is logged in
    THEN check that the profile for the current user is displayed
    """
    response = test_client.get('/users/profile')
    assert response.status_code == 200
    assert b'Flask Stock Portfolio App' in response.data
    assert b'User Profile' in response.data
    assert b'Email: leegay@oregonstate.edu' in response.data

def test_user_profile_not_logged_in(test_client):
    """
    GIVEN a Flask application
    WHEN the '/users/profile' page is requested (GET) when the user is NOT logged in
    THEN check that the user is redirected to the login page
    """
    response = test_client.get('/users/profile', follow_redirects=True)
    assert response.status_code == 200
    assert b'Flask Stock Portfolio App' in response.data
    assert b'User Profile!' not in response.data
    assert b'Email: leegay@oregonstate.edu' not in response.data
    assert b'Please log in to access this page.' in response.data

def test_navigation_bar_logged_in(test_client, log_in_default_user):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET) when the user is logged in
    THEN check that the 'List Stocks', 'Add Stock', 'Profile' and 'Logout' links are present
    """
    response = test_client.get('/')
    assert response.status_code == 200
    assert b'Flask Stock Portfolio App' in response.data
    assert b'Welcome to the Flask Stock Portfolio App!' in response.data
    assert b'List Stocks' in response.data
    assert b'Add Stock' in response.data
    assert b'Profile' in response.data
    assert b'Logout' in response.data
    assert b'Register' not in response.data
    assert b'Login' not in response.data

def test_navigation_bar_not_logged_in(test_client):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET) when the user is not logged in
    THEN check that the 'Register' and 'Login' links are present
    """
    response = test_client.get('/')
    assert response.status_code == 200
    assert b'Flask Stock Portfolio App' in response.data
    assert b'Welcome to the Flask Stock Portfolio App!' in response.data
    assert b'Register' in response.data
    assert b'Login' in response.data
    assert b'List Stocks' not in response.data
    assert b'Add Stock' not in response.data
    assert b'Profile' not in response.data
    assert b'Logout' not in response.data

def test_login_with_next_valid_path(test_client, register_default_user):
    """
    GIVEN a Flask application
    WHEN the 'users/login?next=%2Fusers%2Fprofile' page is posted to (POST) with a valid user login
    THEN check that the user is redirected to the user profile page
    """
    response = test_client.post('users/login?next=%2Fusers%2Fprofile',
                                data={'email': 'leegay@oregonstate.edu',
                                      'password': 'CS561SoftwareEngineering'},
                                follow_redirects=True)
    assert response.status_code == 200
    assert b'Flask Stock Portfolio App' in response.data
    assert b'User Profile' in response.data
    assert b'Email: leegay@oregonstate.edu' in response.data

    # Log out the user - Clean up!
    test_client.get('/users/logout', follow_redirects=True)

def test_login_with_next_invalid_path(test_client, register_default_user):
    """
    GIVEN a Flask application
    WHEN the 'users/login?next=http://www.badsite.com' page is posted to (POST) with a valid user login
    THEN check that a 400 (Bad Request) error is returned
    """
    response = test_client.post('users/login?next=http://www.badsite.com',
                                data={'email': 'leegay@oregonstate.edu',
                                      'password': 'CS561SoftwareEngineering'},
                                follow_redirects=True)
    assert response.status_code == 400
    assert b'User Profile' not in response.data
    assert b'Email: leegay@oregonstate.edu' not in response.data

def test_confirm_email_valid(test_client):
    """
    GIVEN a Flask application
    WHEN the '/users/confirm/<token>' page is requested (GET) with valid data
    THEN check that the user's email address is marked as confirmed
    """
    # Create the unique token for confirming a user's email address
    confirm_serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    token = confirm_serializer.dumps('leegay@oregonstate.edu', salt='email-confirmation-salt')

    response = test_client.get('/users/confirm/'+token, follow_redirects=True)
    assert response.status_code == 200
    assert b'Thank you for confirming your email address!' in response.data
    user = User.query.filter_by(email='leegay@oregonstate.edu').first()
    assert user.email_confirmed

def test_confirm_email_already_confirmed(test_client):
    """
    GIVEN a Flask application
    WHEN the '/users/confirm/<token>' page is requested (GET) with valid data
         but the user's email is already confirmed
    THEN check that the user's email address is marked as confirmed
    """
    # Create the unique token for confirming a user's email address
    confirm_serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    token = confirm_serializer.dumps('leegay@oregonstate.edu', salt='email-confirmation-salt')

    # Confirm the user's email address
    test_client.get('/users/confirm/'+token, follow_redirects=True)

    # Process a valid confirmation link for a user that has their email address already confirmed
    response = test_client.get('/users/confirm/'+token, follow_redirects=True)
    assert response.status_code == 200
    assert b'Account already confirmed.' in response.data
    user = User.query.filter_by(email='leegay@oregonstate.edu').first()
    assert user.email_confirmed

def test_confirm_email_invalid(test_client):
    """
    GIVEN a Flask application
    WHEN the '/users/confirm/<token>' page is is requested (GET) with invalid data
    THEN check that the link was not accepted
    """
    response = test_client.get('/users/confirm/bad_confirmation_link', follow_redirects=True)
    assert response.status_code == 200
    assert b'The confirmation link is invalid or has expired.' in response.data

def test_get_login_page(test_client):
    """
    GIVEN a Flask application
    WHEN the '/users/login' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/users/login')
    assert response.status_code == 200
    assert b'Login' in response.data
    assert b'Email' in response.data
    assert b'Password' in response.data
    assert b'Login' in response.data
    assert b'Forgot your password?' in response.data

def test_get_password_reset_via_email_page(test_client):
    """
    GIVEN a Flask application
    WHEN the '/users/password_reset_via_email' page is requested (GET)
    THEN check that the page is successfully returned
    """
    response = test_client.get('/users/password_reset_via_email', follow_redirects=True)
    assert response.status_code == 200
    assert b'Password Reset via Email' in response.data
    assert b'Email:' in response.data
    assert b'Submit' in response.data

def test_post_password_reset_via_email_page_valid(test_client, confirm_email_default_user):
    """
    GIVEN a Flask application
    WHEN the '/users/password_reset_via_email' page is posted to (POST) with a valid email address
    THEN check that an email was queued up to send
    """
    with mail.record_messages() as outbox:
        response = test_client.post('/users/password_reset_via_email',
                                    data={'email': 'leegay@oregonstate.edu'},
                                    follow_redirects=True)
        assert response.status_code == 200
        assert b'Please check your email for a password reset link.' in response.data
        assert len(outbox) == 1
        assert outbox[0].subject == 'Flask Stock Portfolio App - Password Reset Requested'
        assert outbox[0].sender == 'cs561stockportfoliomanagement@gmail.com'
        assert outbox[0].recipients[0] == 'leegay@oregonstate.edu'
        assert 'Questions? Comments?' in outbox[0].html
        assert 'cs561stockportfoliomanagement@gmail.com' in outbox[0].html
        assert 'http://localhost/users/password_reset_via_token/' in outbox[0].html

def test_post_password_reset_via_email_page_invalid(test_client):
    """
    GIVEN a Flask application
    WHEN the '/users/password_reset_via_email' page is posted to (POST) with an invalid email address
    THEN check that an error message is flashed
    """
    with mail.record_messages() as outbox:
        response = test_client.post('/users/password_reset_via_email',
                                    data={'email': 'notleegay@oregonstate.edu'},
                                    follow_redirects=True)
        assert response.status_code == 200
        assert len(outbox) == 0
        assert b'Error! Invalid email address!' in response.data

def test_post_password_reset_via_email_page_not_confirmed(test_client, log_in_default_user):
    """
    GIVEN a Flask application
    WHEN the '/users/password_reset_via_email' page is posted to (POST) with a email address that has not been confirmed
    THEN check that an error message is flashed
    """
    with mail.record_messages() as outbox:
        response = test_client.post('/users/password_reset_via_email',
                                    data={'email': 'leegay@oregonstate.edu'},
                                    follow_redirects=True)
        assert response.status_code == 200
        assert len(outbox) == 0
        assert b'Your email address must be confirmed before attempting a password reset.' in response.data

def test_get_password_reset_valid_token(test_client):
    """
    GIVEN a Flask application
    WHEN the '/users/password_reset_via_email/<token>' page is requested (GET) with a valid token
    THEN check that the page is successfully returned
    """
    password_reset_serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    token = password_reset_serializer.dumps('leegay@oregonstate.edu'', salt='password-reset-salt')

    response = test_client.get('/users/password_reset_via_token/' + token, follow_redirects=True)
    assert response.status_code == 200
    assert b'Password Reset:' in response.data
    assert b'New Password:' in response.data
    assert b'Submit' in response.data
