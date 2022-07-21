s = input().split(" ")
c = 0
vo = "aeiouAEIOU"
for i in s:
    if i[0] in vo and i[-1] not in vo:
        c+=1
print(c)