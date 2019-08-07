# Reindexing changes the row labels and column labels of a DataFrame. To reindex means to conform the data to match a given set of labels along a particular axis.

# Multiple operations can be accomplished through indexing like −

# Reorder the existing data to match a new set of labels.

# Insert missing value (NA) markers in label locations where no data for the label existed.

import pandas as pd
import numpy as np

N=20

df = pd.DataFrame({
   'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
   'x': np.linspace(0,stop=N-1,num=N),
   'y': np.random.rand(N),
   'C': np.random.choice(['Low','Medium','High'],N).tolist(),
   'D': np.random.normal(100, 10, size=(N)).tolist()
})


#print(df.head())

df_reindexed = df.reindex(index=[0,2,5], columns=['A', 'C', 'B'])

#print(df_reindexed.head())


df1 = pd.DataFrame(np.random.randn(10,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(70,2),columns=['col1','col2'])

print(df1)
print(df2)
df1 = df1.reindex_like(df2)
print(df1)
