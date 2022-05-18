l = ['winter', 'spring', 'summer', 'autumn']
d = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}
month = int(input("Введите месяц по номеру "))
if month ==1 or month == 12 or month == 2:
        print(d.get(1))
        print(l[0])
elif month == 3 or month == 4 or month ==5:
    print(d.get(2))
    print(l[1])
elif month == 6 or month == 7 or month == 8:
    print(d.get(3))
    print(l[2])

elif month == 9 or month == 10 or month == 11:
    print(d.get(4))
    print(l[3])
else:
        print("Такого месяца не существует")