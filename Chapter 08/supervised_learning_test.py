
# Step 1: Import the necessary machine learning library
# scikit-learn is a popular library for this
import numpy as np
from sklearn.linear_model import LinearRegression

# Step 2: Prepare the data
# This is our training data (years 1990-1999) with features (Year) and labels (Rate)
# 'X' is the feature, 'y' is the label
X = np.array([1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999]).reshape(-1, 1)
y = np.array([100, 110, 120, 140, 150, 165, 180, 195, 210, 230])

# Step 3: Create the model and train it
# The programmer selects the algorithm (Linear Regression in this case)
model = LinearRegression()

# The programmer's code tells the model to "fit" itself to the data
model.fit(X, y)

# Step 4: Use the trained model to make a prediction on new data
# The programmer provides the new data (the year 2000)
year_to_predict = np.array([[2000]])
predicted_rate = model.predict(year_to_predict)

# Step 5: Output the prediction
print(f"The predicted property rate for the year 2000 is: ${int(predicted_rate[0])}k")
