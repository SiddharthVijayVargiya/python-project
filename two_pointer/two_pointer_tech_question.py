#Given a sorted array arr = [1, 2, 3, 4, 6, 8] and a target sum 10, 
#use the two-pointer 
#technique to find a pair of elements that add up to the target.
def sort_array(arr):
    left = 0
    right = len(arr) - 1
    
    # Loop until left pointer meets or crosses right pointer
    while left < right:
        # Calculate the sum of the values at the two pointers
        current_sum = arr[left] + arr[right]
        
        # If the sum is 10, return the pair
        if current_sum == 10:
            return (arr[left], arr[right])
        
        # If sum is less than 10, move the left pointer to the right to increase the sum
        elif current_sum < 10:
            left += 1
        
        # If sum is greater than 10, move the right pointer to the left to decrease the sum
        else:
            right -= 1
    
    # If no pair found, return False
    return False

# Test with the array
arr = [1, 2, 3, 4, 6, 8]
x = sort_array(arr)
print(x)  # Output will be (2, 8) because 2 + 8 = 10



#Q7. Container With Most Water:
# Given an array of non-negative integers where each element represents the height of a
# vertical line on the x-axis, use the two-pointer technique to find two lines that together
# with the x-axis form a container that holds the most water.
# Example: heights = [1,8,6,2,5,4,8,3,7]


def max_area(heights):
    left = 0
    right = len(heights) - 1
    max_water = 0
    
    # Loop until the two pointers meet
    while left < right:
        # Calculate the width between the two pointers
        width = right - left
        
        # Calculate the area with the current left and right pointers
        current_water = min(heights[left], heights[right]) * width
        
        # Update max_water if the current area is larger
        max_water = max(max_water, current_water)
        
        # Move the pointer corresponding to the shorter line
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    
    return max_water

# Example test case
heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
result = max_area(heights)
print(result)  # Output: 49
