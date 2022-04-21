n = int(input())
e=0
o=0
d=0
while n:
    if(n%10)%2==0:
        e+=1
    elif (n%10)%2:
        o+=1
    d+=1
    n//=10
if d==e:
    print("Even")
elif d==o:
    print("Odd")
else:
    print("Mixed")