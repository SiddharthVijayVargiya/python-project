def matrix_multiplication(m1, m2):
    m1r = len(m1)        # Number of rows in matrix 1
    m1c = len(m1[0])     # Number of columns in matrix 1
    
    m2r = len(m2)        # Number of rows in matrix 2
    m2c = len(m2[0])     # Number of columns in matrix 2
    
    # Check if matrix multiplication is possible
    if m1c != m2r:
        return "Matrix multiplication is not valid due to dimension mismatch."
    
    # Initialize result matrix with zeros (with dimensions m1r x m2c)
    result = [[0 for _ in range(m2c)] for _ in range(m1r)]
    
    # Perform matrix multiplication
    for i in range(m1r):          # Iterate over the rows of m1
        for j in range(m2c):      # Iterate over the columns of m2
            for k in range(m1c):  # or m2r (since m1c == m2r)
                result[i][j] += m1[i][k] * m2[k][j]
    
    return result

# Example usage:
m1 = [
    [1, 2],
    [3, 4],
    [5, 6]
]

m2 = [
    [7, 8, 9],
    [10, 11, 12]
]

result = matrix_multiplication(m1, m2)

for row in result:
    print(row)










'''
so reason why we take K is we want 
something common reference in both matrix am i right 
?
'''


'''
Yes, you're absolutely right!

The reason we introduce k in matrix multiplication is that we need a common reference
between the two matrices for the multiplication process. Specifically:

The k index allows us to pair elements from a row of matrix A with elements from a column of matrix B.
In each step, A[i][k] refers to an element in the i-th row of A, and B[k][j] refers to an element in the j-th column of B.
Since the number of columns in A must match the number of rows in B, k is the shared dimension, acting as a "bridge" 
for combining elements from these two matrices. The third loop over k ensures we multiply all corresponding pairs and
then sum them to compute the resulting element.

So yes, k serves as the common reference that allows the row of A and the column of B to align for proper multiplication!


'''