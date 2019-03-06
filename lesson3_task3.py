#определить, какое число в массиве встречается чаще всего

import random
s = 10
MAX_LIMIT = 100
MIN_LIMIT = 0

a = [random.randint(MIN_LIMIT, MAX_LIMIT) for i in range(s)]
print(a)

num = a[0]
max_frq = 1
for i in range(s - 1):
    frq = 1
    for k in range(i + 1, s):
        if a[i] == a[k]:
            frq += 1
    if frq > max_frq:
        max_frq = frq
        num = a[i]

if max_frq > 1:
    print("Повторов: ", max_frq, "число: ", num)
else:
    print('нет одинаковых')
