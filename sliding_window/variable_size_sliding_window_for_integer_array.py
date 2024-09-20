def longest_subarray_with_k_distinct(nums, k):
    # Dictionary to store the frequency of integers in the current window
    num_count = {}

    # Initialize the left pointer and the max length of valid subarray
    left = 0
    max_len = 0

    # The right pointer expands the window
    for right in range(len(nums)):
        num = nums[right]
        # Include the current number into the window
        num_count[num] = num_count.get(num, 0) + 1

        # If the number of distinct integers exceeds 'k', shrink the window
        while len(num_count) > k: 
            left_num = nums[left]
            # Decrease the count of the leftmost number
            num_count[left_num] -= 1
            # If its count drops to 0, remove it from the dictionary
            if num_count[left_num] == 0:
                del num_count[left_num]
            # Move the left pointer to shrink the window
            left += 1

        # Calculate the maximum length of the valid window
        max_len = max(max_len, right - left + 1)

    # Return the maximum length of a valid subarray with at most 'k' distinct integers
    return max_len

# Example usage:
nums = [1, 2, 1, 2, 3]
k = 2
print(longest_subarray_with_k_distinct(nums, k))  # Output: 4 (subarray [1, 2, 1, 2])
