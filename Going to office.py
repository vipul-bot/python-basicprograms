D=int(input())
c,f,d=input().split()
c,f,d=int(c),int(f),int(d)
s,b,m,e=input().split()
s,b,m,e=int(s),int(b),int(m),int(e)
OT=c+(D-f)*d
CT=int(b+((D//s)*m)+(D*e))
if OT>CT:
    print("Classic Taxi")
else   :
    print("Online Taxi") 
