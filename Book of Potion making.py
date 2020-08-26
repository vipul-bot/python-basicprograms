n=input()
s=0
for i in range(0,len(n)):
    s=s+((i+1)*int(n[i]))
if s%11==0:
    print("Legal ISBN")
else:
    print("Illegal ISBN")        
