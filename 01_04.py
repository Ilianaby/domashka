"""Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции."""

num1 = int(input("Введите целое положительное число: "))

num = num1
max_num = 0
while num > 0:
    max_num = max(max_num, num % 10)
    num //= 10
print(max_num)


num = num1
result = []
while num > 0:
    result.append(num % 10)
    num //= 10
print(max(result))
