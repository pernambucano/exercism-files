def square_of_sum(count):
    sum = 0
    for number in range(count+1):
        sum += number
    return sum**2 

def sum_of_squares(count):
    sum = 0
    for number in range(count+1):
        sum += number**2
    return sum
    


def difference(count):
    sqsum = square_of_sum(count)
    sumsq = sum_of_squares(count)
    return sqsum - sumsq
