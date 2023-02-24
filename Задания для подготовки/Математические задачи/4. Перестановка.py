import random

def rearrangement():
    num = random.randint(100, 999)
    a = str(num // 100)
    b = str(num % 100)
    print(f'Исходное число: {num} Число послн перестановки: {b + a}')

rearrangement()