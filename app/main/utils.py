def generate_fibonacci(number):
    if number <= 0:
        return []
    memo = [0] * (number + 1)
    memo[1] = 0
    if number > 1:
        memo[2] = 1

    for i in range(3, number + 1):
        memo[i] = memo[i - 1] + memo[i - 2]

    return memo[1:]


def list_to_string(mylist):
    return ', '.join(map(str, mylist))


def string_to_list(mystr):
    return [int(num) for num in mystr.split(",")]