def factors(value):
    list_primes = []
    divisor = 2

    while value > 1:
        if value % divisor == 0:
            list_primes.append(divisor)
            value /= divisor
        else:
            divisor += 1
    return list_primes

