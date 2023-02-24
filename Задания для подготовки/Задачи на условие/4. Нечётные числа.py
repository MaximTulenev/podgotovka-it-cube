import random

def sum_of_negative():
    total = 0
    a = random.randint(-50, 50)
    b = random.randint(-50, 50)
    c = random.randint(-50, 50)
    d = random.randint(-50, 50)
    e = random.randint(-50, 50)
    f = random.randint(-50, 50)
    list_of_nums = []
    if a * (-1) == abs(a): list_of_nums.append(a)
    if b * (-1) == abs(b): list_of_nums.append(b)
    if c * (-1) == abs(c): list_of_nums.append(c)
    if d * (-1) == abs(d): list_of_nums.append(d)
    if e * (-1) == abs(e): list_of_nums.append(e)
    if f * (-1) == abs(f): list_of_nums.append(f)
    for number in list_of_nums:
        total+= number
    print(list_of_nums)
    print(total)

sum_of_negative()