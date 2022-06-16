l1 = [1,2,3,4,5,6,1,3,8,9,5,3,2,5]
l2 = set(l1)
l3 = []
print(l2)
  
for val in l2:
    c = l1.count(val)
    if c > 1:
        l3.append(val)
        print("{} occured {} times".format(val,c))
print(l3)
#==================================================================================l1 = [1,2,3,4,5,6,1,3,8,9,5,3,2,5]
l2 = []
for el in l1:
    if el not in l2:
        l2.append(el)
l3 = []
print(l2)
   
for val in l2:
    c = l1.count(val)
    if c > 1:
        l3.append(val)
        print("{} occured {} times".format(val,c))
print(l3)
#==================================================================================
import numpy as np
l1 = [1,2,3,4,5,6,1,3,8,9,5,3,2,5]
print(np.unique(l1))

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