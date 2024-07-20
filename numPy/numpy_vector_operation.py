import numpy as np 

v1=np.array([1,2,3])
v2=np.array([4,5,6])

addition = v1+v2

# Scalar Multiplication
scalar = 3
scalar_multiplication = scalar * v1

# Dot Product
dot_product = np.dot(v1, v2)

# Cross Product (only for 3D vectors)
cross_product = np.cross(v1, v2)

print("Vector Addition:", addition)
print("Scalar Multiplication:", scalar_multiplication)
print("Dot Product:", dot_product)
print("Cross Product:", cross_product)

