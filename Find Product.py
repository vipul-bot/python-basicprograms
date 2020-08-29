n=int(input())
a=list(map(int,input().split()))
b=1
for i in range(n):
    b=(b*a[i])%(10**9+7)
print(b)    
        
        
