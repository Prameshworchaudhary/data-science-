#You can use the keyword argument linestyle, or shorter ls, to change the style of the plotted line:

import matplotlib.pyplot as plt
import numpy as np

ypoint=np.array([6,3,8,5])

plt.plot(ypoint, linestyle='dotted')
plt.show()

#color as c 

ypoint=np.array([6,3,8,5])

plt.plot(ypoint,c= 'r',linestyle='dotted')
plt.show()

# line width
#the keyword argument linewidth or the shorter lw to change the width of the line.
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linewidth = '20.5')
plt.show()

#multiple line

y1=np.array([6,3,9,4])
y2=np.array([3,6,4,9])

plt.plot(y1)
plt.plot(y2)
plt.show()

#Draw two lines by specifiyng the x- and y-point values for both lines:
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()