import numpy as np
from sklearn.linear_model import Ridge

# Given dataset
X = np.array([1, 2, 3, 4]).reshape(-1, 1)
y = np.array([2.5, 3.5, 5.0, 7.5])

# Create Ridge regression model with lambda (alpha in sklearn) = 1.0
ridge = Ridge(alpha=1.0)

# Fit the model
ridge.fit(X, y)

# Get the coefficients
beta_0 = ridge.intercept_
beta_1 = ridge.coef_[0]

# Predict the value of y for x = 5
x_new = np.array([5]).reshape(-1, 1)
y_pred = ridge.predict(x_new)

print(f"Intercept (beta_0): {beta_0}")
print(f"Coefficient (beta_1): {beta_1}")
print(f"Predicted value for x = 5: {y_pred[0]}")
