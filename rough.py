'''def smallest_array(arr,s):
    left = 0
    window_sum = 0
    min_length = float('inf')
    for right in range(len(arr)):
        window_sum += arr[right]
        while s<= window_sum:
            min = min(min_length,right-left+1)
    return min_length if min_length != '''
    
'''def smallest_sum(arr, s):
    left = 0
    min_length = float('inf')
    window_sum = 0
    
    for right in range(len(arr)):
        window_sum += arr[right]  # Add the current element to the window sum

        # Shrink the window from the left until window_sum is smaller than s
        while window_sum >= s:
            # Update the minimum length of the subarray
            min_length = min(min_length, right - left + 1)
            window_sum -= arr[left]  # Remove the leftmost element
            left += 1  # Shrink the window by moving the left pointer

    # If no valid window was found, return 0
    return min_length if min_length != float('inf') else 0

# Example usage
arr = [1, 2, 3, 4, 5, 6]
s = 7
print(smallest_sum(arr, s))  # Output: 1 (subarray [7] or [4, 3])'''

'''
def matrix_multiplication(mat1,mat2):
    a_rows = len(mat1)
    a_cols = len(mat1[0])
    b_rows = len(mat2)
    b_cols = len(mat2[0])
    if a_cols != b_cols :
        return f"this matrix is not valid"
    for i in range(a_rows):
        for j in  range(b_cols):
            for k in range(b_rows):
               '''
               
'''def matrix_multiplication(m1,m2):
    m1r = len(m1)
    m1c =  len(m1[0])
    
    m2r = len(m2)
     
    m2c = len(m2[0])
    result = [[0 for _ in range(m2c)] for _ in range(m1r)]

    
    if m1c != m2r:
        return f"this is nt valid"
    for i in range(m1r):
        for j in range(m2c):
            for k in range(m2r):
                result[i][j]+= m1[i][k]*m2[k][j]
    '''
'''def variable_size(arr,k):
    left = 0 
    window_sum =0 
    min_length =float("inf")
    for right in range(len(arr)):
        window_sum += arr[right]
        while window_sum>=k:
            right+=1
            min = min(min_length,right-left+1)
            window_sum -= arr[left]
            left += 1'''
'''def two_Pointer(arr,s):
    left = 0 
    right = len(arr)-1
    while left < right :
        if arr[left] == arr[right]:
            return f"afanmfdakf"
        elif :
            right-=1
        else:
            left +=1'''
'''def binary_search(arr,s):
    left =0
    right =0
    middle_value =len[arr]//2 #odd'''
'''def fibonacci(n):
    if n<1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)
n = 4
print(fibonacci(n))'''
'''arr = ["ababa","abhhh","abfjfjaj","ab","a",""]
def longest_Common_prefix(arr):
    prefix = arr[0]
    for string in arr[:1]:
        while 
    '''
'''def longest_prefix(arr):
    if not arr:
        return ""
    prefix = arr[0]
    for string in arr[1:]:
        while string[:len(prefix)] != prefix and prefix :
            prefix = prefix[:-1]
        if not prefix:
            break
    return prefix
arr = ['aaa','aaannn','aaahaha']
print(longest_prefix(arr))'''
'''def matrix_multiplication(m1,m2):
    m1r = len(m1)
    m1c = len(m1[0])
    m2r = len(m2)
    m2c = len(m2[0])
    result = [[0 for _ in range(m2c)]for _ in range(m2r)]    
    for i in range(m1r):
        for j in range (m2c):
            for k in range(m1c):
                result[i][j] += m1[i][k]*m2[k][j]
    return result
m1 = [[2,2],[2,2]]
m2 = [[2,2],[2,2]]
print(matrix_multiplication(m1,m2))'''
'''arr = ['aaaa','aabbbb','aaaabbb']
def longest_substring_prefix(arr):
    prefix = arr[0]
    if prefix not in arr:
        return
    for string in arr[1:]:
        while string[:len(prefix)] != prefix and prefix :
            prefix = prefix[:-1]
        if not prefix :
            break
    return prefix     
print(longest_substring_prefix(arr))'''
'''for i in range(3):
    for j in range (i+1):
        print("*", end=" ")'''
        
        

'''def variable_sliding_window(arr,k):
    
    left = 0
    window_Sum = 0
    minimum_length = float('inf')
    for right in range(len(arr)):
        window_sum += arr[right]
        while S>= window_Sum:'''
        
'''lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lst[::3])'''
import re
import json

# Function to clean and convert WhatsApp chat to desired format
def parse_whatsapp_chat(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        chat_data = f.readlines()

    conversation = []
    parsed_data = []

    # Regex to match chat lines (adjust based on your chat format)
    message_pattern = re.compile(r"^\d{1,2}/\d{1,2}/\d{2}, \d{1,2}:\d{2} [AP]M - (.*?): (.*)$")
    
    for line in chat_data:
        match = message_pattern.match(line)
        if match:
            sender, message = match.groups()
            
            # Add messages to conversation history
            conversation.append(f"{sender}: {message}")

            # Create a new entry when we have both User and Friend message
            if len(conversation) >= 2:
                parsed_data.append({
                    "conversation": " <sep> ".join(conversation[:-1]),  # conversation history (all but last)
                    "response": conversation[-1]  # the latest response
                })
                conversation = [conversation[-1]]  # Keep the latest message for context
    
    # Save the parsed data to a JSON file
    with open('whatsapp_conversations.json', 'w', encoding='utf-8') as outfile:
        json.dump(parsed_data, outfile, ensure_ascii=False, indent=4)

# Usage
parse_whatsapp_chat('your_whatsapp_chat.txt')
