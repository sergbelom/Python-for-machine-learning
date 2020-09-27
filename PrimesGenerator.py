import math
import itertools

def isPrime(x):
    if x <= 1:
        return False
    
    n = int(math.sqrt(x))
    for i in range(2, n + 1):
        if x % i == 0:
            return False
    else:
        return True
    
def primes():
    n = 2
    while True:
        if isPrime(n):
            yield n
        n += 1