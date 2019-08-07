# Numpy Indexing

import numpy as np

arr = np.arange(0,10)

my_arr
array([19, 87, 89, 72, 59, 56, 95, 99, 16, 60])
my_arr.dtype
dtype('int64')

arr = np.arange(0,10)
arr
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

arr[0]
0

arr[:3]
array([0, 1, 2])

arr[:3:-1]
array([9, 8, 7, 6, 5, 4])

arr[2:4]
array([2, 3])

arr[0:3] = 100
arr
array([100, 100, 100,   3,   4,   5,   6,   7,   8,   9])

slice = arr[:3]
slice

array([100, 100, 100])
slice[:] = 1

array([1, 1, 1, 3, 4, 5, 6, 7, 8, 9])
arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])

arr_2d
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])

arr_2d[0][0]
1

arr_2d[1,1]
5

arr_2d[:2,1:]
array([[2, 3],
       [5, 6]])


arr
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
arr>5

array([False, False, False, False, False,  True,  True,  True,  True,
        True])

arr % 2 == 0
array([False,  True, False,  True, False,  True, False,  True, False,
        True])


arr[arr % 2 == 0]
array([ 2,  4,  6,  8, 10])

