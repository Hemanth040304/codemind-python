n = int(input())
sq_n = n*n
sum=0
while sq_n:
    sum+=sq_n%10
    sq_n//=10
if sum==n:
    print("Neon Number")
else:
    print("Not Neon Number")