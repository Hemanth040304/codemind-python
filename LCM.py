a, b = map(int, input().split())
i=1
while 1:
    if (a*i)%b==0:
        print(a*i)
        break
    i+=1