#fibonacci series,
#0,1,1,2,3,5,8
f1=0;f2=1;x=0
n=int(input())
for i in range(n):
    if i in (0,1):
        print(i)
    else:
        x=f2+f1
        print(x)
        f1=f2
        f2=x
        
        
