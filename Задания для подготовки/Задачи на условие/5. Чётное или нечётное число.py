import random

def even_or_odd():
    even = []
    odd = []
    a = random.randint(0, 50)
    b = random.randint(0, 50)
    c = random.randint(0, 50)
    print(f'Все числа: {a, b, c}')
    if a % 2 == 0: even.append(a)
    if b % 2 == 0: even.append(b)
    if c % 2 == 0: even.append(c)

    if a % 2 == 1: odd.append(a)
    if b % 2 == 1: odd.append(b)
    if c % 2 == 1: odd.append(c)

    if len(even) == 2: print(f'Нечётное число: {odd}')
    elif len(odd) == 2: print(f'Чётное число: {even}')
    else: print('Все числа чётные, либо нечётные')

even_or_odd()