import math
for i in range(1000,10000):
    j=str(i)
    for k in range(len(j)):
        if int(j[k])%2!=0:      #all digits even section
           break
    else:    
        m=math.sqrt(i)
        if m in range(30,101):   #checking perfect square
           print(i)
        
#perfect square with even digits between 1000 to 10000
