'''
Problem: Nested Dictionary from List of Tuples
Given a list of tuples, where each tuple contains
three elements: a category, an item, and a value, 
write a function that transforms this list into a 
nested dictionary. 
The structure of the dictionary should be as follows:

The outer dictionary has categories as keys.
Each category maps to an inner dictionary.
The inner dictionary has items as keys.
Each item maps to its corresponding value.
Input:
python
Copy code
data = [
    ('fruit', 'apple', 10),
    ('fruit', 'banana', 5),
    ('vegetable', 'carrot', 7),
    ('fruit', 'orange', 8),
    ('vegetable', 'broccoli', 12),
    ('grain', 'rice', 20)
]
Expected Output:
python
Copy code
{
    'fruit': {
        'apple': 10,
        'banana': 5,
        'orange': 8
    },
    'vegetable': {
        'carrot': 7,
        'broccoli': 12
    },
    'grain': {
        'rice': 20
    }
}
Requirements:
Use dictionary and list comprehensions to create the nested dictionary.
Avoid using any loops (like for or while loops) directly; 
instead, rely solely on comprehensions.
Hint:
Consider using a dictionary comprehension 
that iterates over the unique categories,
and for each category, use another dictionary comprehension to 
build the inner dictionary.

Bonus Challenge: Modify the solution to sum the values if 
there are multiple entries for the same item under the same category.'''


