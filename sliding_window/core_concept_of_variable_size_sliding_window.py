#Core concept of variable sliding window in Python


# 1 You have a left pointer and a right pointer.

# 2 The right pointer expands the window by moving forward to include more elements.

# 3 The left pointer shrinks the window when a certain condition is violated.


'''
# 4 Throughout, you keep track of the desired property 
 (like max/min sum, substring with certain constraints, etc.).
'''

'''

Here's a basic example where we find the length of the longest 
substring with at most two 
distinct characters using the variable sliding window approach:


'''

def longest_substring_with_k_distinct(s, k):
    # Dictionary to store the frequency of characters in the window
    char_count = {}
    
    left = 0
    max_len = 0

    # Right pointer expands the window
    for right in range(len(s)):
        char = s[right]
        char_count[char] = char_count.get(char, 0) + 1

        # Shrink the window if we have more than k distinct characters
        while len(char_count) > k:
            left_char = s[left]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]
            left += 1

        # Update the maximum length of the valid window
        max_len = max(max_len, right - left + 1)

    return max_len

# Example usage:
s = "eceba"
k = 2
print(longest_substring_with_k_distinct(s, k))  # Output: 3 (substring "ece")

'''

Explanation:
The window expands by moving right to include more characters.
Whenever the window has more than k distinct characters, 
the window is shrunk by moving left until it satisfies the condition again.
The goal is to find the maximum valid window size.
This approach ensures an efficient solution with a time complexity of O(n).



'''