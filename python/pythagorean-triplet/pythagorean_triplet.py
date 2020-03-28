import math


def triplets_with_sum(number):
    list_of_triplets = []
    for x in range(1, number):
        x2 = x * x
        for y in range(x + 1, number):
            z = number - x - y
            z2 = z * z
            y2 = y * y
            if z > 0 and (z2 == x2 + y2):
                list_of_triplets.append([x, y, z])
    return list_of_triplets
