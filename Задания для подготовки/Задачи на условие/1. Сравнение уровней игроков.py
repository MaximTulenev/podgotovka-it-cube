import random

def comparison():
    lvl_1 = random.randint(1, 100)
    lvl_2 = random.randint(1, 100)
    print('Сравниваем...')
    if lvl_1 < lvl_2 or lvl_1 > lvl_2:
        print('Уровни игроков не равны')
    else:
        print('Уровни игроков равны')

comparison()