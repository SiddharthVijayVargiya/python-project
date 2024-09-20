#"I Looked While Moving Swiftly Right"
'''
I: Initialize variables (n, left, window_sum, min_length).
L: Loop through the array (right as the window end).
W: While window_sum >= S, update min_length.
M: Move the left pointer to shrink the window.
S: Sum check if a valid subarray exists; return result.
'''

"""
    Function to find the minimum length of a subarray with sum greater than or 
    equal to a given value S.
    
    Parameters:
    arr (list): Input array of integers
    S (int): Target sum value

    Returns:
    int: Minimum length of the subarray with sum >= S, or 0
    if no such subarray exists
"""
def min_subarray_length(arr, S):    
    n = len(arr)  # Get the size of the array
    left = 0  # This will point to the start of our current window
    window_sum = 0  # The sum of the current window
    min_length = float('inf')  # A very large value to track the
                               # minimum length of the subarray
    
    # Loop through the array with 'right' as the end of the window
    for right in range(n):
        window_sum += arr[right]  # Add the current element to the window sum
        
        # Try to shrink the window from the left while the window sum is greater
        # than or equal to S
        while window_sum >= S:
            # Update the minimum length if the current window is smaller
            min_length = min(min_length, right - left + 1)
            
            # Shrink the window by moving 'left' and subtracting the element 
            # at 'left' from the sum
            window_sum -= arr[left]
            left += 1
            
    # If no valid subarray was found, return 0. Otherwise, return the minimum 
    # length found.
    return min_length if min_length != float('inf') else 0


# Example Usage:

arr = [2, 3, 1, 2, 4, 3]
S = 7
result = min_subarray_length(arr, S)
print(result)  # Output will be 2

# Explanation:
# The smallest subarray with a sum >= 7 is [4, 3] with a length of 2.



'''
Step-by-step Mathematical Visualization:
Initialization:
    left = 0 (Initial window starting point)
    window_sum = 0 (Sum of the current window)
    min_length = ∞ (Tracks minimum subarray length)

First Iteration (right = 0):
    right = 0, arr[right] = 2
    window_sum = 2
    Since window_sum < S, we continue expanding the window.

Second Iteration (right = 1):
    right = 1, arr[right] = 3
    window_sum = 2 + 3 = 5
    Since window_sum < S, we continue expanding the window.

Third Iteration (right = 2):
    right = 2, arr[right] = 1
    window_sum = 5 + 1 = 6
    Since window_sum < S, we continue expanding the window.

Fourth Iteration (right = 3):
    right = 3, arr[right] = 2
    window_sum = 6 + 2 = 8
    Now, window_sum >= S, so we update:
    min_length = min(∞, 3 - 0 + 1) = 4.
    To shrink the window, we subtract arr[left] = 2 from window_sum:
    window_sum = 8 - 2 = 6, left = 1.

Fifth Iteration (right = 4):
    right = 4, arr[right] = 4
    window_sum = 6 + 4 = 10
    Now, window_sum >= S, so we update:
    min_length = min(4, 4 - 1 + 1) = 4.
    We shrink the window by subtracting arr[left] = 3:
    window_sum = 10 - 3 = 7, left = 2.
    Again, window_sum >= S, so we update:
    min_length = min(4, 4 - 2 + 1) = 3.
    We shrink the window again by subtracting arr[left] = 1:
    window_sum = 7 - 1 = 6, left = 3.

Sixth Iteration (right = 5):
    right = 5, arr[right] = 3
    window_sum = 6 + 3 = 9
    Now, window_sum >= S, so we update:
    min_length = min(3, 5 - 3 + 1) = 3.
    We shrink the window by subtracting arr[left] = 2:
    window_sum = 9 - 2 = 7, left = 4.
    Again, window_sum >= S, so we update:
    min_length = min(3, 5 - 4 + 1) = 2.

Final Result:
    The smallest subarray that has a sum >= S = 7 is [4, 3] with a length of 2.


'''