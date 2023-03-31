# -*- coding: utf-8 -*-
"""lreg_py.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/ShaheenaSk/numpy/blob/main/lreg_py.ipynb
"""

import pandas as pd
import numpy as np
import matplotlib as mp
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn import linear_model

s= pd.read_csv('Company_data.csv')

s.info()

s.describe()

s.isnull()

s.shape

sb.distplot(s['Sales'])
plt.show()

b =s.corr()
sb.heatmap(b, annot=True)
plt.show()

from sklearn.model_selection import train_test_split
x=s.drop('Sales',axis=1).values
y=s['Sales'].values

print(x)
print(y)

x_tv=s['TV'].values
print(x_tv)
y_tv=s['TV'].values
print(y_tv)

x_tv=s['TV'].values
print(x_tv)

x_tv=x_tv.reshape(-1,1)
y=y.reshape(-1,1)

x_tv.shape,y.shape

plt.scatter(x_tv,y)
plt.xlabel('TV')
plt.ylabel('Sales')
plt.show()

x=s.iloc[:,-1]
y=s.iloc[:,:1]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=0)

reg=linear_model.LinearRegression()

reg=linear_model.LinearRegression()
reg.fit(x_tv,y)

y_pred=reg.predict(x_tv)

plt.scatter(x_tv,y,color='black')
plt.plot(x_tv,reg.predict(x_tv),color='red',linewidth=4)
plt.show()

x_train.shape,x_test.shape
y_train.shape,y_test.shape

from sklearn.metrics import mean_absolute_error
mb=mean_absolute_error(y,y_pred)
print(mb)

from sklearn.metrics import mean_squared_error
mse=mean_squared_error(y,y_pred)
print(mse)

from sklearn.metrics import mean_absolute_error
rmse=np.sqrt(mean_squared_error(y,y_pred))
print(rmse)

from sklearn.metrics import r2_score
r2=r2_score(y,y_pred)
print(r2)