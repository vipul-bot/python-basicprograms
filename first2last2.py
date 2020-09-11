s=input()
if len(s)>=2:
    j=s[0:2]+s[-2:len(s)]
    print(j)
else:
    print("empty string")
