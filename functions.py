def getSum(x, y):
     res =int(x)+int(y)
     return res


def printHello():
    print("Hello")


def greet(*names):
    """This function greets all
    the person in the names tuple."""
    print(type(names))
    # names is a tuple with arguments
    for name in names:
        print("Welcome", name)


num1 =input("Enter Number 1: ")
num2 =input("Enter Number 2: ")

print("Returned Summation is: ", getSum(num1, num2))

a = printHello
a()
greet("Monica", "Luke", "Steve", "John")