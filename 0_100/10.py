"""
Source: Geeks for Geeks
"""

n = 10

# list to store prime numbers 
prime = [True] * (n + 1) 
print(prime)
    
# Create a boolean array "prime[0..n]" 
# and initialize all entries in it as true. 
# A value in prime[i] will finally be 
# false if i is Not a prime, else true. 
    
p = 2
while p * p <= n: 
    # If prime[p] is not changed, then 
    # it is a prime 
    if prime[p] == True: 
        # Update all multiples of p 
        i = p * 2
        while i <= n: 
            prime[i] = False
            i += p 
    p += 1    
        
# Return sum of primes generated through 
# Sieve. 
sum = 0
for i in range (2, n + 1): 
    if(prime[i]): 
        sum += i 
    
print(sum)