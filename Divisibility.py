N=int(input())
q='0'
l=[]
n=list(map(str,input().split()))
for i in range(0,len(n)):
    l.append(n[i][-1])
for j in range(0,len(l)):
    q+=l[j]
q=int(q)    
    

print(q)
if q%10==0:
    print("Yes")
else:
    print("No")        
