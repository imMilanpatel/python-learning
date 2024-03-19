# print the following pattern
"""
|  *
|    *
|      *
|        *
|      *
|    *
|  *
|
|  *
|    *
|      *
|        *
|      *
|    *
|  *
|
|  *
|    *
|      *
|        *
|      *
|    *
|  *

"""

# Number of triangles to print
num_triangles = 3

# Loop for the specified number of triangles
for _ in range(num_triangles):
    # Incrementing stars with 2 spaces
    for spaces in range(0, 7, 2):
        print("|" , " " * spaces , "*")
    # Decrementing stars with 2 spaces
    for spaces in range(5, 0, -2):
        print("|" , " " * spaces , "*")
    # Avoiding a break between triangles
    if _ != num_triangles - 1:
        print("|")