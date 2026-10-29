def two_power(x):
    if x % 2 != 0:
        return x
    else:
        return two_power(x // 2)
 