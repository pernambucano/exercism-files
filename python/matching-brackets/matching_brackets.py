def is_paired(input_string):
    stack = []
    for char in input_string:
        if char in ["{", "[", "("]:
            stack.append(char)
        if char in ["}", "]", ")"]:
            if len(stack) == 0:
                return False
            last_item = stack.pop()
            if char == "}" and last_item == "{":
                continue
            if char == ")" and last_item == "(":
                continue
            if char == "]" and last_item == "[":
                continue
            else:
                return False
    return not stack

