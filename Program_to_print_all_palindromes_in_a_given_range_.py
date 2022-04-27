a = int(input())
b = int(input())
rev = 0
while a<=b:
    temp = a
    rev = 0
    while temp:
        rev=rev*10+temp%10
        temp//=10
    if rev==a:
        print(a,end=" ")
    a+=1