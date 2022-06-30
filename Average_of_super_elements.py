n = int(input())
arr = list(map(int,input().split()))
c = 0
s = 0
for i in set(arr):
    if arr.count(i)==i:
        c+=1
        s+=i
if c==0:
    print("-1")
else:
    su=s/c
    print("%.2f"%su)