def inverse(dictionary):
    result = {}

    for key, value in dictionary.items():
        if value in result:
            result[value].append(key)
        else:
            result[value] = [key]

    return result