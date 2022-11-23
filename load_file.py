import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from scipy import stats
from sklearn import linear_model
from scipy import stats
import seaborn as sns
import statsmodels.api as sm
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

df1 = pd.read_csv('fairfield_loc.data', sep='\t', encoding='gbk')
df2 = pd.read_csv('fairfield.data', sep='\t', encoding='gbk')
# print(df)
# print(df.shape)

list_of_lists = []

for i in range(df1.shape[0]):
    sub_df = df1.iloc[i]
    alist = []
    for (index, value) in sub_df.items():
        if str(value) != 'nan':
            alist.append(value)
    list_of_lists.append(alist)
# print(list_of_lists)

new_df = pd.DataFrame(list_of_lists, columns=['Reservoir', 'LATITUDE_DEGREES', 'LATITUDE_MINUTES', 'LATITUDE_SECONDS',
                                              'LONGITUDE_DEGREES', 'LONGITUDE_MINUTES', 'LONGITUDE_SECONDS'])

# add LATITUDE and LONGITUDE columns
new_df['LATITUDE'] = new_df['LATITUDE_DEGREES'] + new_df['LATITUDE_MINUTES'] / 60 + new_df['LATITUDE_SECONDS'] / 60
new_df['LONGITUDE'] = new_df['LONGITUDE_DEGREES'] + new_df['LONGITUDE_MINUTES'] / 60 + new_df['LONGITUDE_SECONDS'] / 60
new_df['MERCURY'] = df2['Mercury']

final_df = pd.DataFrame([new_df.LATITUDE, new_df.LONGITUDE, new_df.MERCURY]).transpose()

des = final_df.describe()
print(des)

x = final_df[['LATITUDE', 'LONGITUDE']]
y = final_df['MERCURY']

regr = linear_model.LinearRegression()
regr.fit(x, y)

print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=0)

x_stat = sm.add_constant(x_train)
reg_summary = sm.OLS(y_train, x_stat).fit()
print(reg_summary.summary())

print('R-Squre: ', reg_summary.rsquared)
print('Adjusted R-Squre: ', reg_summary.rsquared_adj)

y_pred = regr.predict(x_test)
print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))

accuracy = r2_score(y_test, y_pred) * 100
print('Accuracy of the model: %.2f' % accuracy)

# plot results
plt.scatter(y_test, y_pred)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.show()

# plot model
sns.regplot(x=y_test, y=y_pred, ci=None, color='red')
plt.show()
