#найти сумму n-элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125
#Количество элементов n выводится с клавиатуры

n = int(input("введите количество элементов ряда"))
a = 1
s = 0
i = 0

for i in range(n):
    s += a
    a = a / - 2
    i += 1

print(s)
