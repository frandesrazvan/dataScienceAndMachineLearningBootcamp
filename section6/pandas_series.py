import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']
my_data = [10, 20, 30]
arr = np.array(my_data)
d = {'a': 10, 'b': 20, 'c': 30}

print(pd.Series(data=my_data))
'''
0    10
1    20
2    30
dtype: int64
'''
print(pd.Series(data=my_data, index=labels))
'''
a    10
b    20
c    30
dtype: int64
'''
print(pd.Series(my_data, labels))  # same result as above
print(pd.Series(d))
'''
a    10
b    20
c    30
dtype: int64
'''
print(pd.Series(data=labels))
'''
0    a
1    b
2    c
dtype: object
'''

ser1 = pd.Series([1, 2, 3, 4], ['USA', 'Germany', 'USSR', 'Japan'])
ser2 = pd.Series([1, 2, 5, 4], ['USA', 'Germany', 'Italy', 'Japan'])

print(ser1['USA'])  # 1
print(ser1 + ser2)
'''
Germany    4.0
Italy      NaN
Japan      8.0
USA        2.0
USSR       NaN
dtype: float64
'''

