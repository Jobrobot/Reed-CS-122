x = 3

def pyramid(x):
    result = ""

    for i in range(x):
        result += " " * (x - i - 1)
        result += ("* " * (i + 1)).strip()
        result += "\n"

    return result

print(pyramid(x))