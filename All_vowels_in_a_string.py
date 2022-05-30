a = "AEIOU"
b = "aeiou"
u = 0
l = 0
u_c = []
l_d = []
n = input()
#print(n)
for i in range(0,len(n)-1):
    if n[i] in a:
        if n[i] not in u_c:
            u_c.append(n[i])
            u+=1
    if n[i] in b:
        if n[i] not in l_d:
            l_d.append(n[i])
            l+=1
if u==5 or l==5:
    print(True)
else:
    print(False)