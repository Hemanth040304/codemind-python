for _ in range(int(input())):
    n,m = map(int,input().split())
    c=0
    for i in range(n):
        s=input()
        arr=[]
        for j in s:
            if j=='P' or j=='T':
                arr.append(j)
        for j in range(n):
            if arr[j]=='P':
                for k in range(n):
                    if arr[k]=='T':
                        if abs(j-k)<=m:
                            c+=1
                            arr[k]='0'
                            break
                continue
    print(c)