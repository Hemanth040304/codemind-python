s = input().lower()
s = s.replace(" ","")
s = set(s)
s = list(s)
s.sort()
for i in s:
    print(i,end='')