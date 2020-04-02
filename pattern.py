
for i in range(1,5):       #rows
    for j in range(i):
        print(' #', end="")
    print()


for i in range(4):       #rows
    for j in range(4-i):
        print(' #',end="")
    print()



X=[1,2,3,4,5]
for i in range(1,6):       #rows
    for j in range(1,i):
        print(j, end="")
    print()


for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j, end="")
    print()





print(list(range(5,0,-1)))
print(list(range(0,6,1)))
print(list(range(1,6,1)))
print(list(range(2,6,1)))