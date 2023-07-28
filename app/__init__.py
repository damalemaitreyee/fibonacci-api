import logging
import os
from logging.handlers import RotatingFileHandler

from flask import Flask, jsonify
from flask.logging import default_handler

from app.extensions import db


# Application Factory
def create_app():
    app = Flask(__name__)

    # Configure the flask app instance
    CONFIG_TYPE = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
    app.config.from_object(CONFIG_TYPE)

    # Initialize Flask extensions here. Init DB
    db.init_app(app)

    # Register blueprints
    register_blueprints(app)

    # Configure logging
    configure_logging(app)

    # Register error handlers
    register_error_handlers(app)

    return app


def register_blueprints(app):
    from app.main import main_blueprint
    app.register_blueprint(main_blueprint)


def register_error_handlers(app):
    @app.errorhandler(400)
    def bad_request(e):
        return jsonify({'error': e.description}), 400

    @app.errorhandler(404)
    def page_not_found(e):
        return jsonify({'error': e.description}), 404

    @app.errorhandler(500)
    def server_error(e):
        return jsonify({'error': e.description}), 500


def configure_logging(app):
    # Deactivate the default flask logger so that log messages don't get duplicated
    app.logger.removeHandler(default_handler)

    # Create a file handler object
    file_handler = RotatingFileHandler('flaskapp.log', maxBytes=16384, backupCount=20)

    # Set the logging level of the file handler object so that it logs INFO and up
    file_handler.setLevel(logging.INFO)

    # Create a file formatter object
    file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(filename)s: %(lineno)d]')

    # Apply the file formatter object to the file handler object
    file_handler.setFormatter(file_formatter)

    # Add file handler object to the logger
    app.logger.addHandler(file_handler)
