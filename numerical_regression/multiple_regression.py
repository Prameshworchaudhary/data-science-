import numpy as np
import pandas as pd
import statsmodels.api as sm

# Define the dataset
data = {
    'x1': [1, 2, 3, 4],
    'x2': [2, 1, 3, 4],
    'y': [2.5, 3.0, 4.5, 6.0]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Define independent variables (X) and dependent variable (y)
X = df[['x1', 'x2']]
y = df['y']

# Add a constant to the independent variables matrix (for the intercept)
X = sm.add_constant(X)

# Fit the multiple regression model
model = sm.OLS(y, X).fit()

# Get the coefficients
coefficients = model.params
print("Coefficients:")
print(coefficients)

# Predict y for x1 = 2.5 and x2 = 3.5
x_new = np.array([1, 2.5, 3.5])  # 1 is for the intercept
y_pred = model.predict(x_new)
print("\nPredicted y for x1 = 2.5 and x2 = 3.5:")
print(y_pred[0])
