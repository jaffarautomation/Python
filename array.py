from array import *

va=array('i', [1,2,4,5,7,8,9])

#Below code of line will print the lenght of an array. This will also give address of an array
print(va.buffer_info())

#Below code of line will also print the lenght of an array
print(len(va))

#Below code of line will give an error, because type is int i.e i
# print(va.append(8.5))

#print the type of an array
print(va.typecode)

#In array we can iterate.
print(va[0])

#iterate over a forLoop
for i in range(len(va)):
    print(va[i])

#to insert value at specific index
va.insert(2,45)
print(va)

#to add value in last
va.append(40)
print(va)

#Silicing an array
print(va[4:])

print(len(va))
print(va[4:9])

#to update an array
va[0]=12




print(va)

