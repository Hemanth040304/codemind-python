n = int(input())
while n:
    n-=1
    x = int(input())
    sum = 1
    while x!=1:
        sum*=x
        x-=1
    print(sum)
    sum=0