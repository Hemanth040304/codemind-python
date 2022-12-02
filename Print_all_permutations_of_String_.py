def fun(s,a):
    if len(s)==0:
        print(a)
    for i in range(len(s)):
        c = s[i]
        l = s[0:i]
        r = s[i+1:]
        rest = l+r
        fun(rest,a+c)

s = input()
a = ''
fun(s,a)