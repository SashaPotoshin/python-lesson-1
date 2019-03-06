#В массиве найти максимальный отрицительный элемент.
#вывести на экран его значение и позицию в массиве.
from random import random

a = []

for i in range(20):
    n = int(random() * 11) - 5
    print(n, end=', ')
    if n < 0:
        a.append(n)
max_number = a[0]
pos = 0
for m in range(len(a)):
    if a[m] > max_number:
        max_number = a[m]
        pos = m
print()
print(a)
print(max_number)
print(pos)


