a = int(input())
b = int(input())
while a<=b:
    temp = a
    di = 0
    d = 0
    while temp:
        d += 1
        if temp%10!=0 and a%(temp%10)==0:
            di += 1
        temp//=10
    if di==d:
        print(a,end=" ")
    a += 1