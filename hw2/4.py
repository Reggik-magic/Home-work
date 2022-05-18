l = [i for i in input().split()]
for i in l:
    if len(i)<=10:
        print(i)
    else:
        print(i[:10])