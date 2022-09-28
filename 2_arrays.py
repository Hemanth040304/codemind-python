n = int(input())
arr = list(map(int,input().split()))
brr = list(map(int,input().split()))
c,count,s2,s1 = 0,0,0,0
for i in range(0,n):
    if arr[i]==-1:
        c+=1
    else:
        s1+=arr[i]
    if brr[i]==-1:
        c+=1
    else:
        s2+=brr[i]
if c==2:
    print("Infinite")
else:
    for i in range(0,100000):
        if i+s1 == s2:
            count+=1
    print(count)