import math

n = 600851475143
s = int(math.ceil(math.sqrt(n)))
factors = []

for i in range(1,s+1):
    if i % 2 == 0 or i % 5 == 0: pass
    if n % i == 0:
        factors.append(i)
    
print(factors)
