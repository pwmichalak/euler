found = False
p = 0
from tqdm import tqdm
for a in tqdm(range(1,500)):
    for b in range(a,500):
        for c in range(b,500):
            if a ** 2 + b ** 2 == c ** 2 and a + b + c == 1000: 
                found = True
                print(a)
                print(b)
                print(c)
                p = a * b * c
            if found == True: break
        if found == True: break
    if found == True: break
print(p)