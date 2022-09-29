n = int(input())
p = []
h = []
for i in range(0,n):
    a = int(input())
    p.append(a)
for i in range(0,n):
    a = int(input())
    h.append(a)
count = 0 
for i in range(0,n):
    c = 1
    for j in range(0,n):
        if p[i]<=h[j]:
            h[j]=0
            c=0
            break
    if c!=0:
        count+=1
print(count)