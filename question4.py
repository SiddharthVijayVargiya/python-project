'''variable size sliding window'''
'''

Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence 
and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.



















'''
def longest_str(s):
    # Step 1: Initialize the left pointer for the sliding window, a set to store characters,
    # and a variable to track the maximum length of the substring without repeating characters.
    left = 0  # This is the left boundary of the sliding window.
    char_set = set()  # A set to store the unique characters in the current window.
    max_length = 0  # To keep track of the maximum length of substring without repeating characters.
    
    # Step 2: Iterate through the string with the right pointer.
    # The right pointer will move one step at a time, expanding the window.
    for right in range(len(s)):
        
        # Step 3: Check if the current character (s[right]) is already in the set.
        # If it is, it means we've encountered a repeated character, and we need
        # to adjust the window by moving the left pointer to the right until the
        # repeated character is removed from the set.
        while s[right] in char_set:
            # Remove the character at the left pointer from the set
            # and increment the left pointer to shrink the window.
            char_set.remove(s[left])
            left += 1  # Move the left boundary of the window to the right.
        
        # Step 4: Add the current character (s[right]) to the set, as it is now part of the window.
        char_set.add(s[right])
        
        # Step 5: Update the maximum length if the current window is larger than the previous one.
        # The window size is calculated as (right - left + 1), which is the number of characters
        # between the left and right pointers, inclusive.
        max_length = max(max_length, right - left + 1)
    
    # Step 6: Return the maximum length of the substring without repeating characters.
    return max_length

s = "aaaaabbbbbccccc" 
print(longest_str(s)) 
#For the input string "aaaaabbbbbccccc", the function returns 2. 
# This is because the longest substrings without 
# repeating characters are "ab" or "bc", each of which has a length of 2.
   

#logic
'''
s = "abcabcbb"
 
Window [a] -> max_len = 1
Window [a, b] -> max_len = 2
Window [a, b, c] -> max_len = 3
Duplicate found (a):
Shrink -> Window [b, c, a] -> max_len = 3
Duplicate found (b):
Shrink -> Window [c, a, b] -> max_len = 3
...
Final Answer = 3


'''


'''
Setup:
Let’s define a few key points:

We are given a string s = "abcabcbb".
We use two pointers:
Left pointer (left): It marks the start of the current window.
Right pointer (right): It marks the end of the current window, and 
slides from left to right.
We maintain:

A set to track the unique characters in the window.
A variable max_len to keep track of the maximum
length of the substring without repeating characters.
'''





'''
Step-by-step visualization:
Initial State:
left = 0, right = 0, max_len = 0
char_set = {}
Step 1 (Right Pointer at Index 0: 'a'):
Window: [a]
Set: {a}
max_len = 1 because right - left + 1 = 1 - 0 + 1 = 1
Step 2 (Right Pointer at Index 1: 'b'):
Window: [a, b]
Set: {a, b}
max_len = 2 because right - left + 1 = 2 - 0 + 1 = 2
Step 3 (Right Pointer at Index 2: 'c'):
Window: [a, b, c]
Set: {a, b, c}
max_len = 3 because right - left + 1 = 3 - 0 + 1 = 3
Step 4 (Right Pointer at Index 3: 'a'):
Duplicate 'a' found.
We shrink the window by moving the left pointer
until the duplicate is removed.
Window after shrinking: [b, c, a]
Set: {b, c, a}
max_len = 3 (No change as the current window length is still 3)
Step 5 (Right Pointer at Index 4: 'b'):
Duplicate 'b' found.
Shrink window by moving the left pointer.
Window after shrinking: [c, a, b]
Set: {c, a, b}
max_len = 3 (No change)
Step 6 (Right Pointer at Index 5: 'c'):
Duplicate 'c' found.
Shrink window by moving the left pointer.
Window after shrinking: [a, b, c]
Set: {a, b, c}
max_len = 3 (No change)
Step 7 (Right Pointer at Index 6: 'b'):
Duplicate 'b' found.
Shrink window by moving the left pointer.
Window after shrinking: [c, b]
Set: {c, b}
max_len = 3 (No change)
Step 8 (Right Pointer at Index 7: 'b'):
Duplicate 'b' found.
Shrink window by moving the left pointer.
Window after shrinking: [b]
Set: {b}
max_len = 3 (No change)
Final Answer:
The longest substring without repeating
characters is "abc", and the length is 3.
'''