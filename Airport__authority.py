n = int(input())
b = []
for i in range(0,n):
    a = int(input())
    b.append(a)
c = int(input())
d = 0
for i in range(0,len(b)):
    if b[i]>c:
        d+=2
    else:
        d+=1
print(d)