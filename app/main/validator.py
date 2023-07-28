class InputValidationException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def validate_input(number):
    try:
        integer_num = int(number)
        print(integer_num)
        return integer_num
    except ValueError:
        raise InputValidationException("Invalid integer format")
