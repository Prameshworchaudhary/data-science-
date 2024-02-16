#Pandas is a Python library used for working with data sets.
#It has functions for analyzing, cleaning, exploring, and manipulating data.
#Why Use Pandas?
#Pandas allows us to analyze big data and make conclusions based on statistical theories.
#Pandas can clean messy data sets, and make them readable and relevant.

import pandas
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
myvar = pandas.DataFrame(mydataset)
print(myvar)

newdata={
     'bike':["hero_honda","pulsar","VR"],
    'price': [100000,200000,3000000]
      }
x=pandas.DataFrame(newdata)
print(x)
