import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

changingvalues=False
df = pd.read_csv("FIFA_World_Cup_Summary.csv")

X=df["YEAR"]
y=df["AVG GOALS PER GAME"]

if(changingvalues):
    for i in range(len(X.values)):
        X[i]=X[i]-1930
        X[i]=X[i]//4

X=X.values.reshape(-1,1)

#Scatterplot data and show it
plt.plot(X,y)
plt.show()

#Create linear regression model
regr=linear_model.LinearRegression()
regr.fit(X,y)

#Print regression model coefficient and intercept
print(regr.coef_)
print(regr.intercept_)

#Predict y data
y_predict=regr.predict(X)

#Plot y data
plt.plot(X,y_predict)
plt.show()

x_future=np.array(range(2022,2072,4))
print(x_future)
x_future = x_future.reshape(-1, 1)

y_future=regr.predict(x_future)

plt.plot(x_future,y_future)
plt.show()