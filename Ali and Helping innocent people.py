S=input()
if S[2] in ('A','E','I','O','U','Y'):
    print('invalid')
    exit()
for j in range(len(S)-1):
    if j in (1,2,5, 6):
        continue
    else:
        if (int(S[j])+int(S[j+1]))%2==0:
            continue
        else:
            print('invalid')
            exit()
print('valid')                        
    
    
