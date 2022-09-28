n = int(input())
w = 0 
r = 2
for i in range(0,n):
    x = w
    w = r
    r += x
print(w)