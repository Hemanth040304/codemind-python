n = int(input())
while n:
    n-=1
    x = int(input())
    a=1
    c=0
    while a*a<=x:
        if a*a==x:
            c=1
        else:
            c=0
        a+=1
    if c==1:
        print(True)
    else:
        print(False)