n = input()
m = n.split(" ")
for i in range(0,len(m)):
    print(min(m[i]),max(m[i]),end=" ")