# 2 Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.
# Пример:
# in # 100# out [20, 21, 40, 42, 60, 63, 80, 84, 100]
#  in 424# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100, 105, 120, 126, 140, 147, 160,
# 168, 180, 189, 200, 210, 220, 231, 240, 252, 260,
# 273, 280, 294, 300, 315, 320, 336, 340, 357, 360, 378, 380, 399, 400, 420]

a = int(input("Введите число, предел расчета: "))
num = range(20, a + 1)
list = [element for element in num if element % 20 == 0 or element % 21 == 0]
print(list)
