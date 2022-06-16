# **********Prime Number**********

n = int(input('Enter Number:-'))
count = 0
i = 1

while(i<=n):
    if(n%i == 0):
        count = count + 1
    i = i + 1

if(count == 2):
    print('{} is a prime number'.format(n))
else:
    print('{} is not a prime number'.format(n))