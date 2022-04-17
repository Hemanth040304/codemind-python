n = int(input())
while n:
    n-=1
    x = int(input())
    temp=x
    rev=0
    while temp:
        rev=rev*10+temp%10
        temp//=10
    if rev==x:
        print(True)
    else:
        print(False)