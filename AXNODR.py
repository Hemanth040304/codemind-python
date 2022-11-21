for i in range(int(input())):
    n = int(input())
    if (n-0)%4==0:
        print(n+3)
    elif (n-1)%4==0:
        print(n)
    elif (n-2)%4==0 or (n-3)%4==0:
        print(3)
