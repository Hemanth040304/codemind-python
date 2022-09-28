test = int(input())
while test>0:
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    s = 0
    c = 0 
    for i in range(0,n):
        s = 0
        for j in range(i,n):
            s += arr[j]
            if s==k:
                print(i+1,j+1)
                break
        if s==k:
            c+=1
            break
    if c==0:
        print("-1")
    test-=1