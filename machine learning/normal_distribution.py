#Normal Data Distribution
import numpy as np
import matplotlib.pyplot as plt

x=np.random.normal(0.0,5.0,10000)
print(x)
plt.hist(x,100)
plt.show()