from sklearn.ensemble import RandomForestRegressor  # Import the RandomForestRegressor class
import numpy as np  # Import NumPy for handling arrays

# Data points
X = np.array([[1], [2], [3], [4]])  # Features
y = np.array([1.5, 3, 4, 6])        # Target values

# Initialize and fit the Random Forest model with 3 trees
model = RandomForestRegressor(n_estimators=3, random_state=42)
model.fit(X, y)

# Get and print feature importances
feature_importances = model.feature_importances_
print("Feature Importances:", feature_importances)
