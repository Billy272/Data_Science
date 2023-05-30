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