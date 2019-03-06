#В одномерном массиве целых чисел определить два наименьших элемента.
#Они могут быть равны между собой, так и различаться.

import random

s = 10
MAX_LIMIT = 100
MIN_LIMIT = 0

a = [random.randint(MIN_LIMIT, MAX_LIMIT) for i in range(s)]
print(a)

first_min_number = second_min_number = float('inf')
for i in range(0, s):
    if a[i] < first_min_number:
        second_min_number = first_min_number
        first_min_number = a[i]
    elif a[i] < second_min_number and a[i] != first_min_number:
        second_min_number = a[i]
if (second_min_number == float('inf')):
    print("Нет второго наименьшего элемента")
else:
    print("Первое минимальное число: ", first_min_number, "второе минимальное число: ", second_min_number)


