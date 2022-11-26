for _ in range(int(input())):
    a,b = map(int,input().split())
    c = a**b
    c = str(c)
    print(c[len(c)-1])