import math
def is_prime(n):
    if n==1: return 0
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return 0
    return 1
    
A,B,C,D = map(int,input().split())
for i in range(A,B+1):
    flag = True
    for j in range(C,D+1):
        if is_prime(i+j):
            flag = False
            break
    if flag:
        exit(print("Takahashi"))
print("Aoki")
