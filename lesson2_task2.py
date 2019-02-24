#Посчитать четные и нечетные цифры введенного числа

even_sum = 0
odd_sum = 0

while num > 0:
    if num % 2 == 0:
        even_sum += 1
    else:
        odd_sum += 1
    num = num // 10

print("четных цифр: ", even_sum, "нечетных цифр: ", odd_sum)
