for _ in range(int(input())):
    a,b = map(int,input().split())
    c = 0
    for i in range(0,b):
        if i*i%b==a:
            c = 1
            print(i)
            break
    if c==0:
        print(-1)