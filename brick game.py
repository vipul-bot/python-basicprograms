'''Patlu and Motu works in a building construction, they have to put some number of bricks N from one place to another, and started doing their work. They decided , they end up with a fun challenge who will put the last brick.

They to follow a simple rule, In the i'th round, Patlu puts i bricks whereas Motu puts ix2 bricks.

There are only N bricks, you need to help find the challenge result to find who put the last brick.

Input:

First line contains an integer N.

Output:

Output "Patlu" (without the quotes) if Patlu puts the last bricks ,"Motu"(without the quotes) otherwise.'''
N=int(input())
p=1;m=2
a=((N//3)+1)
for k in range(1,a):
    if k==p:
        N=N-p
        p=p+1
    elif N<p:
        print("Patlu")
        exit()
    if k*2==m:
        N=N-m
        m=m*p
    elif N<m:
        print("Motu")
        exit()                

    

