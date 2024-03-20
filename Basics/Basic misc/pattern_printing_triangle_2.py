'''
This program will print the following pattern,

        *
      * * * 
    * * * * *
  * * * * * * *
* * * * * * * * * 

'''

lines = 1
for _ in range(lines):
    print(" " * 8, "*")
    print(" " * 6, "*" * 5)
    print(" " * 4, "*" * 10)
    print(" " * 2, "*" * 14)
    print("*" * 20)