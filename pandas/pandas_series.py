#A Pandas Series is like a column in a table.
#It is a one-dimensional array holding data of any type.
import pandas as pd
x=[4,5,6]
y=pd.Series(x)
print(y)
print(y[2])

calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)