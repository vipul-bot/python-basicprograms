s=list(input())
c=s.count(s[0])-1
S=''
for i in range(len(s)):
    if i==0:
        continue
    else:
        if s[i]==s[0]:
            s[i]='$'
for j in range(len(s)):
    S+=s[j]
    
print(S)
