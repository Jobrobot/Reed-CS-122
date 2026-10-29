def add_to_target(target, numbers):
    if target == 0:
        return True
    if numbers == []:
        return False

    first = numbers[0]
    rest = numbers[1:]

    return (add_to_target(target - first, rest)
            or add_to_target(target, rest))