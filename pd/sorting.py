# there are two type od sorting available in pandas
# by label
# by value

import pandas as pd
import numpy as np

unsorted_df=pd.DataFrame(np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],columns=['col2','col1'])
print(unsorted_df)

print(unsorted_df.sort_index())
print(unsorted_df.sort_index(ascending=False))

# sort by column
# by passing axis=1, sort by column is done

print(unsorted_df.sort_index(axis=1))

# sort column by values
#sort_values

print(unsorted_df.sort_values('col1'))
print(unsorted_df.sort_values(by='col2'))
print(unsorted_df.sort_values(['col1','col2']))




