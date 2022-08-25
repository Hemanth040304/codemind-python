s = input()
if s[6]=='A':
    if s[0]=='1' and s[1]=='2':
        print("00"+s[2]+s[3]+s[4])
    else:
        print(s[0]+s[1]+s[2]+s[3]+s[4])
else:
    if s[0]=='1' and s[1]=='2':
        print(s[0]+s[1]+s[2]+s[3]+s[4])
    else:
        a=int(s[0])+1
        b=int(s[1])+2
        a=str(a)
        b=str(b)
        print(a+b+s[2]+s[3]+s[4])