for i in range(int(input())):
    a,b = map(int,input().split())
    while a!=b:
        if a>b:
            a-=b
        if b>a:
            b-=a
    if a==1 and b==1:
        print("YES")
    else:
        print("NO")