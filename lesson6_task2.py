# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
#  Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# вариант со словарем. словарь содержит и ключи и значения
# из-за 32 разрядной системы тратит меньше памяти на ячейку, чем 64.


import random
import sys

SIZE = 10
MIN_ITEM = 0
array = [random.randint(MIN_ITEM, SIZE // 1.5) for _ in range(SIZE)]
print(array)

num = array[0]
frequency = 1
for i in range(len(array)):
    spam = 1
    for j in range(i+1, len(array)):
        if array[i] == array[j]:
            spam += 1
    if spam > frequency:
        frequency = spam
        num = array[i]
if frequency > 1:
    print(num, "встречается", frequency)
else:
    print('все элементы уникальны')

counter = {}
frequency2 = 1
num2 = None
for item in array:
    if item in counter:
        counter[item] += 1
    else:
        counter[item] = 1
    if counter[item] > frequency2:
        frequency2 = counter[item]
        num2 = item

if num2 is not None:
    print(num2, "встречается", frequency2)
else:
    print('все элементы уникальны')

def show_size(x: object, level: object = 0) -> object:
    print('\t' * level, f'type = {type(x)}, size = {sys.getsizeof(x)}, obj = {x} ')
    if hasattr(x, '__iter__'):
        if hasattr(x,'items'):
            for key, value in x.items():
                show_size(key, level + 1)
                show_size(value, level + 1)
        elif not isinstance(x, str):
            for item in x:
                show_size(item)
show_size(frequency)
show_size(frequency2)
show_size(counter)

# [6, 5, 2, 4, 1, 6, 0, 1, 2, 1]
# 1 встречается 3
# 1 встречается 3
#  type = <class 'int'>, size = 14, obj = 3
#  type = <class 'int'>, size = 14, obj = 3
#  type = <class 'dict'>, size = 204, obj = {6: 2, 5: 1, 2: 2, 4: 1, 1: 3, 0: 1}
# 	 type = <class 'int'>, size = 14, obj = 6
# 	 type = <class 'int'>, size = 14, obj = 2
# 	 type = <class 'int'>, size = 14, obj = 5
# 	 type = <class 'int'>, size = 14, obj = 1
# 	 type = <class 'int'>, size = 14, obj = 2
# 	 type = <class 'int'>, size = 14, obj = 2
# 	 type = <class 'int'>, size = 14, obj = 4
# 	 type = <class 'int'>, size = 14, obj = 1
# 	 type = <class 'int'>, size = 14, obj = 1
# 	 type = <class 'int'>, size = 14, obj = 3
# 	 type = <class 'int'>, size = 12, obj = 0
# 	 type = <class 'int'>, size = 14, obj = 1