dohod = float(input())
raskhod = float(input())
if dohod>raskhod:
    rent = dohod/(dohod - raskhod)
    k = int(input("Введите численность сотрудников"))
    print((dohod-raskhod)/k)