# Highly divisible triangular number
from math import sqrt

def getFactors(n):
    factors = set()
    for i in range(1, int(sqrt(n))+1):
        if n % i == 0:
            factors.add(i)
            factors.add(int(n/i))
    return factors

i = 0
t = 0
n = 500

while True:
    i += 1
    t += i

    if len(getFactors(t)) > n:
        print(t)
        break
