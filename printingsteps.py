#step pyramid
'''
1
22
333
4444
55555
666666
'''
n=int(input("Enter the number of steps : "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end='')
    print('\n')    
    
