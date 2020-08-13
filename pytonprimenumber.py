def prime(k):
   l=[]
   for i in range(2,k+1):
        if cd(i) != 1:
            l.append(i)
   return(l)
def cd(n):
   for i in range(2,n+1):
       if n%i==0 and n==i:
           return(n)
       if n%i==0 and n!=i:
           return(1)
t=int(input("please enter the number n : "))
print(prime(t))     
