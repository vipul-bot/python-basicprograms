def check(n):
    for i in range(2,n+1):
        if n%i==0 and n!=i:
            break
    else:
        return n
    return -1
n=int(input())
l=[]
for i in range(2,n):
    l.append(check(i))
for j in l:
    if j==-1:
        continue
    print(j)
    
