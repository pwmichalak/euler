def fib(n):
    terms = []
    terms.append(1)
    terms.append(1)
    for i in range(2,n):
        terms.append(terms[i-1]+terms[i-2])

    return terms[n-1]

i = 1
sum = 0
x = 0
while(x < 4000000):
    x = fib(i)
    if x % 2 == 0: sum += x
    i += 1
print(sum)