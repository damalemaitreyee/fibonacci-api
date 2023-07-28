from app.main.model import Fibonacci, db


class FibonacciService:
    def get_fibonacci(self, number):
        # logging.Logger.log("Inside get_fibonacci")
        fib_series = self.get_fibonacci_by_number(number)
        if not fib_series:
            fib_series = self.generate_fibonacci(number)
            self.create_fibonacci(number, self.list_to_string(fib_series))
        return fib_series

    def get_fibonacci_by_number(self, number):
        # logging.Logger.log("Inside get_fibonacci_by_number")
        fibonacci = Fibonacci.query.get(number)
        if fibonacci.series:
            return self.string_to_list(fibonacci.series)

    def create_fibonacci(self, number, series):
        # logging.Logger.log("Inside create_fibonacci")
        fibonacci = Fibonacci(number=number, series=series)
        db.session.add(fibonacci)
        db.session.commit()
        return fibonacci

    def generate_fibonacci(self, number):
        # logging.Logger.log("Inside generate_fibonacci")
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
