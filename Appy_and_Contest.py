for i in range(int(input())):
    n,a,b,k = map(int,input().split())
    c = 0
    if a%b==0:
        c = a
    elif b%a==0:
        c = b
    else:
        c = a*b
    d,e,f = n/c,n/a,n/b
    e-=d
    f-=d
    if e+f>=k:
        print("Win")
    else:
        print("Lose")