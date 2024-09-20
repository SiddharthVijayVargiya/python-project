'''
You have a list of strings containing various words. 
Write a Python code that iterates through the list, 
checks if any word contains the letter 'z', and if so, 
replaces that word with the string "contains_z".
'''
words =['aaaaa','zzzzzzz','lzlzl','z']
x = ['contains_z'
     if 'z' in word 
     else word 
     for word in words ]
print(x)

'''
Question:
You have a list of integers.
Write a Python code that iterates through 
the list and replaces every multiple of 3 with the 
string "multiple_of_3".
'''
numbers =[]
for _ in range(int(input())):
    value = int(input())
    numbers.append(value)
print(numbers)
y = ['multiple_of_3' if value%3 == 0 else value for value in numbers]
print(y)

'''
Question:
You want to iterate through a list of numbers and check if any number is greater than 100. 
If a number is greater than 100, replace it with the string "large". 
How can you achieve this in Python?'''


numbers = []
for _ in range(int(input())):
    number = int(input())
    numbers.append(number)
z = ['large' if number > 100 else number for number in numbers]
print(z)    

'''
Question:
Given a list of names, 
write a Python code that replaces any name longer than 5 characters with the string "long_name".
'''
names = []
for _ in range(int(input())):
    name = input()
    names.append(name)
a = ['long_name' if len(name)> 5 else name for name in names]
print(a)    





'''
Question:
You have a list of mixed data types (integers, strings, and floats).
Write a Python code that iterates through the list and replaces all float values with the string "float_value".
'''

# Initialize an empty list to store mixed data types
info = []

# Get the number of inputs from the user
num_inputs = int(input("Enter the number of elements: "))

# Populate the list with mixed data types
for _ in range(num_inputs):
    mdt = input("Enter a value (could be int, str, or float): ")
    
    # Try to convert the input to an integer or float if possible
    try:
        if '.' in mdt:
            mdt = float(mdt)
        else:
            mdt = int(mdt)
    except ValueError:
        pass  # Leave the input as a string if it's neither int nor float
    
    # Append the value to the list
    info.append(mdt)

# Replace all float values in the list with the string "float_value"
b = ["float_value" if isinstance(value, float) else value for value in info]

print(b)
