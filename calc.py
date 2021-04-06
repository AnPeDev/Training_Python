# Сложение, вычитание, и перевод в exe с помощью модуля pyistaller

# Чтобы скомпилировать в ехе: pyistaller calc.py

from colorama import init
from colorama import Fore, Back, Style
init()

# Тест становится красный
print(Fore.RED)

what = input('Что делаем? (+, -): ')

a = float(input('Введи первое число: '))
b = float(input('Введи второе число: '))

if what == '+':
    c = a + b
    print('Результат: ' + str(c))
elif what == '-':
    c = a - b
    print('Результат: ' + str(c))
else:
    print('Что это такое?')

input()
