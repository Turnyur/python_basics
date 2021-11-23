def getSum(x, y):
     res =int(x)+int(y)
     return res


def printHello():
    print("Hello")


num1 =input("Enter Number 1: ")
num2 =input("Enter Number 2: ")

print("Returned Summation is: ", getSum(num1, num2))

a = printHello
a()