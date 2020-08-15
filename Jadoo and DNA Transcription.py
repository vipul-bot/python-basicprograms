def ff(a):
 k=''   
 for i in a:
  if i =='C' or i=='c':
   i="G"
   k+=i
  elif i=='G' or i=='g':
   i='C'
   k+=i
  elif i=='T' or i=='t':
   i='A'
   k+=i
  elif i=='A' or i=='a':
   i='U'
   k+=i
  else :
   return('Invalid Input')
 return(k)  

a=input()

print(ff(a))   

  
