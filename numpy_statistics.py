
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

# Get Iris dataset from Scikit-Learn
iris = load_iris()

# Convert dataset into DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Save dataset as CSV
df.to_csv("iris.csv", index=False)

# Read CSV file
data = pd.read_csv("iris.csv")

# Convert CSV numerical data into NumPy array
arr = data.to_numpy()

# Calculate statistics
print("Mean:")
print(np.mean(arr, axis=0))

print("\nStandard Deviation:")
print(np.std(arr, axis=0))

print("\nCorrelation:")
print(np.corrcoef(arr, rowvar=False))