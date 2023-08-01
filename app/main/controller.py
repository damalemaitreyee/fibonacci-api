from flask import request, jsonify, abort, current_app
from flask_cors import cross_origin

from . import main_blueprint
from .service import FibonacciService
from .validator import validate_input, InputValidationException

service = FibonacciService()


@cross_origin
@main_blueprint.route('/fibonacci', methods=['GET'])
def fib():
    current_app.logger.info("Here")
    if request.method == 'GET':
        try:
            if 'input' in request.args:
                fib_input = request.args['input']
                number = validate_input(fib_input)
                result = service.get_fibonacci(number)
                return jsonify(result)
            else:
                return abort(400, "Please specify the number till which you want a fibonacci series")
        except InputValidationException as e:
            abort(400, e.message)
