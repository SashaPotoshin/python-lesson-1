#Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
print ("введите три числа")

a= int(input("первое число: "))
b= int(input("второе число: "))
c= int(input("третье число: "))

if a<b and b<c or b>c and b>a:
    print (b)
elif a>b and c>a or c<a and b>c:
    print (a)
else:
    print (c)
