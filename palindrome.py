'''
Example 2: Checking for Palindrome
Problem: Given a string, check if it is a palindrome.

String: "racecar"

Approach:

Initialize Pointers: left at index 0, right at index len(string) - 1.
Check Characters:
Compare string[left] with string[right].
If they are not equal, the string is not a palindrome.
If they are equal, move left forward and right backward.'''
def is_palindrome(s):
    # Initialize the left pointer at the start of the string
    left = 0
    
    # Initialize the right pointer at the end of the string
    right = len(s) - 1
    
    # Loop until the left pointer is less than the right pointer
    while left < right:
        # Check if the characters at the left and right pointers are not equal
        if s[left] != s[right]:
            # If they are not equal, the string is not a palindrome
            return False
        
        # Move the left pointer to the right
        left += 1
        
        # Move the right pointer to the left
        right -= 1
    
    # If all characters matched, the string is a palindrome
    return True

# Usage
s = "racecar"  # Define a string to check if it's a palindrome
print(is_palindrome(s))  # Call the function and print the result, expected output: True

