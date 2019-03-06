#Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия..
# Программа должна определить среднюю прибыль (за год для всех предприятий) и
#  вывести наименования предприятий, чья прибыль выше среднего и отдельно
#  вывести наименования предприятий, чья прибыль ниже среднего.

companies = {}
n = int(input("введите количество предприятий: "))

s = 0
for i in range(n):
    sname = input(str(i+1) + "ое" if (i+1)//3 == 0 else str(i+1) + "ье")
    salesQ1 = int(input("Q1:"))
    salesQ2 = int(input("Q2:"))
    salesQ3 = int(input("Q3:"))
    salesQ4 = int(input("Q4:"))
    average = (salesQ4 + salesQ2 + salesQ3 + salesQ1) / 4
    companies[sname] = average
    s += average
avrg = s/n
print("Средняя прибыль:", avrg)
for i in companies:
    if companies[i] > avrg:
        print("Компания c прибылью выше среднего: ", i)
for i in companies:
    if companies[i] < avrg:
        print("Компания c прибылью ниже среднего: ", i)


