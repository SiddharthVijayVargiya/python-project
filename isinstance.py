# Checking if a variable is of a specific type
num = 5.5
text = "Hello"
items = [1, 2, 3]

# Check if 'num' is a float
print(isinstance(num, float))  # Output: True

# Check if 'text' is a string
print(isinstance(text, str))  # Output: True

# Check if 'items' is a list
print(isinstance(items, list))  # Output: True

# Check if 'num' is an integer
print(isinstance(num, int))  # Output: False

# Check if 'text' is either a string or a list
print(isinstance(text, (str, list)))  # Output: True
