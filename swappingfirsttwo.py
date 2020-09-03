s1,s2=input().split()
s1,s2=list(s1),list(s2)
(s1[0],s2[0])=(s2[0],s1[0])
(s2[1],s1[1])=(s1[1],s2[1])
S1,S2='',''
for i in range(len(s1)):
    S1+=s1[i]
for j in range(len(s2)):
    S2+=s2[j]
print(S1,S2)    
