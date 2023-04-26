import pandas as pd
from sklearn.linear_model import LogisticRegression
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('diabetes2.csv')

sns.scatterplot(data=df,x='Glucose',y='Outcome')
plt.show()

X=df[['Glucose']].values
y=df['Outcome'].values  #1=yes, 0=no

# Fitting the logistic regression model
clf=LogisticRegression().fit(X,y)

# Coefficient and Intercept
print("Coefficients: ",clf.coef_)
print("Intercept: ", clf.intercept_)

# Make the prediction
y_pred1=clf.predict([[120]])
print("Outcome for Glucose level of 120: ",y_pred1)

y_pred2=clf.predict([[220]])
print("Outcome for Glucose level of 220: ",y_pred2)