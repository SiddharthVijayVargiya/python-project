'''
1. Reversing a string or list:
Simple reversal using [::-1]:
'''
s = "Python"
print(s[::-1])  # Output: nohtyP


'''
Skipping elements (every second item):
Slicing with a step to skip elements.
'''
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lst[::2])  # Output: [0, 2, 4, 6, 8]

'''
Extracting elements in reverse order but skipping some:
You can reverse the sequence and also skip elements using a negative step.
'''
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lst[::-2])  # Output: [9, 7, 5, 3, 1]
'''
Slicing with a negative start and stop:
Negative indices allow slicing from the end of a sequence.
'''
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lst[-8:-2])  # Output: [2, 3, 4, 5, 6, 7]


'''
Reversing part of a list:
Reverse only a portion of the list.
'''
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lst[2:7][::-1])  # Output: [6, 5, 4, 3, 2]


'''
Multiple steps within a sublist:
Slice a portion with skips inside.

'''
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lst[1:8:3])  # Output: [1, 4, 7]

'''
Using out-of-bound indices:
Slicing gracefully handles out-of-bound indices without throwing errors.
'''
lst = [1, 2, 3]
print(lst[1:100])  # Output: [2, 3]

'''
Reverse only the last n elements:
Reverse just the last 3 elements of the list.
'''
lst = [1, 2, 3, 4, 5, 6, 7]
print(lst[:-4:-1])  # Output: [7, 6, 5]


'''
Manipulating two slices together:
Join the results of two slices.
'''
lst = [1, 2, 3, 4, 5, 6, 7]
print(lst[:3] + lst[5:])  # Output: [1, 2, 3, 6, 7]


'''
Setting values using slicing:
You can modify parts of a list using slicing.
'''
lst = [1, 2, 3, 4, 5]
lst[1:4] = [10, 20, 30]  # Replace index 1 to 3
print(lst)  # Output: [1, 10, 20, 30, 5]

'''
Reversing a string from a specific position:
Reverse the string but only starting from a certain index.
'''
s = "abcdefgh"
print(s[:3] + s[3:][::-1])  # Output: abchedg

'''
Extracting the last n elements in reverse:
A concise way to get the last n elements in reverse order.
'''
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lst[:-4:-1])  # Output: [9, 8, 7]


'''
Skipping elements in reverse:
Slicing backwards while skipping elements.
'''

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lst[8:2:-2])  # Output: [9, 7, 5]


'''
Mirroring the list:
Create a mirrored version of a list.
'''

lst = [1, 2, 3, 4]
print(lst + lst[::-1])  # Output: [1, 2, 3, 4, 4, 3, 2, 1]


'''
Duplicating every element in a list:
Use slicing to repeat each element in a list.
'''
lst = [1, 2, 3]
print([item for item in lst for _ in (0, 1)])  # Output: [1, 1, 2, 2, 3, 3]


'''
Extracting every second element starting from the second one:
Skip every other element starting from index 1.
'''

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(lst[1::2])  # Output: [1, 3, 5, 7]
'''
Extracting a sublist in reverse starting at a specific index:
You can reverse slice starting at an arbitrary point.
'''

lst = [10, 20, 30, 40, 50, 60, 70]
print(lst[5:1:-1])  # Output: [60, 50, 40, 30]
'''
Swapping halves of a list:
Swap the first and second halves of a list.
'''
lst = [1, 2, 3, 4, 5, 6]
mid = len(lst) // 2
print(lst[mid:] + lst[:mid])  # Output: [4, 5, 6, 1, 2, 3]


'''
Rotating a list using slicing:
Perform a simple list rotation by n elements.
'''
lst = [1, 2, 3, 4, 5]
n = 2  # Rotate by 2 elements
print(lst[n:] + lst[:n])  # Output: [3, 4, 5, 1, 2]
'''
Extract elements from the middle:
Get elements from the middle of the list, leaving out the first and last n elements.
'''

lst = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(lst[2:-2])  # Output: [30, 40, 50, 60, 70]
'''
Slicing with a negative step and custom bounds:
Extract elements from a range and reverse them with a step.

'''
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lst[8:1:-3])  # Output: [8, 5, 2]
'''
Reversing odd indexed elements only:
Keep even indexed elements in place, but reverse only the odd indexed ones.
'''
lst = [1, 2, 3, 4, 5, 6, 7, 8]
print(lst[::2] + lst[1::2][::-1])  # Output: [1, 3, 5, 7, 8, 6, 4, 2]
'''
Replacing part of a string using slicing:
You can replace a specific part of a string.

'''
s = "abcdefgh"
new_s = s[:3] + "XYZ" + s[6:]
print(new_s)  # Output: abcXYZgh
'''
Alternating between two lists using slicing:
Merge two lists by alternating their elements.
'''

