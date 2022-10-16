# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". 
# В тексте используется разделитель пробел.

from random import choices

def name(a, b):
    name = []
    for i in range(a):
        y = choices(b, k=3)
        name.append(''.join(y))
    return name

my_list = name(int(input('Введите количество элементов > ')), 'абв')
s = ' '.join(my_list)
print(s, s.replace('абв ', ''), sep='\n')
