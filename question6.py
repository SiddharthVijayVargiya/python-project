class Solution:
    def reverse(self, x: int) -> int:
        # Step 1: Determine the sign of the input integer
        # If the number is negative (x < 0), set sign to -1, otherwise set it to 1 (for positive numbers)
        sign = -1 if x < 0 else 1
        
        # Step 2: Reverse the digits of the absolute value of the number
        # abs(x) gives the absolute value (positive part) of x
        # str(abs(x)) converts the absolute value to a string, so we can reverse it
        # [::-1] is slicing notation that reverses the string
        # int() converts the reversed string back into an integer
        rev = int(str(abs(x))[::-1])
        
        # Step 3: Restore the original sign
        # Multiply the reversed integer by the sign (-1 or 1) to make it negative or positive as needed
        rev *= sign
        
        # Step 4: Check for overflow in the 32-bit signed integer range
        # The valid range for a 32-bit signed integer is from -2^31 to 2^31 - 1
        # If the reversed number is within the valid range, return it
        # If the reversed number is outside this range, return 0 to signify overflow
        return rev if -2**31 <= rev <= 2**31 - 1 else 0
