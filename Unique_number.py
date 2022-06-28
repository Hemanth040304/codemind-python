n = int(input())
on,tw,th,fo,fi,si,se,ei,ni=0,0,0,0,0,0,0,0,0
while n:
    if n%10==1:
        on+=1
    elif n%10==2:
        tw+=1
    elif n%10==3:
        th+=1
    elif n%10==4:
        fo+=1
    elif n%10==5:
        fi+=1
    elif n%10==6:
        si+=1
    elif n%10==7:
        se+=1
    elif n%10==8:
        ei+=1
    elif n%10==9:
        ni+=1
    n//=10
if on<2 and tw<2 and th<2 and fo<2 and fi<2 and si<2 and se<2 and ei<2 and ni<2:
    print("Unique Number")
else:
    print("Not Unique Number")