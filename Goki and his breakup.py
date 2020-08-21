N=int(input())
x=int(input())
l=[]
for i in range(0,N):
    y=int(input())
    if y>=x:
        l.append('YES')
    else:
        l.append('NO')
for j in range (0,len(l)):
    print(l[j])            
