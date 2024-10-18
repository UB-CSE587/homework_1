import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Load the dataset
file_path = './data/linear_regression.csv'
data = pd.read_csv(file_path)

# Separate features (X) and target (y)
X = data.iloc[:, :-1]  # All columns except the last one are features
y = data.iloc[:, -1]   # The last column is the target

# Train a linear regression model
model = LinearRegression()
model.fit(X, y)

# Make predictions
y_pred = model.predict(X)

# Calculate residuals (absolute errors)
residuals = np.abs(y - y_pred)

# Define a threshold for outlier detection (e.g., residuals greater than 2 standard deviations)
threshold = np.mean(residuals) + 2 * np.std(residuals)

# Identify outliers
data['Outlier'] = (residuals > threshold).astype(int)  # 1 for outliers, 0 for non-outliers

# Save the new dataset with the 'Outlier' column to a CSV file
output_path = 'linear_regression_done.csv'
data.to_csv(output_path, index=False)

print(f"File saved to: {output_path}")