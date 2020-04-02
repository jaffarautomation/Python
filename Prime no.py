Number =int(input("Please enter the no"))




for i in range(2,Number):
    if Number%i==0:
        print("The given number is not prime because it is divisble by ", i)
        break
else:
    print("Number is prime")












