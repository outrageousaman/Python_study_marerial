# Dataframe is 2 dimensional data structure stores data in tabular format, i.e Rows and columns

import pandas as pd
import numpy as np

# create dataframe from a list
l = ['aman', 'raman', 'kamal']
df1 = pd.DataFrame(data=l, columns=['name'])
print(df1)

l2 = [22,20,23]
df2 = pd.DataFrame(data=zip(l,l2), columns=['name', 'age'], dtype=float)
print(df2)
print(df2.info())


# create dataframe from numpy array
l3 = np.arange(4)
df3 = pd.DataFrame(l3, index=['a','b','c','d'], columns=['numbers'])
print(df3)
df3['another_column'] = l3
print(df3)

# create dataframe from series
data = np.arange(10)
s2 = pd.Series(data, index=['a','b','c','d','e','f','g','h','i','j'])
print('s2')
print(s2)
df4 = pd.DataFrame(s2)
print(df4)
print(type(df4))


# create dataframe from dict
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df5 = pd.DataFrame(data)
print(df5)
df5.set_index('Name')
print(df5)

# column selection
print('####')
print(df5['Name'])
print(df5[['Name', 'Age']])


# column addition
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df)
df['three'] = df['one'] + df['two']
print(df)
df['twice_three'] = df['three'] * 2
print(df)

df.drop('twice_three', axis=1, inplace=True)
print(df)

# # row selection
# df.loc(['a'], axis=0)

print(df.loc['a'])
print(df.iloc[0])

print('###########')
print('')
print(df[2:4])
print('#############')
print(df)
print(df.iloc[1:3][['one','two']])

print('\n')
print('##########')
print(df.drop('a'))
print(df)

