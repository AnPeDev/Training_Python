#  join, replace, startswith, endswith, lower, upper, split
#  min, max, abs, sum

fruits = ['Lemons', 'Apples', 'Kiwi', 'Pineapple', 'Strawberry']
members = 'James,Jonny,Jessie,Jack,John'
digits = [2, -3, -67, 45, 36, 136]

print(fruits)
print(' | '.join(fruits))

print('Hello, Andrei!'.replace('Andrei', 'Apple'))  # Заменяет слово

name = 'Andrei'
if name.lower().startswith('a'):  # Если начинается с буквы А и переводит слово в нижний регистр
    print('Yes')
else:
    print('No')

#  upper - переводит слово в верхний регистр

print(members.split(','))  # Переводит сроку в список

print(min(digits))  # min
print(max(digits))  # max
print(abs(-12345))  # переводит в положительное число
print(sum(digits))  # считает сумму
