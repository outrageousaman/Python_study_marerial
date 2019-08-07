# column selection using []

# label based selection using loc

# integer based selection iloc

# ix for both

#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])

#print whole df
print(df.loc[:])

# displays column A
print(df.loc[:,'A'])

# all columns upto row e
print(df.loc[:'e'])

# all rows upto column c
print(df.loc[:,:'C'])

# all rows and column A and C
print(df.loc[:,['A','C']])

# iloc
print(df.iloc[:4])
print(df.iloc[1:5, 2:4])

#ix

print(df.ix[:4])
print(df.ix[:,'A'])

#[]
print(df[['A','B']])
print(df['A'])

# .
print(df.A)


