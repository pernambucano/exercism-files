import math


def classify(number):
    if number <= 0:
        raise ValueError("Can not classify negative numbers")
    factors = find_factors(number)
    sum_value = sum(factors)
    if sum_value == number:
        return "perfect"
    elif sum_value < number:
        return "deficient"
    else:
        return "abundant"


def find_factors(number):
    result = set()
    for divisor in range(1, int(math.sqrt(number)) + 1):
        if number % divisor == 0 and divisor != number:
            result.add(divisor)
            if divisor != 1:
                result.add(number // divisor)
    return result
