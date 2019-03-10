# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
#  Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# вариант со списком.
#Размер списка вне зависимости от реализации(вариант 1 и вариант 3) получился 68.
#Вариант 2 - без списка, тип переменной - целое число, size = 14

import sys

# вариант 1
print("вариант 1")
arr = [0] * 9
for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            arr[j - 2] += 1
i = 0
while i < len(arr):
    # print("Числу", i + 2, "кратно", arr[i])
    i += 1

# вариант 2
# print('вариант2')
START_NUM = 2
END_NUM = 99
START_DIV = 2
END_DIV = 9

for i in range(START_DIV, END_DIV + 1):
    frequency = 0
    for j in range(START_NUM, END_NUM + 1):
        if j % i == 0:
            frequency += 1
    # print(f' Числу {i} кратно {frequency} чисел')

# вариант 3
# print('вариант3')
frequency1 = [0] * (END_DIV - START_DIV + 1)
for i in range(START_NUM, END_NUM + 1):
    for j in range(START_DIV, END_DIV + 1):
        if i % j == 0:
            frequency1[j - START_DIV] += 1
for i, item in enumerate(frequency1, start=START_DIV):
    print(f' Числу {i} кратно {item} чисел')

def show_size (x, level = 0):
    print('\t' * level, f'type= {type(x)}, size = {sys.getsizeof(x)}, obj= {x}')
    if hasattr(x, '__iter__'):
        for item in x:
            show_size(item, level+1)

print('Вариант1: ')
show_size(arr)
print('Вариант2: ')
show_size(frequency)
print(print('Вариант3: '))
show_size(frequency1)



#Версия Python 3.7.1 32 разрядная система [MSC v.1915 32 bit (Intel)] on win32

# Вывод - Вариант1:
#  type= <class 'list'>, size = 68, obj= [49, 33, 24, 19, 16, 14, 12, 11]
#  type= <class 'int'>, size = 14, obj= 49
#  type= <class 'int'>, size = 14, obj= 33
#  type= <class 'int'>, size = 14, obj= 24
#  type= <class 'int'>, size = 14, obj= 19
#  type= <class 'int'>, size = 14, obj= 16
#  type= <class 'int'>, size = 14, obj= 14
#  type= <class 'int'>, size = 14, obj= 12
#  type= <class 'int'>, size = 14, obj= 11
# Вариант2:
#  type= <class 'int'>, size = 14, obj= 11
# Вариант3:
# None
#  type= <class 'list'>, size = 68, obj= [49, 33, 24, 19, 16, 14, 12, 11]
#  type= <class 'int'>, size = 14, obj= 49
#  type= <class 'int'>, size = 14, obj= 33
#  type= <class 'int'>, size = 14, obj= 24
#  type= <class 'int'>, size = 14, obj= 19
#  type= <class 'int'>, size = 14, obj= 16
#  type= <class 'int'>, size = 14, obj= 14
#  type= <class 'int'>, size = 14, obj= 12
#  type= <class 'int'>, size = 14, obj= 11