# Напишите программу, удаляющую из текста все слова, содержащие "абв".
# В тексте используется разделитель пробел.
# Пример:
# in  Number of words: 10# out # авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба
# in Number of words: 6 out  ваб вба абв ваб бва абв
# ваб вба ваб бва
# in Number of words: -1
# out The data is incorrect

import random

text = "абв"
num_word = (int(input("Number of words: ")))
listWord = []
for x in range(num_word):
    random_text = random.sample(text, 3)
    listWord.append("".join(random_text))

print(" ".join(listWord))

listWord2 = list(filter(lambda x: text not in x, listWord))
print(" ".join(listWord2))
