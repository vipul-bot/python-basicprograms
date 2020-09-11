s=input()
j=s.find('not',0,len(s))
k=s.find('poor',0,len(s))
t=0
if j<k:
   t= s.replace(s[j:k+4],'good')
print(t)    
