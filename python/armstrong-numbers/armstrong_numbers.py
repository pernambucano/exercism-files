def is_armstrong_number(number):
    number_str = str(number)
    number_length = len(number_str)
    return number == sum(int(char) ** number_length for char in number_str)
