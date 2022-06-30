s = input().lower()
s = s.split(' ')
for i in range(len(s)):
    d = 0
    for j in s[i]:
        if j in 'aeiou':
            d+=1
    print(d,end=" ")