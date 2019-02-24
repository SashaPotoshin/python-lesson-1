#сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.

num = int(input("Введите число: "))
reverse = 0

while num > 0:
    n = num % 10
    num = num // 10
    reverse = reverse*10
    reverse = reverse + n
print(reverse)
