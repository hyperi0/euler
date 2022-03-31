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
        masks.append(int(bin(i)[2:].rjust(length, "0")))

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

maxCheck = 100000
isPrime = getPrimes(100000)
checked = [False for i in range(maxCheck)]

for n in range(10000,100000):
    for mask in getMasks(5):
        base = getBase(n, mask)

        if not checked[base]:
            checked[base] = True

            family = [base + mask * i for i in range(10)]
            primeFamily = [f for f in family if isPrime[f]]

            if len(primeFamily) >= familySize:
                