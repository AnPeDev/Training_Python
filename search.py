'''Поиск наименьшего и сортировка выбором'''


def findSmallest(arr):
    '''Поиск наименьшего значения'''
    smallest = arr[0]  # Для хранения наименьшего значения
    smallest_index = 0  # Для хранения индекса наименьшего значения
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


print(findSmallest([5, 3, 6, 2, 10]))


def selectionSort(arr):
    '''Сортировка выбором. Находит наименьший в массиве и добавляет его в новый список'''
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


print(selectionSort([5, 3, 6, 2, 10]))
