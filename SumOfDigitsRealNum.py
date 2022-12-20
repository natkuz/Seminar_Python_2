#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Пример:
# 6782 -> 23
# 0,56 -> 11

from decimal import Decimal

number = Decimal(input('Enter real number: '))
sum = 0

if number - int(number) == 0:
    while number != 0:
        sum = sum + int(number) % 10
        number = int(number / 10)
else:
    number = str(number)
    array = number.split('.')
    for i in array[0]:
        sum = sum + int(array[0]) % 10
        array[0] = int(int(array[0]) / 10)
    for i in array[1]:
        sum = sum + int(array[1]) % 10
        array[1] = int(int(array[1]) / 10)

print(f'The sum of digits of the real number {number} = {sum}')