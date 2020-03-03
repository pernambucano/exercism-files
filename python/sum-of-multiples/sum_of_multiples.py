def sum_of_multiples(limit, multiples):
    return sum(
        [
            number
            for number in range(limit)
            if any(number % item == 0 for item in multiples if item != 0)
        ]
    )
