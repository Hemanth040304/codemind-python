n = input()
c = 999999999999
n = n.split(" ")
c_=0
for j in n:
    count = 0
    a = j
    for i in a:
        if i in 'aeiou':
            count += 1
    if c>count:
        c=count
for j in n:
    count = 0
    a = j
    for i in a:
        if i in 'aeiou':
            count += 1
    if c==count:
        c_ += 1
print(c_)