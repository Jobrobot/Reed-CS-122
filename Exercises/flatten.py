def flatten(x):
    b = []

    for n in range(len(x)):
        if isinstance(x[n], list):
            b += flatten(x[n])
        else:
            b.append(x[n])

    return b