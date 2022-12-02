n = int(input())
s = input()
f = s.find("HH")
if f == -1:
    print("YES")
    print(s.replace(".","B"))
else:
    print("NO")