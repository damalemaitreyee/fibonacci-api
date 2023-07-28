# This blueprint will deal with fibonacci generation functionality

from flask import Blueprint

main_blueprint = Blueprint('main', __name__)

from . import controller
