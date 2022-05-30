n = input()
m = n.split(" ")
for i in range(0,len(m)):
    mi=ord(min(m[i]))
    ma=ord(max(m[i]))
    print(abs(mi-ma),end=" ")