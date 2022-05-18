n = int(input())
maxi = 0
s = str(n)
i = 0
while i<len(s):
    if int(s[i])>maxi:
        maxi = int(s[i])
    i+=1
print(maxi)