# largest collatz sequence

maxN = 1000000
lengths = {}

def nextTerm(n):
    if n % 2 == 0:
        return int(n/2)
    else:
        return n*3 + 1

def chainLength(n):
    length = 1
    k = n
    while k != 1:
        if k in lengths:
            return length + lengths[k] - 1
        else:
            k = nextTerm(k)
            length += 1
    return length

for i in range(1, maxN+1):
    lengths[i] = chainLength(i)

maxLen = 0
maxStart = 0
for key in lengths:
    if lengths[key] > maxLen:
        maxLen = lengths[key]
        maxStart = key

print(maxStart, maxLen)