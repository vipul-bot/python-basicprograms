l=int(input())
n=int(input())
li=[]
for i in range(0,n):
    w,h=input().split()
    w,h=int(w),int(h)
    if l>w or l>h:
        li.append("UPLOAD ANOTHER")
    if l<=w and l<=h:
        if w==h:
           li.append("ACCEPTED")
        else: 
           li.append("CROP IT")
for d in range(0,len(li)):
    print(li[d])                
        


