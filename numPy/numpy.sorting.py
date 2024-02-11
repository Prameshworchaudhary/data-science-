#Sorting Arrays
#Sorting means putting elements in an ordered sequence.
#Ordered sequence is any sequence that has an order corresponding to elements, like numeric or alphabetical, ascending or descending.
#The NumPy ndarray object has a function called sort(), that will sort a specified array.

import numpy as np
arr=np.array([5,4,3,2,1,0])
print(np.sort(arr))

arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))

arr = np.array([True, False, True])
print(np.sort(arr))

arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))