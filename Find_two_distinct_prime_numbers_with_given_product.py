def prime(n):
    if n==1:
        return 0
    else:
        c = 0
        for _ in range(2,n//2):
            if n%_==0:
                c+=1
        if c == 0:
            return 1
        else:
            return 0

n = int(input())
k = 0
for i in range(2,n//2+1):
    if prime(i) and prime(n//i) and n%i==0 and n%(n//i)==0:
        print(i,n//i)
        k+=1
        break
if k==0:
    print(-1)