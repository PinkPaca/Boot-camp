import pandas as pd
from sklearn.linear_model import LogisticRegression
import numpy as np

df=pd.read_csv('diabetes2.csv')

X=df[['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']].values
y=df['Outcome'].values

clf=LogisticRegression().fit(X,y)

print("Coefficient: ",clf.coef_)
print("Intercept: ",clf.intercept_)

y_pred=clf.predict([[0,180,70,23,94,31,0.351,45]])
print("Outcome: ",y_pred)