n = int(input())
f,s = 0,1
print(f,s,end=" ")
while n-2:
    ne = f+s
    print(ne,end=" ")
    f=s
    s=ne
    n -= 1