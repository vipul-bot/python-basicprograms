N,Q=input().split()
N,Q=int(N),int(Q)
l1=[]
Numbers=list(map(int,input().split()))
for i in range(Q):
    f,l,mean,count=0,0,0,0
    L,R=input().split()
    L,R=int(L),int(R)
    for j in range(len(Numbers)):
        if Numbers[j]==L:
            f=j
        if Numbers[j]==R:
            l=j
    for k in range(f,l+1):
        mean+=Numbers[k]
        count+=1
    l1.append(mean/count)
for l in range(len(l1)):
    print(int(l1[l]))   
