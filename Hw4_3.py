# 3. Задайте последовательность чисел. Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности в том же порядке.
# Пример:
# in 7 out [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]
# in -1 out Negative value of the number of numbers! []
#  in 10 out [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]

spisok = list(map(int, input('Введите числа списка через пробел: ').split()))
print(f'Список: {spisok}')

newSpisok = []
for i in range(len(spisok)):
    for j in range(len(spisok)):
        if i != j and spisok[i] == spisok[j]:
            break
    else:
        newSpisok.append(spisok[i])
print(f'Cписок неповторяющихся элементов {newSpisok}')
