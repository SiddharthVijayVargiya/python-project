def two_sum(nums, target):
    # Initialize an empty dictionary (hash map) to store numbers and their indices
    hash_map = {}
    
    # Iterate over the array, with 'i' as the index and 'num' as the current number
    for i, num in enumerate(nums):
        # Calculate the complement of the current number
        # (complement is the number that, when added to the current number,
        # gives the target sum)
        complement = target - num
        
        # Check if the complement already exists in the hash map
        # If it does, we've found a pair of numbers that add up to the target
        if complement in hash_map:
            # Return the indices of the complement and the current number
            return [hash_map[complement], i]
        
        # If the complement is not found, store the current number in the hash map
        # The key is the current number (num), and the value is its index (i)
        hash_map[num] = i

    # (If no solution is found (which shouldn't 
    # happen based on the problem assumption),)
    # return an empty list as a fallback
    return []

# Example usage
nums = [2, 7, 11, 15]  # The list of numbers
target = 9  # The target sum we're looking for
print(two_sum(nums, target))  
# Output will be [0, 1], since nums[0] + nums[1] = 2 + 7 = 9
'''
Step-by-Step Example (with explanation):
Let’s use the array [2, 7, 11, 15] and 
the target 9 to walk through the logic.

Step 1: Start Iterating Over the Array
Initialize an empty hash map to store 
the numbers we have seen so far.
Step 2: Process the First Number
Current number (num): 2
Calculate the complement: 9 - 2 = 7
Check if the complement (7) is in the hash map: 
It’s not, 
because we haven’t seen any numbers yet.
Store 2 in the hash map with its index (0): {2: 0}
Move to the next number.
Step 3: Process the Second Number
Current number (num): 7
Calculate the complement: 9 - 7 = 2
Check if the complement (2) is in the hash map: Yes, it is! 
We stored 2 in the previous step.
Since 2 is in the hash map, that means:
nums[0] + nums[1] = 2 + 7 = 9
nums[0] + nums[1] = 2 + 7 = 9
So, we’ve found the two numbers (2 and 7) that add up to 9.
Return the indices of 2 and 7, which are [0, 1].
At this point, the algorithm is done. 
We don’t need to check the remaining numbers in the array because
we’ve already found a valid pair.
'''

            
            
            
        