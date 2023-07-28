from app import db


class Fibonacci(db.Model):
    __tablename__ = 'fib_series'
    number = db.Column(db.Integer, primary_key=True)
    series = db.Column(db.String)

    def __repr__(self):
        return f'<Fibonacci {self.number} - {self.series}>'
