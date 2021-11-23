x = 10
y = 12

# Output: x > y is False
print('x > y is',x>y)
# Output: x < y is True
print('x < y is',x<y)
# Output: x == y is False
print('x == y is',x==y)

# Output: x != y is True
print('x != y is',x!=y)
# Output: x >= y is False
print('x >= y is',x>=y)
# Output: x <= y is True
print('x <= y is',x<=y)




#Logical Operators

x = True
y = False
print('x and y is',x and y)
print('x or y is',x or y)
print('not x is',not x)

print()
print()
print()
print()
#Identity Operators
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

# Output: False
print(x1 is not y1)
# Output: True
print(x2 is y2)
# Output: False
print(x3 is y3)


#Membership operators
print()
print()
x = 'Hello world'
y = {1:'a',2:'b'}
# Output: True
print('H' in x)
# Output: True
print('hello' not in x)
# Output: True
print(1 in y)
# Output: False
print('a' in y)
print('Address: ', id(x))