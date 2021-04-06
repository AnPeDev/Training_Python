contacts = {
    'Andrei': '+7345345345345',
    'Valera': '+7234234234424',
    'Ira': '+7423424124452'
}

name = input('Enter name: ')

print(contacts.get(name, 'No name'))

# if name in contacts:
#     print(name, contacts[name])
# else:
#     print('No name')    