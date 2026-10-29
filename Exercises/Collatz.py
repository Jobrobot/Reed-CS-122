def length(start):
    count = 1
    num = start

    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1

        count += 1

    return count

def collatz(x):
    start = 1

    while True:
        if length(start) >= x:
            return start

        start += 1

print(collatz(11))