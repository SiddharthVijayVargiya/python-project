"""


    Function to find the maximum sum of any subarray of size 'k' 
    in the given array.

    Parameters:
    arr (list): Input array of integers
    k (int): Size of the subarray

    Returns:
    int: Maximum sum of any subarray of size 'k'
    
    
"""



def max_sum_fixed_window(arr, k):

    # Calculate the initial sum of the first 'k' elements
    curr_sum = sum(arr[:k])
    max_sum = curr_sum
    
    # Slide the window across the array
    for i in range(k, len(arr)):
        # Add the next element to the current sum
        curr_sum += arr[i]
        # Remove the element that is no longer in the window
        curr_sum -= arr[i - k]
        # If the current sum is bigger than the previous max, update max_sum
        if curr_sum > max_sum:
            max_sum = curr_sum
            
    return max_sum

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8]
k = 4
print(max_sum_fixed_window(arr, k))  # Output will be 26
'''
Detailed Example:

Initial Window:

Window: [1, 2, 3, 4]
curr_sum = 10
max_sum = 10
First Slide:

New Window: [2, 3, 4, 5]
curr_sum = 10 + 5 - 1 = 14
max_sum = max(10, 14) = 14
Second Slide:

New Window: [3, 4, 5, 6]
curr_sum = 14 + 6 - 2 = 18
max_sum = max(14, 18) = 18
Third Slide:

New Window: [4, 5, 6, 7]
curr_sum = 18 + 7 - 3 = 22
max_sum = max(18, 22) = 22
Fourth Slide:

New Window: [5, 6, 7, 8]
curr_sum = 22 + 8 - 4 = 26
max_sum = max(22, 26) = 26
Final Result:

Maximum sum of any subarray of size k = 4 is 26.

'''