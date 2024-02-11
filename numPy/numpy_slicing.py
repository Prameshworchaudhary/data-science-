#Slicing
#Slicing in python means taking elements from one given index to another given index.
#We pass slice instead of index like this: [start:end].
#We can also define the step, like this: [start:end:step].

import numpy as np

arr= np.array([1,2,3,4,5,6])
print(arr[1:3])
print(arr[4:])
print(arr[:5])

#negative slicing
#Use the minus operator to refer to an index from the end:
print(arr[-4:-1])
print(arr[-5:-1])

#Use the step value to determine the step of the slicing:
print(arr[0:5:2])

#2-d array
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1:4])