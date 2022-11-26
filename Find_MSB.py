for _ in range(int(input())):
    n = int(input())
    s = 2
    p = 1
    while p<n:
        if p*2>n:
            break
        p*=s
    print(p)