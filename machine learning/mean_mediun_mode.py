#Mean, Median, and Mode
"""
Mean - The average value
Median - The mid point value
Mode - The most common value
"""
import numpy as np
speed=[99,89,87,67,89,87,78,77,88,87,68,93]
mean=np.mean(speed)
print("mean is ",mean)
#median
median=np.median(speed)
print("median is ",median)

#mode
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = stats.mode(speed)

print(x)