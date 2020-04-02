from array import *

#To take input from user for an array
Number =int(input('Please enter the size of an array'))
va=array('i',[])
for i in range(Number):
        n= int(input('Please enter the number in array'))
        va.append(n)
print(va)

#Taking input from user for which value need to be serach in array
k=0
v=int(input('Enter the value which need to be search'))
for e in va:
    if e==v:
        print('Yes the given value is present at index no:', k)
        break
    k+=1
else:
    print('no value as such')

va.


