s=input()
count=0
if len(s)%2!=0:
    for i in range(0,int((len(s)-1)/2)):
        if s[i]==s[len(s)-1-i]:
            count+=1
        else :
            print('NO')
    if count==int((len(s)-1)/2):
        print('YES')
