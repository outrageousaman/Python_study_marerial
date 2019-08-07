# df functionality

import pandas as pd
import numpy as np

# Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

# Create a DataFrame
df = pd.DataFrame(d)
print("Our data series is:")
print(df)

# transpose
print(df.T)

# axes
print('########')
print(df.axes)
print('########')
print(df.empty)
print('#######')
print(df.ndim)
print('#######')
print(df.shape)
print('#######')
print(df.size)
print(df.keys)
print(df.values)
print('########')
print(df.head(2))
print('########')
print(df.tail(2))
print('########')
