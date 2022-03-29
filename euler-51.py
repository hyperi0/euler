digits = 1
primes = [False for i in range(10**digits)]

for i in range(2, int(sqrt(digits))+1):
    for j in range(1, (10**digits) / i):

