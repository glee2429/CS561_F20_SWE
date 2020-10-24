"""
The stocks blueprint handles the user management for this application.
Specifically, this blueprint allows for users to add, edit, and delete
stock data from their portfolio.
"""
from flask import Blueprint

stocks_blueprint = Blueprint('stocks', __name__, template_folder='templates')

from . import routes

from flask_sqlalchemy import SQLAlchemy


#######################
#### Configuration ####
#######################

# Create the instances of the Flask extensions in the global scope,
# but without any arguments passed in. These instances are not
# attached to the Flask application at this point.
database = SQLAlchemy()

#######################
### Helper Function ###
#######################


def initialize_extensions(app):
    # Since the application instance is now created, pass it to each Flask
    # extension instance to bind it to the Flask application instance (app)
    database.init_app(app)

def create_app():
    # Create the Flask application
    app = Flask(__name__)

    # Configure the Flask application
    config_type = os.getenv('CONFIG_TYPE', 'config.DevelopmentConfig')
    app.config.from_object(config_type)

    initialize_extensions(app)  # NEW!!
    register_blueprints(app)
    configure_logging(app)
    register_error_pages(app)
    register_app_callbacks(app)
    return app
