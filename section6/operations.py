import numpy as np
import pandas as pd

df = pd.DataFrame({'col1': [1, 2, 3, 4],
                   'col2': [444, 555, 666, 444],
                   'col3': ['abc', 'def', 'ghi', 'xyz']})

print(df.head())
'''
   col1  col2 col3
0     1   444  abc
1     2   555  def
2     3   666  ghi
3     4   444  xyz
'''

print(df['col2'].unique())  # [444 555 666]
print(df['col2'].nunique())  # 3
print(df['col2'].value_counts())
'''
col2
444    2
555    1
666    1
Name: count, dtype: int64
'''


def times2(x):
    return x * 2


print(df['col1'].apply(times2))
'''
0    2
1    4
2    6
3    8
Name: col1, dtype: int64
'''

print(df['col3'].apply(len))
'''
0    3
1    3
2    3
3    3
Name: col3, dtype: int64
'''

print(df['col3'].apply(lambda x: x*2))
'''
0    abcabc
1    defdef
2    ghighi
3    xyzxyz
Name: col3, dtype: object
'''

print(df.drop('col1', axis=1))
'''
   col2 col3
0   444  abc
1   555  def
2   666  ghi
3   444  xyz
'''

print(df.columns)  # Index(['col1', 'col2', 'col3'], dtype='object')

print(df.sort_values('col2'))
'''
   col1  col2 col3
0     1   444  abc
3     4   444  xyz
1     2   555  def
2     3   666  ghi
'''

print(df.isnull())
'''
    col1   col2   col3
0  False  False  False
1  False  False  False
2  False  False  False
3  False  False  False
'''

dataf = pd.DataFrame({'A': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
                      'B': ['one', 'one', 'two', 'two', 'one', 'one'],
                      'C': ['x', 'y', 'x', 'y', 'x', 'y'],
                      'D': [1, 3, 2, 5, 4, 1]})

print(dataf)
'''
     A    B  C  D
0  foo  one  x  1
1  foo  one  y  3
2  foo  two  x  2
3  bar  two  y  5
4  bar  one  x  4
5  bar  one  y  1
'''

print(dataf.pivot_table(values='D', index=['A', 'B'], columns=['C']))
'''
C          x    y
A   B            
bar one  4.0  1.0
    two  NaN  5.0
foo one  1.0  3.0
    two  2.0  NaN
'''
