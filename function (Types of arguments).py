

#Here x and y are called the  formal arguments
def add(x,y):
     c=x+y
     print(c)

#here 5 and 6 are called actual argument becuase you are actually passing some value
#Actual arguments ---> Position, keyword, defualt, variable lenght
add(5,6)


#1)
def person (name, age):
    print(name)
    print(age)

#This is called the kyword argument becuase you are mentioning the actual name of the argument
person(name='jeff', age=45)

#2) Default
#If you dont pass the argument then, function will throw an error, but in case you want to pass only one argument while calling the method, then you need to define the actual value in formal arguments
#in this case it is age
def person (name, age=18):
    print(name)
    print(age)

person('jeff')


#3)Variable lenght
#In java, we create the method depending upon the no of arguments, there is no concept of passing more argument as defined in the method.
#But in python you can create the dynamic argument, when you are not sure whether your method will hold 2 or 3 or more argument, you can create the variable lenght function as mention below
#Here 1 value will assign to a as int  and 4,5,6 value will assign to b as a tuple not int


def add(a,*b):

    print(a)
    print(b)
    c=0
    for i in b:
        c =c+i
    z=a+c
    print(z)

add(1,4,5,6)