import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)

arr1=np.array((1,2,3,4,5,6))
print(arr1)

#dimensions
#zero dimensions
#A dimension in arrays is one level of array depth (nested arrays).
#nested array: are arrays that have arrays as their elements.
#0-d array
zero_arr=np.array(45)
print(zero_arr)

#1-d array
#An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.
arr=np.array(["a","b","c","d","e"])
print(arr)

#2-D Arrays
#An array that has 1-D arrays as its elements is called a 2-D array.

arr=np.array([[1,2,3],[4,5,6]])
print(arr)

#3-D arrays
#An array that has 2-D arrays (matrices) as its elements is called 3-D array.
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)

#Check Number of Dimensions?
#NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])


print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

#indexing array
arr=np.array([1,2,3,4,5])
print(arr[0])
print(arr[4])
print(arr[3])


