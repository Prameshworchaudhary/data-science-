import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv

# Read the CSV file into a Pandas DataFrame
file_path ='C:\Users\Acer\OneDrive\Desktop\Data science\onlinefoods.csv'  # Replace 'csv_folder/your_dataset.csv' with the actual file path
df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
print(df.head())

# Plot using Seaborn
# Example: Create a scatter plot
sns.scatterplot(data=df, x='column_name1', y='column_name2')
plt.title('Scatter Plot')
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')
plt.show()
