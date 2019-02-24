#Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
#  Вывести на экран это число и сумму его цифр.
num= int(input("введите число:"))
max_s=0 #max summary of components
max_n=0 #maximal number

while num != 0:
    s = 0     #summary of components
    n = num
    while num > 0:
        s += num % 10
        num //= 10
    if s > max_s:
        max_s = s
        max_n = n
    elif s == max_s:
        print("существует несколько чисел с одинаковой наибольшей суммой цифр" ,max_s)
    num= int(input("введите число:"))
print ("максимальное число: ", max_n, "c cуммой цифр: ", max_s)


