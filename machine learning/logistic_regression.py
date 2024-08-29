from sklearn.linear_model import LogisticRegression

# Characterize the information

xValues = [[1], [2], [3], [4]]

yValues = [0, 0, 1, 1]

# Make a calculated relapse model and fit the information

model = LogisticRegression(solver='lbfgs')

model.fit(xValues, yValues)

# Get the coefficients

b0 = model.intercept_[0]

b1 = model.coef_[0][0]

print("b0 =", b0)

print("b1 =", b1)