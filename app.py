from flask import Flask, escape, render_template, request, session, redirect, url_for, flash
import logging
from flask.logging import default_handler
from logging.handlers import RotatingFileHandler
import os
from project import create_app

# Call the application factory function to construct a Flask application
# instance using the development configuration
app = create_app()
