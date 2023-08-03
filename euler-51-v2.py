import math

def getDigits(n):
    digits = []
    nd = int(math.log(n, 10)) + 1

    for digit in range(nd):
        digit = int(n / (10 ** digit)) % 10
        digits.insert(0, digit)

    return digits

def getMasks(length):
    masks = []

    for i in range(2 ** length):
        masks.append(int(bin(i)[2:]))

    return masks

def getBase(n, mask):
    base = n

    for i in range(int(math.log(n, 10) + 1)):
        base -= (int(n / (10 ** i)) % 10) * (int(mask / (10 ** i)) % 10) * 10 ** i

    return base

def getPrimes(n):

    isPrime = [True for i in range(n+1)]

    for i in range(2, int(n/2)+1):
        if isPrime[i]:
            for j in range(2, int(n/i)+1):
                if i*j < n+1: isPrime[i*j] = False

    return isPrime

familySize = 8
maxCheck = 1000000
isPrime = getPrimes(maxCheck)

for n in range(100000, maxCheck):
    if isPrime[n]:
        for mask in getMasks(6):
            base = getBase(n, mask)
            family = {base + mask * i for i in range(10)}
            primeFamily = [f for f in family if isPrime[f] and f >= 100000]

            if len(primeFamily) >= familySize:
                print(n, primeFamily)
                
