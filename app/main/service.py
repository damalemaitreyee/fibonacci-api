from app.main.model import Fibonacci, create_fibonacci
from flask import current_app


class FibonacciService:
    def get_fibonacci(self, number):
        current_app.logger.info("Get fibonacci series till %s", number)
        fib_series = self.get_fibonacci_by_number(number)
        if not fib_series:
            current_app.logger.info("Fibonacci series till %s is not present in database", number)
            fib_series = self.generate_fibonacci(number)
            create_fibonacci(number, self.list_to_string(fib_series))
        return fib_series

    def get_fibonacci_by_number(self, number):
        fibonacci = Fibonacci.query.get(number)
        if fibonacci and fibonacci.series:
            return self.string_to_list(fibonacci.series)

    def generate_fibonacci(self, number):
        current_app.logger.info("Generating Fibonacci series till %s", number)
        if number <= 0:
            return []
        memo = [0] * (number + 1)
        memo[1] = 0
        if number > 1:
            memo[2] = 1

        for i in range(3, number + 1):
            memo[i] = memo[i - 1] + memo[i - 2]

        return memo[1:]

    @staticmethod
    def list_to_string(mylist):
        return ', '.join(map(str, mylist))

    @staticmethod
    def string_to_list(mystr):
        return [int(num) for num in mystr.split(",")]
