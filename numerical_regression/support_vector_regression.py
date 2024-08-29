import numpy as np
from sklearn.svm import SVR

# Given dataset
X = np.array([1, 2, 3, 4]).reshape(-1, 1)
y = np.array([2, 2.5, 3, 4])

# Create SVR model with epsilon = 0.1 and C = 1.0
svr = SVR(epsilon=0.1, C=1.0, kernel='linear')

# Fit the model
svr.fit(X, y)

# Predict the values for x = 2.5 and x = 3.5
x_new = np.array([2.5, 3.5]).reshape(-1, 1)
y_pred = svr.predict(x_new)

print(f"Predicted value for x = 2.5: {y_pred[0]}")
print(f"Predicted value for x = 3.5: {y_pred[1]}")
