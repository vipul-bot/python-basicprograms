t=int(input())
l=[]
for z in range(0,t):
    
    cgreen,cpurple=input().split()
    cgreen=int(cgreen);cpurple=int(cpurple)
    if z in (1,3,5,7,9):
        (cgreen,cpurple)=(cpurple,cgreen)
        
    n=input()
    n=int(n)
    tgreencost=0;tpurplecost=0
    for k in range(0,n):
        i,j=input().split()
        i=int(i);j=int(j)
        if i==1:
           tgreencost+=cgreen
        if j==1:
           tpurplecost+=cpurple
    l.append(tgreencost+tpurplecost)
for k in range(0,len(l)):
    print(l[k])
        
      
