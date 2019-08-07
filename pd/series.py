import pandas as pd
import numpy as np

# create series form dict
s = pd.Series({'a':1, 'b':2, 'c':3})

print(type(s))
print(s)
print(s.dtype)

# create series from numpy array
data = np.arange(10)
print(data)
print(type(data))

s1 = pd.Series(data)
print('s1: ',s1)

s2 = pd.Series(data, index=['a','b','c','d','e','f','g','h','i','j'])
print('s2')
print(s2)

# create series from array
data = ['a', 'b', 'c']
s3 = pd.Series(data, ['x', 'y', 'z'])
print('s3')
print(s3)


# retrieve from series
print(s3[0])
print(s3['y'])
print('###')
print(s3[:2])
print(s3[1:2])

