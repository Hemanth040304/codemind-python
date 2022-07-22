s = input().lower()
a = ''
for i in set(s):
    if s.count(i)==1:
        a+=i
a = list(a)
a.sort()
a = str(a)
a=a.replace(" ","")
a=a.replace("'","")
a=a.replace("[","")
a=a.replace("]","")
a=a.replace(" ","")
a=a.replace(",","")
print(a)