a = [1, 3, 5, 7]
b = [2, 4, 6, 8]
combined = [None]*(len(a)+len(b))
combined[::2], combined[1::2] = a, b
print(combined)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
'''
Removing all odd-indexed elements:
Easily remove all elements at odd indices.
'''
lst = [10, 20, 30, 40, 50, 60, 70, 80]
print(lst[::2])  # Output: [10, 30, 50, 70]
'''
Extracting alternating elements in reverse order:
Extract every alternate element starting from the last element and go backwards.

'''
lst = [1, 2, 3, 4, 5, 6, 7, 8]
print(lst[::-2])  # Output: [8, 6, 4, 2]



'''
Modifying part of a list using slicing:
Replace part of the list with new values.
'''

lst = [1, 2, 3, 4, 5]
lst[1:3] = [9, 8]  # Replace elements at indices 1 and 2
print(lst)  # Output: [1, 9, 8, 4, 5]


'''
Inserting elements using slicing:
Insert new elements into a list at a specific position.
'''
lst = [1, 2, 3, 7, 8]
lst[3:3] = [4, 5, 6]  # Insert before index 3
print(lst)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]


'''
 Removing elements using slicing:
You can use slicing to remove elements from a list.

'''
lst = [1, 2, 3, 4, 5]
del lst[1:4]  # Remove elements at index 1 to 3
print(lst)  # Output: [1, 5]


'''
Extracting a sublist with a custom step:
Use slicing to extract a sublist but skip elements according to a custom step.
'''
lst = [1, 2, 3, 4, 5, 6, 7, 8]
print(lst[1:7:2])  # Output: [2, 4, 6]
'''
Reverse every other element in a sublist:
Extract and reverse alternate elements within a sublist.
'''
lst = [1, 2, 3, 4, 5, 6, 7, 8]
print(lst[::2][::-1])  # Output: [7, 5, 3, 1]
'''
Extract the middle element of a list:
For odd-length lists, you can extract the exact middle element.
'''
lst = [1, 2, 3, 4, 5]
middle = len(lst) // 2
print(lst[middle])  # Output: 3



'''
 Circular shift (rotating elements):
Perform a circular shift of elements by slicing and concatenating.
'''
lst = [1, 2, 3, 4, 5]
n = 2  # Number of elements to rotate
print(lst[n:] + lst[:n])  # Output: [3, 4, 5, 1, 2]


'''
Reversing a tuple:
You can reverse a tuple just like a list using slicing.

'''
t = (1, 2, 3, 4, 5)
print(t[::-1])  # Output: (5, 4, 3, 2, 1)
'''
Extracting the last n elements and reversing them:
Get the last n elements in reverse.

'''

lst = [1, 2, 3, 4, 5, 6, 7]
print(lst[:-4:-1])  # Output: [7, 6, 5]


'''
Combining two lists with alternating elements:
Combine elements from two lists in an alternating pattern.
'''

a = [1, 3, 5]
b = [2, 4, 6]
combined = [None]*(len(a)+len(b))
combined[::2], combined[1::2] = a, b
print(combined)  # Output: [1, 2, 3, 4, 5, 6]


'''

Extracting elements with both positive and negative steps:
Mix positive and negative steps to extract specific patterns.
'''
lst = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(lst[1:-1:3])  # Output: [20, 50]
print(lst[-2:1:-3])  # Output: [80, 50, 20]
'''
 Selecting every nth element:
Extract every nth element starting from the beginning.
'''
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 3
print(lst[::n])  # Output: [1, 4, 7]
'''
Extracting elements with wrap-around indices:
Slicing with negative indices can create a wrap-around effect.

'''
lst = [1, 2, 3, 4, 5, 6, 7]
print(lst[-3:] + lst[:-3])  # Output: [5, 6, 7, 1, 2, 3, 4]
'''
Split a list into multiple chunks:
Slice a list into smaller sublists of equal size.

'''
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 3  # Size of each chunk
chunks = [lst[i:i+n] for i in range(0, len(lst), n)]
print(chunks)  # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
'''
Remove every nth element:
Use slicing to remove every nth element from the list.
'''
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del lst[::3]  # Removes every 3rd element
print(lst)  # Output: [2, 3, 5, 6, 8, 9]
'''

Rotating elements to the right:
Rotate the elements to the right by a specified number of steps.
'''
lst = [1, 2, 3, 4, 5]
n = 2
print(lst[-n:] + lst[:-n])  # Output: [4, 5, 1, 2, 3]
'''
Extracting elements from the second half of the list:
Get elements from the second half of the list.
'''

lst = [1, 2, 3, 4, 5, 6, 7, 8]
print(lst[len(lst)//2:])  # Output: [5, 6, 7, 8]


'''
Extract a palindrome pattern from a list:
Create a palindrome using slicing and reversing.

'''
lst = [1, 2, 3]
print(lst + lst[::-1])  # Output: [1, 2, 3, 3, 2, 1]
'''
Reverse and alternate:
Combine reversing and alternating between elements.
'''
lst = [1, 2, 3, 4, 5]
print(lst[::-1][::2])  # Output: [5, 3, 1]
