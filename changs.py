s=input()
if len(s)>=3:
    if s.endswith('ing',0,len(s)):
        s+='ly'
    else:
        s+='ing'
else:
    pass
print(s)
