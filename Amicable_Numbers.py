a = int(input())
b = int(input())
x = 1
sum = 0
while x<=a//2:
    if a%x==0:
        sum+=x
    x+=1
if sum==b:
    print("Amicable")
else:
    print("Not Amicable")