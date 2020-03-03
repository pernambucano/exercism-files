def square(number):
    if number <= 0 or number > 64:
        raise ValueError("Impossible number")
    return 2 ** (number - 1)


def total():
    return sum((square(n) for n in range(1, 65)))
