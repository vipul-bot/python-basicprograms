

word=input()
x=0;y=0
for i in word:
   if i=='z' or i=='Z':
       x+=1
   else	:
       y+=1
if 2*x==y:
   print('yes')
else:
   print('No')   	      
