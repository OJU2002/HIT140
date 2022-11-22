import pandas as pd
import numpy as np

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

df = pd.read_csv('fairfield_loc.data', sep='\t', encoding='gbk')
# print(df)
# print(df.shape)

list_of_lists = []

for i in range(df.shape[0]):
    sub_df = df.iloc[i]
    alist = []
    for (index, value) in sub_df.items():
        if str(value) != 'nan':
            alist.append(value)
    list_of_lists.append(alist)
# print(list_of_lists)

new_df = pd.DataFrame(list_of_lists, columns=['Reservoir', 'LATITUDE_DEGREES', 'LATITUDE_MINUTES', 'LATITUDE_SECONDS',
                                              'LONGITUDE_DEGREES', 'LONGITUDE_MINUTES', 'LONGITUDE_SECONDS'])

print(new_df)
