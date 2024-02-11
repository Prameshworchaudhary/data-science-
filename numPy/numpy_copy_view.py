#The Difference Between Copy and View
#The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.
#copy
import numpy as np
arr=np.array([1,2,3,4,5])
a=arr.copy()
arr[0]=60
print(arr)
print(a)

#view
#Make a view, change the original array, and display both arrays:
arr=np.array([1,2,3,4,5])
a=arr.view()
arr[0]=60
print(arr)
print(a)

#Check if Array Owns its Data
#Print the value of the base attribute to check if an array owns it's data or not:
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()
print(x.base)  #return none
print(y.base)  #return the arr value