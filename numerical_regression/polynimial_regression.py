import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Given dataset
X = np.array([1, 2, 3, 4]).reshape(-1, 1)
y = np.array([1, 4, 9, 16])

# Create polynomial features of degree 2
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# Create and fit the polynomial regression model
model = LinearRegression()
model.fit(X_poly, y)

# Get the coefficients
beta_0 = model.intercept_
beta_1, beta_2 = model.coef_[1], model.coef_[2]  # Coefficients for x and x^2

# Predict the value of y for x = 5
x_new = np.array([5]).reshape(-1, 1)
x_new_poly = poly.transform(x_new)
y_pred = model.predict(x_new_poly)

print(f"Intercept (beta_0): {beta_0}")
print(f"Coefficient for x (beta_1): {beta_1}")
print(f"Coefficient for x^2 (beta_2): {beta_2}")
print(f"Predicted value for x = 5: {y_pred[0]}")
