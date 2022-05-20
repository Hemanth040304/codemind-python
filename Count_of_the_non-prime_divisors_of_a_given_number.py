def is_prime(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return 0
    return 1

n = int(input())
c = 2
for i in range(2,(n//2)+1):
    if n%i==0:
        if is_prime(i):
            i+=1
            continue
        else:
            c+=1
print(c)