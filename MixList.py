# Реализуйте алгоритм перемешивания списка. 
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для получения случайного int

import random

n = int(input('Enter number of list elements: '))

list_for_shuffling = []
shuffled_list = []

for i in range(n):
    list_for_shuffling.append(i)

print(f'List for shuffling: {list_for_shuffling}')

for j in range(n):
    temp = list_for_shuffling[random.randrange(len(list_for_shuffling))]
    shuffled_list.append(temp)
    list_for_shuffling.remove(temp)
    
print(f'List after shuffling: {shuffled_list}')

