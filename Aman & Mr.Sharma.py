import math
d=int(input());t=0
for i in range(d):

    r,x=input().split()
    r,x=int(r),int(x)
    dis=100*x
    circum=math.pi*2*r
    if dis>=circum:
        t+=1
print(t)       

