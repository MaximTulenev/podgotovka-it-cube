import random

def nums_of_num():
    num = random.randint(10, 99)
    print(f'В числе {num} содержатся {num // 10} десятков и {num % 10} единиц')

nums_of_num()