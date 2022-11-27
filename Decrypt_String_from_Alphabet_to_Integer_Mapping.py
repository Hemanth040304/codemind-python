s=input()
i,j,i1=0,0,0
for i in range(len(s)):
    val=0
    if (s[i]=='#'):
        for j in range(i1,i-2):
            print(chr(ord(s[j])-48+96),end="")
        val=(ord(s[i-2])-48)*10+ord(s[i-1])-48+96
        print(chr(val),end="")
        i1=i+1
    if i==len(s)-1:
        for j in range(i1,len(s)):
            val=ord(s[j])-48+96
            print(chr(val),end="")
        break