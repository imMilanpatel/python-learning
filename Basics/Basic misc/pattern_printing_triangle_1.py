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

# Constants
lines_to_print = 8
spaces = 0

for line in range(1,lines_to_print + 1):
    print("|", " " * 2 * line, "*")
    spaces += 2
    print(spaces)
    