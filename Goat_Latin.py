def fun(s):
    w = s.split()
    v = set("AEIOUaeiou")
    for i in range(len(w)):
        if w[i][0] in v:
            w[i] = w[i]+"ma"+"a"*(i+1)
        else:
            w[i] = w[i][1:]+w[i][0]+"ma"+"a"*(i+1)
    return " ".join(w)

s = input()
print(fun(s))