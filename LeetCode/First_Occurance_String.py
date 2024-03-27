'''
Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

'''
def string_occurance(input_string, string_to_search) -> int:
    if needle in haystack:
        indices = []
        for letters in haystack:
            if letters == needle[0]:
                indices.append(haystack.index(letters))
            else:
                pass
        
        return indices
    else:
        return -1


haystack = "sadbutsad"
needle = "sad"

result = string_occurance(haystack, needle)
print(result)