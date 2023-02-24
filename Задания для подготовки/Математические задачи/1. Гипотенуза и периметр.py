import math

def hypotenuse():
    a = int(input('Первый катет: '))
    b = int(input('Второй катет: '))
    cc = a ** 2 + b ** 2
    c = math.sqrt(cc)
    print(f'Гипотенуза равна {c}')
    triang_sum(a, b, c)

def triang_sum(a, b, c):
    print(f'Периметр треугольника: {a + b + c}')

hypotenuse()