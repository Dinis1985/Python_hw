# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# Например:
# in 5 out [10, 2, 3, 8, 9] 22
# in 4 out [4, 2, 4, 9]  8

import random

nums = []
a = int(input("Введите количество чмсел: "))
for i in range(a):
    nums.append(random.randint(1, 20))
print(f"Cписок: {nums}")
sumNum = 0

for i in range(0, len(nums), 2):
    sumNum += nums[i]
print(f'Сумма элементов списка, стоящих на нечетных позициях: {sumNum}')
