n = int(input())
arr = list(map(int,input().split()))
x,y,c =0,0,0
for i in range(n):
    c1,c2=0,0
    for j in range(i,n):
        if arr[j]==0:
            c1+=1
        if arr[j]==1:
            c2+=1
        if c1==c2 and c<j-i:
            c=j-i
            x,y=i,j
if c==0:
    print(-1)
else:
    print(x,y)
