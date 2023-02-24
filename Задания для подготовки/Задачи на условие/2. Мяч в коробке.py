def ball_in_box():
    cube_V = 35 * 28 * 30
    ball_radius = float(input('Введите радиус шара: '))
    ball_V = 4/3 * 3.14 * ball_radius ** 2
    if cube_V > ball_V:
        print('Мяч поместится в отсек')
    else:
        print('Мяч не поместится в отсек')

ball_in_box()