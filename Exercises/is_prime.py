x = 14

def is_prime(x):
    if x <= 1:
        return False

    divisor = 2

    while divisor < x:
        if x % divisor == 0:
            return False
        divisor += 1
    return True
    
print(is_prime(x))