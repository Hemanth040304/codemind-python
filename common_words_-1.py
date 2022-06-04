a = input()
b = input()
a , b = a.lower() , b.lower()
a , b = a.split(" ") , b.split(" ")
c = 0
for i in range(0,len(a)):
    if a[i] in b:
        c += 1
print(c)