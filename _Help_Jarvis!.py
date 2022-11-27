for _ in range(int(input())):
    n = int(input())
    if n==0:
        print("YES")
    else:
        arr = []
        while n>0:
            arr.append(n%10)
            n//=10
        c = 0
        arr.sort()
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]==1:
                c=1
            else:
                c=0
                break
        if c==1:
            print("YES")
        else:
            print("NO")