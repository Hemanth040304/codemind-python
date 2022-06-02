n = input()
c = 999999999999
n = n.split(" ")
for j in n:
    count = 0
    a = j
    for i in a:
        if i in 'aeiou':
            count += 1
    if c>count:
        c=count
print(c)