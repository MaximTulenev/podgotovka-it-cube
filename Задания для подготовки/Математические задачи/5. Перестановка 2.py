import random

def rearrangement():
    num = random.randint(100, 999)
    a = str(num // 100)
    b = num % 100
    c = str(b // 10)
    d = str(b % 10)
    print(f'Исходное число: {num} Число после перестановки: {a + d + c}')

rearrangement()