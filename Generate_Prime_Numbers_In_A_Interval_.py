a = int(input())
b = int(input())
while a<=b:
    c = 0
    x = 1
    while x<=a//2:
        if a%x==0:
            c+=1
        x+=1
    if c==1:
        print(a)
    a+=1