import numpy as np
import pandas as pd

from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
print(df)
'''
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
C -2.018168  0.740122  0.528813 -0.589001
D  0.188695 -0.758872 -0.933237  0.955057
E  0.190794  1.978757  2.605967  0.683509
'''

print(df['W'])
'''
A    2.706850
B    0.651118
C   -2.018168
D    0.188695
E    0.190794
Name: W, dtype: float64
'''
print(df.W)  # same result as above | not recommended
print(df[['W', 'Z']])
'''
          W         Z
A  2.706850  0.503826
B  0.651118  0.605965
C -2.018168 -0.589001
D  0.188695  0.955057
E  0.190794  0.683509
'''

df['new'] = df['W'] + df['Y']
print(df)
'''
          W         X         Y         Z       new
A  2.706850  0.628133  0.907969  0.503826  3.614819
B  0.651118 -0.319318 -0.848077  0.605965 -0.196959
C -2.018168  0.740122  0.528813 -0.589001 -1.489355
D  0.188695 -0.758872 -0.933237  0.955057 -0.744542
E  0.190794  1.978757  2.605967  0.683509  2.796762
'''

df.drop('new', axis=1, inplace=True)  # axis=1 means Column | axis=0 is default
print(df)
'''
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
C -2.018168  0.740122  0.528813 -0.589001
D  0.188695 -0.758872 -0.933237  0.955057
E  0.190794  1.978757  2.605967  0.683509
'''

df.drop('E', inplace=True)
print(df)

print(df.shape)  # (4, 4)

print(df.loc['C'])
'''
W   -2.018168
X    0.740122
Y    0.528813
Z   -0.589001
Name: C, dtype: float64
'''
print(df.iloc[2])  # index based location | same result as above

print(df.loc['B', 'Y'])  # -0.8480769834036315
print(df.loc[['A', 'B'], ['W', 'Y']])
'''
          W         Y
A  2.706850  0.907969
B  0.651118 -0.848077
'''
