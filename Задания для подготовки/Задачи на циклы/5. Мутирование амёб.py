ameba = 1
hours = 0

while hours < 24:
    hours += 3
    ameba *= 2
    print(f'Через {hours} часа будет {ameba} амёб.')
    hours += 3
    ameba *= 4
    print(f'Через {hours} часа будет {ameba} амёб.')