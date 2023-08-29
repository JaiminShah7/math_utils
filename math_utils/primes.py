def isprime(n):
    from math import sqrt,floor
    if n==1:
        return False
    for m in range(2,floor(sqrt(n))+1):
        if n%m == 0:
            return False
    return True