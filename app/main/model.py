from app import db
from flask import current_app


class Fibonacci(db.Model):
    __tablename__ = 'fib_series'
    number = db.Column(db.Integer, primary_key=True)
    series = db.Column(db.String)

    def __repr__(self):
        return f'<Fibonacci {self.number} - {self.series}>'


def create_fibonacci(number, series):
    current_app.logger.info("Saving Fibonacci series till %s in the database", number)
    fibonacci = Fibonacci(number=number, series=series)
    db.session.add(fibonacci)
    db.session.commit()
    return fibonacci
