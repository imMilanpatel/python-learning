# List of colors 
colors = ["blue", "red", "purple", "orange", "white", "grey", "yellow", "black", "green"]

# Change the value None to the index of the color grey
# index_grey = None
index_grey = colors.index("grey")
print('You must see here the index of the color grey:', index_grey)

# Change the value None to access to the color purple with the right index
# purple = None
purple_index = colors.index("purple")
purple = colors[purple_index]
print('You must see here the color purple:', purple)

# uncomment lines bellow to see if your results is correct
# Will throw an error if your solution is incorrect

assert(index_grey == 5)
assert(purple == 'purple')