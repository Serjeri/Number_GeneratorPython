#Генератор Гос Номеров в Питере
# Саня есть еще один способ, подумай как улучшить код.
import random

number = random.randrange(1, 10)
letters = ['А', 'В', 'Е', 'К', 'М', 'Н', 'О', 'Р', 'С', 'Т', 'У', 'Х']
region = 178

hig = len(letters)

for i in range(1):
    a = random.randrange(hig)
    b = random.randrange(hig)
    c = random.randrange(hig)

    if 100 > number and number > 10:
        print(letters[a], '0', number, letters[b], letters[c], region, sep='')
    if 10 > number:
        print(letters[a], '00', number, letters[b], letters[c], region, sep='')

    else:
        if number > 100:
            print(letters[a], number, letters[b], letters[c], region, sep='')