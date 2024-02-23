#To create big data sets for testing, we use the Python module NumPy, which comes with a number of methods to create random data sets, of any size.
#Create an array containing 250 random floats between 0 and 5:
import numpy as np 
import matplotlib.pyplot as plt
x=np.random.uniform(0.0,5.0,250)
print(x)
plt.hist(x,5)
plt.show()

#Big Data Distributions
y=np.random.uniform(0.0,5.0,100000)
plt.hist(y,5)
plt.show()