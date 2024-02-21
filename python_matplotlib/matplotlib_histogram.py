#A histogram is a graph showing frequency distributions.

import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)
print(x)

plt.hist(x)
plt.show() 