def is_paired(input_string):
    symbol_list = []
    for char in input_string:
        if char in ["{", "[", "("]:
            symbol_list.append(char)
        if char in ["}", "]", ")"]:
            if len(symbol_list) == 0:
                return False
            last_item = symbol_list.pop()
            if char == "}" and last_item == "{":
                continue
            if char == ")" and last_item == "(":
                continue
            if char == "]" and last_item == "[":
                continue
            else:
                return False
    if len(symbol_list) > 0:
        return False
    return True

