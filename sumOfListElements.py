# Задайте список из n чисел последовательности (1 + 1/n)**n, выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n = 4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

n = int(input('Enter integer number: '))
array = []

for i in range(1, n + 1):
    num = round((1 + 1 / i) ** i, 2)
    array.append(num)
    
print(f'List of n sequence numbers is {array}')

sum = 0

for j in array:
    sum += j

print(f'The sum of the elements of a sequence list = {sum}')
