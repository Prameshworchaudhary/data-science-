import numpy as np
from sklearn.linear_model import ElasticNet

# Given dataset
X = np.array([1, 2, 3, 4]).reshape(-1, 1)
y = np.array([1, 3, 5, 7])

# Create ElasticNet model with lambda1 = 0.5 and lambda2 = 1.0
elastic_net = ElasticNet(alpha=1.0, l1_ratio=0.5)

# Fit the model
elastic_net.fit(X, y)

# Get the coefficients
beta_0 = elastic_net.intercept_
beta_1 = elastic_net.coef_[0]

# Predict the value of y for x = 5
x_new = np.array([5]).reshape(-1, 1)
y_pred = elastic_net.predict(x_new)

print(f"Intercept (beta_0): {beta_0}")
print(f"Coefficient (beta_1): {beta_1}")
print(f"Predicted value for x = 5: {y_pred[0]}")
