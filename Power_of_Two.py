n = int(input())
i = 2
while 2**i<=n:
    if 2**i==n:
        print(True)
        break
    i+=1
else:
    print(False)