import random

def even():
    a = random.randint(1, 1000)
    b = random.randint(1, 1000)
    c = random.randint(1, 1000)
    if a % 2 == 0: print(a)
    if b % 2 == 0: print(b)
    if c % 2 == 0: print(c)

even()