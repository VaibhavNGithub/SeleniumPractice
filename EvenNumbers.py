n = int(input('Enter Number:-'))
s = 0
i = 1

while(i<=n):
    if(i%2==0):
        s = s + i**2
    i = i + 1
    
print('Sum of Square of all even numbers till {} is {}'.format(n,s))