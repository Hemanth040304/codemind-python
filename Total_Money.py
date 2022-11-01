t=int(input())
for i in range(t):
    D,d,P,Q=map(int,input().split())
    n=D//d
    q=D%d
    s=0
    for i in range(n):
        s+=(P+(Q)*i)*d
    s+=(P+Q*n)*q
    print(s)