#Matplotlib is a low level graph plotting library in python that serves as a visualization utility.

#Draw a line in a diagram from position (0,0) to position (6,250):
import matplotlib.pyplot as plt
import numpy as np
x_points=np.array([0,6])
y_points=np.array([0,250])
plt.plot(x_points,y_points)
plt.show()