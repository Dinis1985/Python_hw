# 3. Задайте список из n чисел, заполненный по формуле
# (1 + 1/n) ** n и выведите на экран их сумму.
# Например:
# Для n = 6: [2, 2, 2, 2, 2, 3] -> 13

n = int(input('Введите число N: '))


def calc(n):
    return round((1 + (1 / n)) ** n)


step = []
for i in range(1, n + 1):
    step.append(calc(i))
if step:
    print(f"Сумма значений  {step} -> {sum(step)}")
else:
    print('Сумма значений -> 0')