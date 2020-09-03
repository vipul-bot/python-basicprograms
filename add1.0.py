l=[1,2,4,4]
L=[1,3,5,]
'''def add(x,y):
    return x+y
r=list(map(add,l,L))'''
r=list(map(lambda x,y:x+y,l,L))

print(r)
