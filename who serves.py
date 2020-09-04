n=int(input())
l=[]
for i in range(n):
    q=0
    p1,p2,k=input().split()
    p1,p2,k=int(p1),int(p2),int(k)
    q=(p1+p2)//k
    if q%2==0:
        l.append("CHEF")
    else:
        l.append("COOK")        
for j in range(len(l)):
    print(l[j])
