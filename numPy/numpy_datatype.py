#Data Types in Python
#By default Python have these data types:

#strings - used to represent text data, the text is given under quote marks. e.g. "ABCD"
#integer - used to represent integer numbers. e.g. -1, -2, -3
#float - used to represent real numbers. e.g. 1.2, 42.42
#boolean - used to represent True or False.
#complex - used to represent complex numbers. e.g. 1.0 + 2.0j, 1.5 + 2.5j

#The NumPy array object has a property called dtype that returns the data type of the array:

import numpy as np
arr=np.array([1,2,3])
print(arr.dtype)
arr=np.array(["apple","banana","orange"])
print(arr.dtype)
