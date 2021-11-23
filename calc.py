print("How many numbers do you want to calculate? ")
loop_counter = input()
counter = 1
number_container =[]
result=0
operato_valid = True
while counter<=int(loop_counter):
    number_container.insert(counter, int(input())) 
    counter+=1
print(number_container)
m_operator = input("What operation do you want to perform?: ")
if m_operator=="/":
      for index, num in enumerate(number_container):
        if index==0:
            result=num
            continue
        result /= num
elif m_operator=="-":
    for num in number_container:
        result -= num
elif m_operator=="*":
    for index, num in enumerate(number_container):
        if index==0:
            result=num
            continue
        result *= num
elif m_operator=="+":
    for num in number_container:
        result += num
else:
    operato_valid = False

if not operato_valid:
    print("Enter a valid mathematical operator")
else:
    print(f"The result of '{m_operator}' operation is: {int(result)}")