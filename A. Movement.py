n=int(input())
count=0
while n>0:
    if n>=5:
        count+=1
        n-=5
      
    elif n>=4:
        count+=1
        n-=4
        
    elif n>=3:
        count+=1
        n-=3
        
    elif n>=2:
        count+=1
        n-=2
            
    elif n>=1 :
        count+=1
        n-=1
    
print(count)           
