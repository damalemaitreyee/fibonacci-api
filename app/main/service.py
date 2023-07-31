from app.main.model import Fibonacci, create_fibonacci
from flask import current_app

from app.main.utils import generate_fibonacci, list_to_string, string_to_list


class FibonacciService:
    def get_fibonacci(self, number):
        current_app.logger.info("Get fibonacci series till %s", number)
        fib_series = self.get_fibonacci_by_number(number)
        if not fib_series:
            current_app.logger.info("Fibonacci series till %s is not present in database", number)
            current_app.logger.info("Generating Fibonacci series till %s", number)
            fib_series = generate_fibonacci(number)
            create_fibonacci(number, list_to_string(fib_series))
        return fib_series

    def get_fibonacci_by_number(self, number):
        fibonacci = Fibonacci.query.get(number)
        if fibonacci:
            return string_to_list(fibonacci.series)
