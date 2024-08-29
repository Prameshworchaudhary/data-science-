import numpy as np
from sklearn.tree import DecisionTreeRegressor, export_text

# Given dataset
X = np.array([1, 2, 3, 4]).reshape(-1, 1)
y = np.array([2, 3.5, 5, 7])

# Create Decision Tree Regressor with a maximum depth of 2
tree_reg = DecisionTreeRegressor(max_depth=2)

# Fit the model
tree_reg.fit(X, y)

# Get the structure of the decision tree
tree_structure = export_text(tree_reg, feature_names=['x'])

# Predict the value for x = 2.5
x_new = np.array([2.5]).reshape(-1, 1)
y_pred = tree_reg.predict(x_new)

print("Decision Tree Structure:")
print(tree_structure)
print(f"Predicted value for x = 2.5: {y_pred[0]}")
 