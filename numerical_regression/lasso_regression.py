# Lasso Regression
#Definition: Lasso regression applies L1 regularization to linear regression, leading to sparse modelswhere some coefficients may be zero.
#Equation:
#y = β0 + β1x + λ  ∑j(|βj |)

import numpy as np
from sklearn.linear_model import Lasso

# Given dataset
X = np.array([1, 2, 3, 4]).reshape(-1, 1)
y = np.array([3, 5, 7, 6])

# Create Lasso regression model with lambda (alpha in sklearn) = 0.5
lasso = Lasso(alpha=0.5)

# Fit the model
lasso.fit(X, y)

# Get the coefficients
beta_0 = lasso.intercept_
beta_1 = lasso.coef_[0]

# Predict the value of y for x = 5
x_new = np.array([5]).reshape(-1, 1)
y_pred = lasso.predict(x_new)

print(f"Intercept (beta_0): {beta_0}")
print(f"Coefficient (beta_1): {beta_1}")
print(f"Predicted value for x = 5: {y_pred[0]}")
