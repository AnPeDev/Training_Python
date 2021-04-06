# Открывает файл для записи (удаляет все что было или создает файл)
with open('new_file.txt', 'w') as file:
    file.write('Hello world')

# Добавляет в конец файла (\n с новой строки)
with open('new_file.txt', 'a') as file:
    file.write('\nIndiapolis')

# Выводит файл для чтения
with open('new_file.txt', 'r') as file:
    print(file.read())
