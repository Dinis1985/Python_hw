# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Например:
# in 4 out [2, 5, 8, 10]
# [20, 40]
# in 5 out [2, 2, 4, 8, 8]
# [16, 16, 4]

import random

nums = []
a = int(input("Введите число: "))
for i in range(a):
    nums.append(random.randint(1, 10))
print(f"Cписок: {nums}")
sumNum = 0
len_list = 0
if len(nums) % 2 == 0:
    len_list = len(nums) // 2
    for i in range(len_list):
        print(nums[i] * nums[len(nums) - 1 - i], end=" ")

else:
    len_list = len(nums) // 2
    for i in range(len_list):
        print(nums[i] * nums[len(nums) - 1 - i], end=" ")

    print((nums[len(nums) // 2]))
