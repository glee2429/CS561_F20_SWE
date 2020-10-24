"""
The users Blueprint handles the user management for this application.
Specifically, this Blueprint allows for new users to register and for
users to log in and to log out of the application.
"""
from flask import Blueprint, render_template

users_blueprint = Blueprint('users', __name__, template_folder='templates')

from . import routes


@users_blueprint.errorhandler(403)
def page_forbidden(e):
  return render_template('users/403.html'), 403
