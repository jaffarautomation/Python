# you can  create a function by using def keyword. A function can have arguments and it can return two value.

#this function return two values
def add (x,y):
    c= x+y
    d=x-y
    return d,c

result1 =  add(10,5)
print(result1)


#python is not pass by value and pass by object.
#Pass by value---> In this obly value of variable is pass and it will not affect the caller value
#for  Ex : here a is main variable and x is the another variable, and if we pass a in value argument , we can see they both have same id. Well this mean it is pass by reference?
#Actually no, becuase the value of a is not change....it can be see from code itself. If you uncomment the line 21 and 22
# In python everything is an object, if i create the int i =10 and int b=10; though they have same value there address or id will be same. in other word they both i and b points to same memory location i.e 10
#thats why the id of both a and x in function is same.

#Now if you change the value of x inside the function then, a new memory location will be created for x and value of a will remain unchanged.
#remmember, in python intm str are immutable. once value assigned they cant be changed in future. thats why a new momory location for x is created



#In below code x will first receive the value as 10...since it got change in later part of code ...thats why new memory for the value is created and x is now pointing to new value
def value(x):
    print(id(x))


    x=8
    print(id(x))

    print("x",x)

a=10
print(id(a))

a=89
print(id(a))

value(a)
print("a" , a)


############################################################################################################################


#In below code of line, we have created the function which takes argument as List. comment out line 54 and 55.
#In python if we create two variable having same value, they both refer to same memory location, like string constant pool in java. But in python thats a case with int, string and list,set etc.
#for int and string, they are immutable means there value cant be change.
#but as list is mutable, when we change the list value from the function, both original and argument list value got change and they all refer to same object.


def mutablevalue (Li):

   print(id(Li))

   # Li[0] =15
   # print(id(Li))

   print("Li", Li)


list =[10,20, 30]
print(id(list))
mutablevalue(list)
print("List", list)

