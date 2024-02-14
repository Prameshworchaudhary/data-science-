#Exponential Distribution
#Exponential distribution is used for describing time till next event e.g. failure/success etc.
#It has two parameters:
#scale - inverse of rate ( see lam in poisson distribution ) defaults to 1.0.
#size - The shape of the returned array.
from numpy import random
x=random.exponential(scale=1,size=(2,3))
print(x)

#Visualization of Exponential Distribution
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.exponential(size=1000), hist=False)
plt.show()