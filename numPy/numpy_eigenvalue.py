import numpy as np

# Define a square matrix
A = np.array([[4, -2],
              [1, 1]])

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)


print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
