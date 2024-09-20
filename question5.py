'''
Problem Statement: Longest Common Prefix
Given an array of strings arr, write a function to find the longest common prefix among all the
strings. If there is no common prefix, return an empty string "".

Input:
arr: A list of strings, with 1 <= len(arr) <= 200 and each string having a length of 1 <= len(string) <= 200.
Output:
Return the longest common prefix among all the strings in the array. If no common prefix exists, return "".

'''


#Input: arr = ["flower", "flow", "flight"]
#Output: "fl"
#Explanation: The longest common prefix among all strings is "fl".




'''
Input: arr = ["dog", "racecar", "car"]
Output: ""
Explanation: There is no common prefix among the input strings.

'''


'''
Constraints:
All strings in the input array consist of lowercase English letters.
Notes:
The common prefix is the initial part of each string that is shared by all strings in the array.
You must compare each string and iteratively reduce the prefix until the longest possible common prefix is found.

'''
def longest_common_prefix(arr):
    # Step 1: Handle the edge case where the input array is empty.
    # If the input list of strings is empty, return an empty string immediately
    if not arr:
        return ""  # No strings to compare, so no common prefix is possible.
    
    # Step 2: Initialize the prefix as the first string in the array.
    # The assumption is that the first string could potentially be the common prefix,
    # and we will try to reduce it by comparing with other strings.
    prefix = arr[0]
    
    # Step 3: Iterate through each of the remaining strings in the array.
    # We start from the second string, because we already initialized the prefix
    # with the first string.
    for string in arr[1:]:
        # Step 4: Compare the current string with the prefix.
        # The loop checks if the current string starts with the current prefix.
        # If it doesn't, we reduce the prefix by removing its last character.
        # This process continues until the prefix becomes a valid common prefix
        # for the current string, or until it becomes empty.
        while string[:len(prefix)] != prefix and prefix:
            # Step 5: Gradually reduce the prefix by slicing off the last character.
            # Each time the prefix doesn't match the start of the string, 
            # we shorten the prefix from the right side by one character.
            prefix = prefix[:-1]
        
        # Step 6: If at any point the prefix becomes empty, we can break the loop early.
        # This means there is no common prefix at all between the strings.
        if not prefix:
            break  # No need to check further; no common prefix exists.

    # Step 7: After comparing with all strings, return the resulting prefix.
    # If a common prefix was found, it will be returned; otherwise, an empty
    # string will be returned if no common prefix exists across all strings.
    return prefix

# Example test case:
arr = ['a','abccd', 'abccd','ab']  # All strings are identical, so the common prefix is the entire string.
print(longest_common_prefix(arr))  # Output: "abccd"

