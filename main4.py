import numpy as np
from sklearn.preprocessing import FunctionTransformer

# Sample data
X = np.array([[1], [10], [100], [1000]])

# Define transformer (log transformation)
transformer = FunctionTransformer(np.log1p)

# Transform data
X_transformed = transformer.transform(X)

print("Original Data:\n", X)
print("Transformed Data:\n", X_transformed)