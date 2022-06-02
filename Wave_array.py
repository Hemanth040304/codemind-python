x = int(input())
l = list(map(int,input().split()))
c=0
if l[0]<l[1]:
    for i in range(1,x-1,2):
        if (l[i-1]<l[i] and l[i]>l[i-1]):
            c+=1
        else:
            print('no')
            c=0
            break
    if c!=0:
        print("yes")
else:
    for i in range(1,x-1,2):
        if (l[i-1]>l[i] and l[i]<l[i-1]):
            c+=1
        else:
            print('no')
            c=0
            break
    if c!=0:
        print("yes")