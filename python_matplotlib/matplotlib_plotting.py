#The plot() function is used to draw points (markers) in a diagram.
#By default, the plot() function draws a line from point to point.

import matplotlib.pyplot as plt
import numpy as np

x_point=np.array([1,8])
y_point=np.array([2,15])

plt.plot(x_point,y_point)
plt.show()

#Plotting Without Line
#To plot only the markers, you can use shortcut string notation parameter 'o', which means 'rings'.
x_point=np.array([1,8])
y_point=np.array([2,15])

plt.plot(x_point,y_point,'o')
plt.show()

#Multiple Points
#You can plot as many points as you like, just make sure you have the same number of points in both axis.

x_point=np.array([2,4,6,8,10])
y_point=np.array([12,5,10,1,15])

plt.plot(x_point,y_point)
plt.show()

#Default X-Points
#If we do not specify the points on the x-axis, they will get the default values 0, 1, 2, 3 etc., depending on the length of the y-points.
y_point=np.array([12,6,14,4,15])

plt.plot(y_point)
plt.show()