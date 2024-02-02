'''
Find the common Elements in an Array.

Array_1 = [1,2,3,2,1]
Array_2 = [1,2,3]
Array_3 = [1,2,3,4]

Output should be.,
[1,2,3]

Array can be of any size and by default there should be two arrays for comparison.

'''
# SOME MORE MODIFICATIONS NEED TO BE DONE.


# Milan Patel version of the solution
# Version 1, using "set".
Array_1 = [1,2,3,2,1]
Array_2 = [1,2,3]
Array_3 = [1,2,3,4]

common_elements = set(Array_1) & set(Array_2) & set(Array_3)
print(list(common_elements))


###########################################################

# Version 2 using for and if loops with a dedicated method.

def find_common_elements(arr1, arr2, arr3):
    common_elements = []

    for elem1 in arr1:
        if elem1 in arr2 and elem1 in arr3 and elem1 not in common_elements:
            common_elements.append(elem1)

    for elem2 in arr2:
        if elem2 in arr1 and elem2 in arr3 and elem2 not in common_elements:
            common_elements.append(elem2)

    for elem3 in arr3:
        if elem3 in arr1 and elem3 in arr2 and elem3 not in common_elements:
            common_elements.append(elem3)

    return common_elements

result = find_common_elements(Array_1, Array_2, Array_3)
print(result)

###########################################################