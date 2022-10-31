# 1. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента. Use comprehension.
# Пример:
# in # 9# out [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]
# # in 10 out [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]

import random

list = []
a = int(input("Введите количество элементов: "))
for i in range(a):
    list.append(random.randint(1, 20))

result_list = []
# list = [int(i) for i in input("Введите список чисел: ").split()]
for i in range(1, len(list)):
    if list[i] > list[i - 1]:
        (result_list.append(list[i]))
print("Исходный список: ", list)

print("Результирующий список: ", result_list)
