a=int(input())
arr=list(map(int,input().split()))
m=-1000
s=0
for k in range(a):
    ft=arr[0]
    arr[0]=arr[a-1]
    for  i in range(1,a):
        t=arr[i]
        arr[i]=ft
        ft=t
    for i in range(a):
        s=0
        for j in range(i,a):
            s+=arr[j]
            if m<s:
                m=s
print(m)