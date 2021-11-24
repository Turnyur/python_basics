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

def pythonPass():
    '''pass is just a placeholder for
    functionality to be added later.'''
    sequence = {'p', 'a', 's', 's'}
    print("Executing pythonPass ...")
    for val in sequence:
        pass


num1 =input("Enter Number 1: ")
num2 =input("Enter Number 2: ")

print("Returned Summation is: ", getSum(num1, num2))

a = printHello
a()
greet("Monica", "Luke", "Steve", "John")
pythonPass()