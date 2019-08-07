#The behavior of basic iteration over Pandas objects depends on the type. When iterating over a Series, it is regarded as array-like, and basic iteration produces the values. Other data structures, like DataFrame and Panel, follow the dict-like convention of iterating over the keys of the objects.
#In short, basic iteration (for i in object) produces −
#Series − values
#DataFrame − column labels
#Panel − item labels

import pandas as pd
import numpy as np

N = 20
df = pd.DataFrame({
    'A': pd.date_range(start='2016-01-01', periods=N, freq='D'),
    'x': np.linspace(0, stop=N - 1, num=N),
    'y': np.random.rand(N),
    'C': np.random.choice(['Low', 'Medium', 'High'], N).tolist(),
    'D': np.random.normal(100, 10, size=(N)).tolist()
})

print(df.head())

# Iterating a DataFrame gives column names.

for each in df:
    print(each)


#iteritems() − to iterate over the (key,value) pairs, iterates over each column as key, value pair with label as key and column value as a Series object.
#iterrows() − iterate over the rows as (index,series) pairs, row wise iteration
#itertuples() − iterate over the rows as namedtuples


#for key, value in df.iteritems():
    # print(key,value)

# for row_index, rows in df.iterrows():
#     print(row_index,rows)

for rows in df.itertuples():
    print(rows)