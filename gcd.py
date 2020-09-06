#greatest common divisior
#taken a as greatest
def gcd(a,b):
    
    if a<b:
        (a,b)=(b,a)
    #euclid algorithm is if a,b gcd is b c
    #then r which is a%b is also divisible by c
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)
a,b=input().split()
a,b=int(a),int(b)    
print(gcd(a,b))    
