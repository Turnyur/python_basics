matrix = [
    [4,5,1],
    [7,8,3],
    [2,3,9]
]

#print(matrix[:])
# print(f''' 
#     [
#         {matrix}
       
#     ]
# ''')
i=0
print("[")
for row in matrix:
    print("[", end=" ")
    for item in row:
        print(item, end=" ")
    print("]", end=" ")
print("]", end=" ")