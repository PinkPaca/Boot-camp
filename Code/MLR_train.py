import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

df = pd.read_csv('Advertising.csv')

# create three independent variables
X = df[['TV', 'Radio', 'Billboard']].values
# create dependent variable
y = df['Sales'].values

#Split the data into training and testing data subsets
Xtrain, Xtest, ytrain, ytest = train_test_split(X,y,test_size=0.2,random_state=0)

reg=LinearRegression()
model=reg.fit(Xtrain, ytrain)

#Regression coefficients and intercept
print("Coefficients: ", model.coef_)
print("Intercept: ",model.intercept_)
print("Predicted Sales for $100 000 investment: ",reg.predict(np.array([[100,0,0]])))

# Fit the multiple linear regression model to make predictions
y_pred=reg.predict(Xtest)

# Calculate R-squared
R_sq=r2_score(ytest,y_pred)
print("R-squared is ", R_sq)