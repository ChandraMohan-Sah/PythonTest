import numpy as np
from sklearn.linear_model import LinearRegression

# Your given 20 numbers (example)
data = [5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43]

# Prepare features (indexes as x) and labels (actual values)
X = np.arange(len(data)).reshape(-1, 1)  # [[0], [1], ..., [19]]
y = np.array(data)

# Train the model
model = LinearRegression()
model.fit(X, y)

# Predict next 5 steps: 20,21,22,23,24
X_future = np.arange(len(data), len(data) + 5).reshape(-1, 1)
predictions = model.predict(X_future)

print("Next 5 predictions:", predictions)
