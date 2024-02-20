#A simple way to store big data sets is to use CSV files (comma separated files).
#CSV files contains plain text and is a well know format that can be read by everyone including Pandas.

#in example download this -> Download data.csv.
import pandas as pd
df = pd.read_csv('data.csv')

print(df.to_string()) 

#Print the DataFrame without the to_string() method:

df = pd.read_csv('data.csv')

print(df)