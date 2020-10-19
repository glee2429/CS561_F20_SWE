"""
This file (test_models.py) contains the unit tests for the models.py file.
"""
import pytest
from models import Stock


def test_new_stock(new_stock):
    """
    GIVEN a Stock model
    WHEN a new Stock object is created
    THEN check the symbol, number of shares, and purchase price fields are defined correctly
    """
    stock = Stock('AAPL', '16', '406.78')
    assert stock.stock_symbol == 'AAPL'
    assert stock.number_of_shares == 16
    assert stock.purchase_price == 40678
def test_new_user(new_user):
    """
    GIVEN a User model
    WHEN a new User object is created
    THEN check the email is valid and hashed password does not equal the password provided
    """
    assert new_user.email == 'leegay@oregonstate.edu'
    assert new_user.password_hashed != 'CS561SWE'
