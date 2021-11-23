unstructured_numbers = [5, 2, 3, 7, 7, 10, 4, 2, 2, 3, 7]
cleaned_numbers = []

for item in unstructured_numbers:
    if item not in cleaned_numbers:
        cleaned_numbers.insert(len(cleaned_numbers), item)
print("Original List: ", unstructured_numbers)
print("Cleaned List: ", cleaned_numbers)

