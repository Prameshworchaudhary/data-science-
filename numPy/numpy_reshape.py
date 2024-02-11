#Reshaping arrays
#Reshaping means changing the shape of an array.
#The shape of an array is the number of elements in each dimension.
#By reshaping we can add or remove dimensions or change number of elements in each dimension.

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)

#Convert the following 1-D array with 12 elements into a 3-D array.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr)

#Flattening the arrays
#Flattening array means converting a multidimensional array into a 1D array.
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)
