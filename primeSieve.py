
def getPrimes(n):

    isPrime = [True for i in range(n+1)]

    for i in range(2, int(n/2)+1):
        if isPrime[i]:
            for j in range(2, int(n/i)+1):
                if i*j < n+1: isPrime[i*j] = False

    return [p for p in range(2, n+1) if isPrime[p]]