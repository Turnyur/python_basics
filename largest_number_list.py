m_size = input("What is the size of the list? ")
container=[]
i = 1
max_number=0
#print(type(max_number))
while i <= int(m_size):
    container.insert(i, input())
    i+=1
for index, item in enumerate(container):
    int_item =int(item)
    if int_item>max_number:
        max_number=int_item
print(f"Max number is: {max_number}")