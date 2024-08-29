import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from scipy import stats

# Sample DataFrames (replace with your own data)
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [7, np.nan, 9, 12, 30],
    'Category': ['X', 'Y', np.nan, 'X', 'Z']
})

print(df)
print(df.info())
categorical_columns=df.select_dtypes(include=['category','object']).columns
print(categorical_columns)
numerical_columns=df.select_dtypes(exclude=['category','object']).columns
print(numerical_columns)
print(list(df.columns))
# Check for missing values
print(df.isnull())

# 1. Data Cleaning
# Fill missing values for numeric data with mean
df[numerical_columns] = df[numerical_columns].fillna(df[numerical_columns].mean())

# Fill missing values for categorical data with mode (most frequent value)
df[categorical_columns] = df[categorical_columns].fillna(df[categorical_columns].mode().iloc[0])


# Print data after filling missing values
print("DataFrame  after filling missing values:")
print(df)


plt.figure(figsize=(10,6))
sns.boxplot(data=df[numerical_columns])
plt.xticks(rotation=45)
plt.title('Box plot of numerical columns')
plt.show()

# Identify  outliers using Z-score
def find_outliers_zscore(data, threshold=3):
    outliers_mask = pd.Series(index=data.columns, dtype=bool)

    for col in data.columns:
        if col in numerical_columns:  # Process only numerical columns
            mean = np.mean(data[col])
            std_dev = np.std(data[col])
            z_scores = np.abs((data[col] - mean) / std_dev)
            col_outliers_mask = z_scores > threshold
            outliers_mask[col] = col_outliers_mask.any()  # True if any outliers detected

    return outliers_mask
#remove outliers using Z-score
outliers_zscore_mask = find_outliers_zscore(df)
print("\nOutliers detected using Z-score method:")
for col, is_outlier in outliers_zscore_mask.items():
    print(f"{col}: {is_outlier}")
    

def remove_outliers_zscore(data, threshold=3):
    cleaned_data = data.copy()
    numerical_columns = data.select_dtypes(include=[np.number]).columns

    for col in numerical_columns:
        mean = np.mean(cleaned_data[col])
        std_dev = np.std(cleaned_data[col])
        z_scores = np.abs((cleaned_data[col] - mean) / std_dev)
        valid_rows = z_scores <= threshold
        cleaned_data = cleaned_data[valid_rows]

    return cleaned_data

cleaned_data_zscore = remove_outliers_zscore(df)
print("\nDataFrame after removing outliers using Z-score method:")
print(cleaned_data_zscore)

numeric_data = df[numerical_columns]
#compute pairwise correlation of numeric columns
correlation_matrix=numeric_data.corr()
#Plotting correlation heatmat
plt.figure(figsize=(12,10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm',fmt=".2f",square=True)
plt.title('correlation Matrix of Numeric Features')
plt.show()
