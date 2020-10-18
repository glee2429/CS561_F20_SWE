from flask import Flask, escape, render_template, request, session, redirect, url_for, flash
import logging
from flask.logging import default_handler
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
app.config.from_pyfile(os.environ['YOUR_APPLICATION_SETTINGS'])

app.secret_key = '\x94\xdf\x08\x97\xf1\xb2\x03\x9c\x8d~\xe7][P\x14\xe6U\xe2}\x81C;h\xf4G\xfa\xf9\xc64I\xec7'
# Remove the default logger configured by Flask
app.logger.removeHandler(default_handler)

# Logging Configuration
file_handler = RotatingFileHandler('flask-stock-portfolio.log',
                                   maxBytes=16384,
                                   backupCount=20)
file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(filename)s:%(lineno)d]')
file_handler.setFormatter(file_formatter)
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)

# Log that the Flask application is starting
app.logger.info('Starting the Flask Stock Portfolio App...')

# import the blueprints
from project.stocks import stocks_blueprint
from project.users import users_blueprint

# register the blueprints
app.register_blueprint(stocks_blueprint)
app.register_blueprint(users_blueprint, url_prefix='/users')
