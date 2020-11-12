primes = []
i = 2
n = 10000
while len(primes) <= n+1:
    p = True
    for j in primes:
        if i % j == 0: 
            p = False
            break
    if p: primes.append(i)
    i += 1
    
print(primes[n])