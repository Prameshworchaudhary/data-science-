#The Normal Distribution is one of the most important distributions.
#It fits the probability distribution of many events, eg. IQ Scores, Heartbeat etc.
#Use the random.normal() method to get a Normal Data Distribution.
#
from numpy import random
x=random.normal(size=(2,3))
print(x)
#three parameter
#loc - (Mean) where the peak of the bell exists.
#scale - (Standard Deviation) how flat the graph distribution should be.
#size - The shape of the returned array.
y=random.normal(loc=1,scale=2,size=(2,3))
print(y)

#Visualization of Normal Distribution
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.normal(size=1000), hist=False)
plt.show()