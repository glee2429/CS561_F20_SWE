"""
This file (test_app.py) contains the unit tests for the app.py file.
"""

def test_index_page():
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b'Flask Stock Portfolio App' in response.data
        assert b'Welcome to the Flask Stock Portfolio App!' in response.data

def test_about_page():
    """
    GIVEN a Flask application
    WHEN the '/about' page is requested (GET)
    THEN check the response is valid
    """
    with app.test_client() as client:
        response = client.get('/about')
        assert response.status_code == 200
        assert b'Flask Stock Portfolio App' in response.data
        assert b'About' in response.data
        assert b'This application is built using the Flask web framework.' in response.data
