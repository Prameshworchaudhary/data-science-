#Markers
#You can use the keyword argument marker to emphasize each point with a specified marker:
import matplotlib.pyplot as plt
import numpy as np

ypoint=np.array([1,9,3,7,5])
plt.plot(ypoint,marker='o')
plt.show()

#You can also use the shortcut string notation parameter to specify the marker.
#This parameter is also called fmt, and is written with this syntax:
#marker|line|color

ypoint=np.array([1,9,3,7,5])
plt.plot(ypoint,'o:r') #marker='o' , : = dotted line and color=red
plt.show()

plt.plot(ypoint,'*--g') #marker='*' , -- = dashed line and color=green
plt.show()

#Marker Size
#You can use the keyword argument markersize or the shorter version, ms to set the size of the markers:
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20)
plt.show()

#Marker Color
#You can use the keyword argument markeredgecolor or the shorter mec to set the color of the edge of the makers

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
plt.show()

#You can use the keyword argument markerfacecolor or the shorter mfc to set the color inside the edge of the makersypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
plt.show()

#use of mec and mfc

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mfc = 'g')
plt.show()
