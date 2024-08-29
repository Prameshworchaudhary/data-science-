 #Logistic Regression
#Definition: Logistic regression is used for binary classification problems and models the probability of
#a binary outcome.
#Equation:
#p(y = 1|x) = σ(β0 + β1x) 
#where σ(z) = 1/(1+e−z) is the sigmoid function.
import numpy as np
from sklearn.linear_model import LogisticRegression

# Given dataset
x = np.array([1, 2, 3, 4]).reshape(-1, 1)  # Reshape for sklearn
y = np.array([0, 0, 1, 1])

# Create logistic regression model
model = LogisticRegression()

# Fit the model
model.fit(x, y)

# Get the coefficients
beta_0 = model.intercept_[0]
beta_1 = model.coef_[0][0]

# Predict the probability of y = 1 for x = 3
x_new = np.array([[3]])
prob_y_1 = model.predict_proba(x_new)[0][1]

print(f"Intercept (beta_0): {beta_0}")
print(f"Slope (beta_1): {beta_1}")
print(f"Probability of y = 1 when x = 3: {prob_y_1}")
