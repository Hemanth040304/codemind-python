n = input()
i = 0
x = len(n)
while x:
    x-=1
    if int(n[i])%2:
        print(int(n[i])**2,end='')
    i+=1