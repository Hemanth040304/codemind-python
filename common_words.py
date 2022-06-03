a = input()
b = input()
a , b = a.lower() , b.lower()
a , b = a.split(" ") , b.split(" ")
for i in range(0,len(b)):
    if b[i] in a:
        print(b[i],end=" ")