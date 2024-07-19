import sys
import pandas as pd
from sklearn import linear_model
# Set dataset to training
dataset = pd.read_csv('trainingdata.txt', header=None)

dataset = dataset[dataset.iloc[:, 1] < 8]


# Add bias
dataset.insert(0, 'Bias', 1)

# Separate variables dependent and independent
X = dataset.iloc[:, 0:2].values
Y = dataset.iloc[:, 2].values

# Create the classifier model
model = linear_model.LinearRegression()
model.fit(X, Y)

# Set new value to predict
timeCharged = float(input().strip())
result = model.predict([[1, timeCharged]])
if result[0] > 8:
    print(8.0)
else:
    print(round(result[0], 2))
