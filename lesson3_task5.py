#сумма элементов между минимальным и максимальным элементами массива

import random

s = 10
MAX_LIMIT = 100
MIN_LIMIT = 0
inbetween = 0
a = [random.randint(MIN_LIMIT, MAX_LIMIT) for i in range(s)]
print(a)

min_id = 0
max_id = 0
for i in range(1, s):
    if a[i] < a[min_id]:
        min_id = i
    elif a[i] > a[max_id]:
        max_id = i
print(a[min_id], a[max_id])

if min_id > max_id:
    min_id, max_id = max_id, min_id


for i in range(min_id+1, max_id):
    inbetween += a[i]
print(inbetween)
