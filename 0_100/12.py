found = False
ourTriangle = 0
triangle = 1
add = 2
while not found:
    divisors = []
    for i in range(1,int(triangle ** 0.5)):
        if triangle % i == 0: divisors.append(i)
    if len(divisors) > 500: 
        found = True
        ourTriangle = triangle
    triangle += add
    add += 1
print(ourTriangle)