for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    if n==1:
        print(0)
    else:
        w = []
        for i in arr:
            if i in range(1,1000000000,2):
                w.append(i)
        if len(w)==1:
            print(0)
        elif len(w)%2==0:
            print(int(len(w)//2))
        else:
            print(int(len(w)-1)//2)