a = int(input())
b = int(input())
i = 1
while a<=b:
    a*=1.1
    i+=1
    print(a)
print('на {} день спортсмен достиг результата - не менее {} км'.format(i,b))


