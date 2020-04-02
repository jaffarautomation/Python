
#Below code give insight about pass keyword in python
from builtins import print

for i in range(1, 51):

    if i%2!=0:
        pass   #it is necessary to provide some statement in method or if and else block, simply they cant be empty. But if you wish not to write any statement you can use pass keyword
        #It simply means user dont want to provide any implemenation as of now....can you please skip these func or block and move forward
    else:
        print('This are all odd no', i)
print('bye')



# Below code give insight about break keyword in python
available =10
user =12

for i in range(user):
    if (i<=available):
        print("You have received you candy", i)
    else:
        print('sorry we are out of stock')
        break
    i+=1

print("bye")


#Below code explain the continue keyword. When you want to skip condition you can use continue
for i in range(5):
    if i==3:
        continue
    print("hello", i)
