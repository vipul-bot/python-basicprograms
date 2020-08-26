n=int(input())
l1=[]
q='0'
l=list(map(str,input().split()))
for i in range(0,int(len(l)/2)):
    l1.append(l[i][0])
for j in range(int(len(l)/2),len(l)):
    l1.append(l[j][-1])
for k in range(0,len(l1)):
     q+=l1[k]
q=int(q)
if q%11==0:
    print("OUI")
else:
    print('NON')    

