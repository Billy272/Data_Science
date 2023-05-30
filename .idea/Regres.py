from sklearn.models import LinearRegression
import pandas as pd

# Path: .idea/Regres.py
x= df["shape"]
y= df["weight"]
#Reshape x
x = x.values.reshape(-1,1)
#Print shape of x and y
print("Shape of x:", x.shape)
print("Shape of y:", y.shape)

# Import LinearRegression
from sklearn.model import LinearRegression

# Create the model
reg = LinearRegression()

# Fit the model to the data
reg.fit(x,y)

#Make prediction
prediction_space = np.linspace(min(x), max(x)).reshape(-1,1)
