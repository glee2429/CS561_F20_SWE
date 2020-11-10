"""
This file (test_app.py) contains the unit tests for the app.py file.
"""


def test_index_page(test_client):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/')
    assert response.status_code == 200
    assert b'Stock Portfolio Management App' in response.data
    assert b'Welcome to the Stock Portfolio Management App!' in response.data


def test_about_page(test_client):
    """
    GIVEN a Flask application
    WHEN the '/users/about' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/users/about')
    assert response.status_code == 200
    assert b'Stock Portfolio Management App' in response.data
    assert b'About' in response.data
    assert b'This application is built using the Flask web framework.' in response.data
    assert b'CS 561 Software Engineering Project' in response.data
