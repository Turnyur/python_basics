numbers = [5, 2, 3, 7, 4]
print(numbers)
numbers.append(30)
print(f"Append 30: {numbers}")
numbers.insert(0, 10)
print(f"Insert 10 at index 0: {numbers}")
numbers.remove(5)
print(f"Remove 5: {numbers}")
print("Is 5 in Numbers List:", (5 in numbers))
numbers.pop()
numbers.insert(0, 12)
numbers.insert(0, 12)
numbers.insert(0, 12)
print(numbers)
print(numbers.count(12))
print(numbers)
print(f"Pop: {numbers}")
numbers.sort()
print("Sort: ", numbers)
numbers.reverse()
print("Reverse", numbers)
#numbers.clear()
#print(f"Clear: {numbers}")


numbers2 = numbers.copy()
numbers.clear() 
print("NUMBERS: ", numbers)
print("NUMBERS_2: ", numbers2)


a = [5,10,15,20,25,30,35,40]

# a[2] = 15
print("a[2] = ", a[2])

# a[0:3] = [5, 10, 15]
print("a[0:3] = ", a[0:3])

# a[5:] = [30, 35, 40]
print("a[5:] = ", a[5:])