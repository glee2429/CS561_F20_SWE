"""
This file (test_app.py) contains the unit tests for the app.py file.
"""

def test_index_page(test_client):
    response = test_client.get('/')
    assert response.status_code == 200
    assert b'Flask Stock Portfolio App' in response.data
    assert b'Welcome to the Flask Stock Portfolio App!' in response.data


def test_about_page(test_client):
    response = test_client.get('/users/about')
    assert b'Flask Stock Portfolio App' in response.data
    assert b'About' in response.data
    assert b'This application is built using the Flask web framework.' in response.data
    assert b'Course developed by TestDriven.io.' in response.data
