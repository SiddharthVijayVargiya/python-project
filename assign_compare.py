'''
These expressions relate to how conditions and 
operations are evaluated in Python, 
especially when checking for divisibility and 
performing division. Let's break down each one:

1. VALUE % 3 = 0
Explanation: This is not valid syntax in Python. 
The single equals sign (=) is used for 
assignment, not for comparison. 
This line would raise a SyntaxError 
because Python expects a comparison operator (==) instead 
of an assignment 
in a conditional statement.
2. VALUE % 3 == 0
Explanation: This checks if the
remainder when VALUE is divided by 3 is 0. 
If VALUE is divisible by 3, this condition evaluates to True.
Use Case: This is the correct
way to check if a number is divisible by 3. 
For example, 9 % 3 == 0 returns True 
because 9 is divisible by 3.
3. VALUE / 3 = 0
Explanation: This is also not valid syntax in Python. 
The single equals sign (=) is used for assignment, not comparison. 
This line would raise a SyntaxError 
because you're trying to assign a 
value to a result of a division, which is not allowed.
4. VALUE / 3 == 0
Explanation: This checks if the result of dividing 
VALUE by 3 is exactly 0.
Use Case: This is generally not 
useful when checking for divisibility.
For example, 9 / 3 == 0 would evaluate to
False because 9 / 3 equals 3, not 0. 
You should not use this to check for divisibility.
Correct Usage:
To check if a number is divisible by 3: Use VALUE % 3 == 0.
To check if the result of division is zero:
This typically wouldn't be used for divisibility checks. 
Instead, it's used to confirm if the result of division 
by 3 gives exactly zero (which usually doesn’t make 
sense unless VALUE is 0).
For divisibility checks, always go with the modulus
operator (%), like in the VALUE % 3 == 0 example.
'''