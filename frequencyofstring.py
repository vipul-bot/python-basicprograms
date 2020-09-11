s=input()
m=0;l=[];n=0;j=()
for i in range(len(s)):
    if i>0:
        if s[i] in s[0:i]:
            continue
    m=s.count(s[i],i,len(s))
    n=s[i]
    j=(n,m)
    l.append(j)
for k in l:
    print(*k)
    
