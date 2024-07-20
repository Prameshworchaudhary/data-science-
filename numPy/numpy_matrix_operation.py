import numpy as np

# Define two matrices
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

# Matrix Addition
matrix_addition = A + B

# Scalar Multiplication
scalar = 2
scalar_multiplication_matrix = scalar * A

# Matrix Multiplication
matrix_multiplication = np.dot(A, B)

# Transpose
transpose = np.transpose(A)

# Determinant
determinant = np.linalg.det(A)

# Inverse (if the matrix is invertible)
# Note: A should be a square matrix and invertible
# The example matrix A here is singular (not invertible), so let's use another example
A_inv = np.array([[1, 2],
                  [3, 4]])

inverse = np.linalg.inv(A_inv)

print("Matrix Addition:\n", matrix_addition)
print("Scalar Multiplication:\n", scalar_multiplication_matrix)
print("Matrix Multiplication:\n", matrix_multiplication)
print("Transpose:\n", transpose)
print("Determinant:", determinant)
print("Inverse:\n", inverse)