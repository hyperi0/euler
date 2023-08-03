
def getPrimes(n):

    isPrime = [True for i in range(n+1)]

    for i in range(2, int(n/2)+1):
        if isPrime[i]:
            for j in range(2, int(n/i)+1):
                if i*j < n+1: isPrime[i*j] = False

    return [p for p in range(2, n+1) if isPrime[p]]

familySize = 7
primes = getPrimes(100000)

for p in primes:

    n = str(p)
    digits = len(n)

    masks = []

    for i in range(2**digits):
        mask = bin(i)[2:]
        masks.append(mask.rjust(digits, "0"))

    for mask in masks:
        family = set()

        for i in range(10):
            newVal = []

            for digit in range(digits):
                newVal.append(n[digit] if mask[digit] == "0" else str(i))

            if newVal[0] != "0":
                newVal = int("".join(newVal))
                if newVal in primes: family.add(newVal)

        if len(family) >= familySize:
            print(n)
