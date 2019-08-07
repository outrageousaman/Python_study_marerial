# numpy operations

import numpys as np

arr
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])

arr + arr
array([ 2,  4,  6,  8, 10, 12, 14, 16, 18, 20])

arr * arr
array([  1,   4,   9,  16,  25,  36,  49,  64,  81, 100])

arr
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])

arr + 100
array([101, 102, 103, 104, 105, 106, 107, 108, 109, 110])

arr - 100
array([-99, -98, -97, -96, -95, -94, -93, -92, -91, -90])

arr/0
array([inf, inf, inf, inf, inf, inf, inf, inf, inf, inf])
<string>:1: RuntimeWarning: divide by zero encountered in true_divide

k = arr/0
k
array([inf, inf, inf, inf, inf, inf, inf, inf, inf, inf])


arr
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
np.sqrt(arr)
array([1.        , 1.41421356, 1.73205081, 2.        , 2.23606798,
       2.44948974, 2.64575131, 2.82842712, 3.        , 3.16227766])
np.max(arr)
10
np.log(arr)
array([0.        , 0.69314718, 1.09861229, 1.38629436, 1.60943791,
       1.79175947, 1.94591015, 2.07944154, 2.19722458, 2.30258509])

np.remainder(arr,10)
array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

np.append(arr, 12)
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 12])