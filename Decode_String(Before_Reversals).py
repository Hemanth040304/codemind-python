for _ in range(int(input())):
    a,b = map(int,input().split())
    s = input()
    while b>0:
        s1 = s[:b]
        s = s1[::-1]+s[b:]
        b-=1
    print(s)