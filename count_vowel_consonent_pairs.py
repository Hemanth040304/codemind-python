v = 'aeiouAEIOU'
c = 'qwrtypsdfghjklzmxncbvQWRTYPSDFGHJKLZMXNCBV'
s = input()
count=0
l = len(s)-1
f=0
while f<l:
    if (((s[f] in v) and (s[l] in c)) or ((s[f] in c) and (s[l] in v))):
        count+=1
    f+=1
    l-=1
print(count)