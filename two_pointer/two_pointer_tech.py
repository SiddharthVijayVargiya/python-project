           #Two-Pointer Technique
           
'''
Concept: The two-pointer technique involves using two 
pointers to traverse an array or a list. These pointers are 
usually initialized at different positions (e.g., start and end) and 
moved towards each other based on certain conditions.'''

'''
Types of Problems:

Finding pairs with a given sum.
Checking for palindromes.
Sorting and merging arrays.
Removing duplicates.
'''
'''
Here are some typical uses of the two-pointer technique:

1 Finding pairs in a sorted array: 
You can use one pointer at the start and one at the end to
find pairs of numbers that satisfy a certain condition.

2 Reversing an array or string: 
One pointer starts from the beginning and the other from 
the end, and you swap elements until the pointers meet.

3 Removing duplicates:
Use two pointers to track unique elements and shift them
to the front of the array
'''


'''
Basic Steps:
Initialize Two Pointers: Usually, 
one pointer starts from the beginning (left), 
and the other starts from the end (right).
Move Pointers: Based on the condition, move the pointers towards 
each other
or in specific directions.
Check Conditions: Check if the condition (like sum, equality) 
is met and take necessary actions (e.g., store result, move pointers).

'''


'''
Examples:
Example 1: Finding a Pair with a Given Sum
Problem: Given a sorted array and a target sum, 
find if there is a pair that adds up to the target sum.

Array: [1, 3, 4, 6, 8, 10]
Target Sum: 9
'''


'''
Approach:

Initialize Pointers: left at index 0, right at index 5 (end).
Check Sum:
1 Calculate current_sum = array[left] + array[right].
2 If current_sum equals target, return the pair.
3 If current_sum is less than target, 
increment left (move towards right).
4 If current_sum is greater than target, 
decrement right (move towards left).
'''

def find_pair_with_sum(arr, target):
    # Initialize the left pointer at the start of the array
    left = 0
    
    # Initialize the right pointer at the end of the array
    right = len(arr) - 1
    
    # Loop until the left pointer is less than the right pointer
    while left < right:
        # Calculate the sum of elements at the left and right pointers
        current_sum = arr[left] + arr[right]
        
        # Check if the current_sum is equal to the target
        if current_sum == target:
            # If true, return the pair of elements (arr[left], arr[right])
            return (arr[left], arr[right])
        
        # If current_sum is less than the target, move the left pointer to 
        # the right
        elif current_sum < target:
            left += 1
        
        # If current_sum is greater than the target, move the right pointer to the left
        else:
            right -= 1
    
    # If no pair is found that sums up to the target, return None
    return None


# Usage
arr = [1, 3, 4, 6, 8, 10]
target = 9
print(find_pair_with_sum(arr, target))  # Output: (4, 5)
 
 
 
#Same way with palindrome 
'''
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

'''



#Visualization:
#For the string "racecar":

#Initial State:

#left = 0 (points to 'r'), right = 6 (points to 'r').
#After First Comparison:

#left = 1 (points to 'a'), right = 5 (points to 'a').
#After Second Comparison:

#left = 2 (points to 'c'), right = 4 (points to 'c').
#After Third Comparison:

#left = 3 (points to 'e'), right = 3 (also points to 'e').
#At this point, left = right, so no further comparisons are needed. 
# The loop terminates.


