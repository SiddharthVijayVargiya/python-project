squares = [x * 2 for x in range(1, 6)]
print(squares)  # Output: [2, 4, 6, 8, 10]




even_squares = [x * 2 for x in range(1, 6) if x % 2 == 0]
print(even_squares)  # Output: [4, 8]




pairs = [(x, y) for x in range(1, 3) for y in range(4, 6)]
print(pairs)  # Output: [(1, 4), (1, 5), (2, 4), (2, 5)]

 


nums = [1, 2, 3, 4, 5]
result = ["even" if x % 2 == 0 else "odd" for x in nums]
print(result)  # Output: ['odd', 'even', 'odd', 'even', 'odd']



nested_list = [[1, 2], [3, 4], [5, 6]]
flattened_list = [item 
                  for sublist in nested_list #outer loop
                  for item in sublist] #inner loop
print(flattened_list)  # Output: [1, 2, 3, 4, 5, 6]
'''In a list comprehension, the outer loop 
should come first (for sublist), 
followed by the inner loop (for item in sublist).'''



nums = [1, 2, 3, 4]
squared_dict = {x: x**2 for x in nums}
print(squared_dict)  # Output: {1: 1, 2: 4, 3: 9, 4: 16}



nums = [1, 2, 2, 3, 4, 4, 5]
unique_squares = {x**2 for x in nums}#SET_COMPREHENSION 
print(unique_squares)  # Output: {1, 4, 9, 16, 25}# set use for removing removes duplicate

'''[expression for item in iterable if condition1 and condition2 and ...]
'''
students = [['Alice', 85], ['Bob', 90], ['Charlie', 75], ['David', 65]]
filtered_students = [student 
                     for student in students 
                     if student[1] > 70 and student[1] < 90]

print(filtered_students)
'''[['Alice', 85], ['Charlie', 75]]
'''



'''List Comprehension with a Filter Condition:
Syntax: [expression for item in iterable if condition]

Purpose: Filters the elements of the iterable 
based on the condition
before applying the expression.

Example: Extract words that contain the letter 'z':

python
Copy code
words_with_z = [word for word in words if 'z' in word]
This will create a new list containing 
only the words that have 'z'.

2. List Comprehension with a Conditional Expression:
Syntax: [expression1 if condition else expression2 
for item in iterable]

Purpose: Applies expression1 if the condition is True,
otherwise applies expression2. This doesn’t filter 
out elements but 
rather transforms them based on the condition.

Example: Replace words that contain the letter 'z'
with "contains_z":'''