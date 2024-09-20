'''
The enumerate() function in Python is used when you want to
loop over an iterable (like a list or tuple) and need to keep
track of both the index and the value of each item in the iterable.
It returns a tuple 
containing the index and the corresponding item from the iterable.
'''

# enumerate(iterable, start=0)

'''
iterable: Any iterable object (like a list, tuple, or string).
start (optional): The starting index value (default is 0).


'''



'''
Common Use Cases:
1 Looping over a list with both the index and item.
2 Modifying items in a list based on their index.
3 Converting an iterable to a dictionary with index as the key

'''

fruits = ['apple', 'banana', 'cherry']

# Using enumerate() to get index and value
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

'''
Index 0: apple
Index 1: banana
Index 2: cherry
'''

fruits = ['apple', 'banana', 'cherry']

# Start index from 1 instead of 0
for index, fruit in enumerate(fruits, start=1):
    print(f"Index {index}: {fruit}")
'''
Index 1: apple
Index 2: banana
Index 3: cherry


'''

message = "hello"

# Enumerating over characters in a string
for index, char in enumerate(message):
    print(f"Character at position {index}: {char}")
'''
Character at position 0: h
Character at position 1: e
Character at position 2: l
Character at position 3: l
Character at position 4: o
'''

names = ['Alice', 'Bob', 'Charlie']

# Create a dictionary using enumerate()
name_dict = {index: name for index, name in enumerate(names, start=1)}
print(name_dict)
'''
{1: 'Alice', 2: 'Bob', 3: 'Charlie'}
'''

numbers = [10, 20, 30, 40]

# Update items based on their index
for index, number in enumerate(numbers):
    numbers[index] = number * 2

print(numbers)
'''
[20, 40, 60, 80]
'''
colors = ('red', 'green', 'blue')

# Enumerating over a tuple
for index, color in enumerate(colors):
    print(f"Color at index {index}: {color}")
'''
Color at index 0: red
Color at index 1: green
Color at index 2: blue
'''
# Multiply each element in the list by its index
numbers = [2, 4, 6, 8]
result = [index * num for index, num in enumerate(numbers)]
print(result)
'''
[0, 4, 12, 24]

'''

'''
Conclusion:
The enumerate() function is particularly
useful when you need both the index and the value
while iterating over an iterable. It simplifies the process
of manually managing a counter or index in loops and makes the
code more readable.

'''