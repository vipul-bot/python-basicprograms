#fizz buzz test
#3 multiple is fizz
#5 multiple is buzz
#3,5 multiple is fizz buzz
#run it from 1 to 20
for i in range(1,20):
    if i%3==0 and i%5==0:
        print("Fizzbuzz")
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print("Buzz")
    else:
        print(i)
        
    
