a = input()
a,b = a.split()
k = []
for i in b:
    k.append(i)
f=0 
for i in a:
    if i in k:
        f = 1
        k.remove(i)
    else:
        f = 0
        break
if  f==1:
    print(True)
else:
    print(False)