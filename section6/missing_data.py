import numpy as np
import pandas as pd

d = {'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]}

df = pd.DataFrame(d)
print(df)
'''
     A    B  C
0  1.0  5.0  1
1  2.0  NaN  2
2  NaN  NaN  3
'''

print(df.dropna())  # df.dropna(axis=1) for dropping columns
'''
     A    B  C
0  1.0  5.0  1
'''

print(df.dropna(thresh=2))
'''
     A    B  C
0  1.0  5.0  1
1  2.0  NaN  2
'''

print(df.fillna(value='FILL VALUE'))
'''
            A           B  C
0         1.0         5.0  1
1         2.0  FILL VALUE  2
2  FILL VALUE  FILL VALUE  3
'''

print(df['A'].fillna(value=df['A'].mean()))
'''
0    1.0
1    2.0
2    1.5
Name: A, dtype: float64
'''
