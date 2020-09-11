def p_star(n):
    for i in range(n):
        if i>0:
            for k in range(i):
                print(' ',end='')
        for j in range(n,i,-1):
            print('*',end='')
        print('\n')    
        
    return ''
    

n=int(input("Enter the value : "))
print(p_star(n))
