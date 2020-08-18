s=input()
x=0;y=0
for i in range(0,len(s)):
    if s[i]=='L':
      x=x-1
    elif s[i]=="R":
      x=x+1
    elif s[i]=="U":
      y=y+1
    elif s[i]=='D':
      y=y-1
print(x,y)	            
