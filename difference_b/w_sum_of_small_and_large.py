mi = 0
ma = 0
n = input()
m = n.split(" ")
for i in range(len(m)):
    mi+=ord(min(m[i]))
    ma+=ord(max(m[i]))
print(abs(mi-ma))