def isPalindrome(n):
    if n < 0: return False
    temp = n
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n = n//10
    return rev == temp

max = 0
for i in range(100,999):
    for j in range(i,999):
        x = i * j
        if isPalindrome(x) and max < x: max = x

print(max)
