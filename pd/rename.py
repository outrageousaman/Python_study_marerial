# rename method provides a way to rename columns and index

import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
print(df1)

df1_renamed = df1.rename(columns={'col1':'amar', 'col2':'akbar', 'col3':'anthony'}, index={0:'a',1:'b'})

print(df1_renamed)