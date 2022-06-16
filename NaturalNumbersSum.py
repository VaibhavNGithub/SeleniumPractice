n = int(input('Enter Number:-'))
i=1
s = 0

while(i<=n):
    s = s + i**2
    i = i + 1

print('Sum of square of all natural number till {} is {}'.format(n,s))
