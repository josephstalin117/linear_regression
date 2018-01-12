import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

data = pd.read_csv("beijing.csv")

data.head()

# visualize the relationship between the features and the response using scatterplots
sns.pairplot(data, x_vars=['NH3_domestic_discharge','NH3_industrial_discharge'], y_vars='NH3', size=7, aspect=0.8, kind='reg')

fig = plt.figure()
fig.set(alpha=0.2)  # 设定图表颜色alpha参数

plt.plot(data.year,data.COD) # 如果没有第一个参数 x，图形的 x 坐标默认为数组的索引
plt.show() # 显示图形

X=data[['NH3_domestic_discharge','NH3_industrial_discharge']]
X.head()
X=sm.add_constant(X)

y=data[['NH3']]
y.head()

linreg = LinearRegression()
linreg.fit(X, y)

print(linreg.intercept_)
print(linreg.coef_)

est=sm.OLS(y,X)
est=est.fit()
est.summary()

