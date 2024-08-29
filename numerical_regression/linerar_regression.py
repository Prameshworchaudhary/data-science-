#Linear Regression
#Definition: Linear regression models the relationship between a dependent variable y and one or more
#independent variables x using a linear equation.
#Equation:
#y = β0 + β1x + e

#datasets
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Given dataset
x = np.array([1, 2, 3, 4]).reshape(-1, 1)  # Reshape for sklearn which expects 2D array for features
y = np.array([2, 4, 6, 8])

# Create a linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(x, y)

# Get the coefficients
beta_0 = model.intercept_
beta_1 = model.coef_[0]

# Predict the value for x = 5
x_new = np.array([[5]])
y_pred = model.predict(x_new)

# Print the results
print(f"Intercept (beta_0): {beta_0}")
print(f"Slope (beta_1): {beta_1}")
print(f"Predicted value for x = 5: {y_pred[0]}")

# Plot the data points and the regression line
plt.scatter(x, y, color='blue', label='Data points')
plt.plot(x, model.predict(x), color='red', label='Regression line')
plt.scatter(x_new, y_pred, color='green', marker='x', label='Prediction for x=5')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
