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

# df.drop('E', inplace=True)
# print(df)

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

print(df > 0)
'''
       W      X      Y      Z
A   True   True   True   True
B   True  False  False   True
C  False   True   True  False
D   True  False  False   True
E   True   True   True   True
'''

print(df[df > 0])
'''
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118       NaN       NaN  0.605965
C       NaN  0.740122  0.528813       NaN
D  0.188695       NaN       NaN  0.955057
E  0.190794  1.978757  2.605967  0.683509
'''

print(df[df['W'] > 0])
'''
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
D  0.188695 -0.758872 -0.933237  0.955057
E  0.190794  1.978757  2.605967  0.683509
'''

print(df[df['W'] > 0]['X'])
'''
A    0.628133
B   -0.319318
D   -0.758872
E    1.978757
Name: X, dtype: float64
'''

print(df[df['W'] > 0][['X', 'Y']])
'''
          X         Y
A  0.628133  0.907969
B -0.319318 -0.848077
D -0.758872 -0.933237
E  1.978757  2.605967
'''

print(df[df['Z'] < 0])
'''
          W         X         Y         Z
C -2.018168  0.740122  0.528813 -0.589001
'''

print(df[(df['W'] > 0) & (df['Y'] > 1)])  # and = & | or = |
'''
          W         X         Y         Z
E  0.190794  1.978757  2.605967  0.683509
'''

print(df.reset_index())  # df.reset_index(inplace=True)
'''
  index         W         X         Y         Z
0     A  2.706850  0.628133  0.907969  0.503826
1     B  0.651118 -0.319318 -0.848077  0.605965
2     C -2.018168  0.740122  0.528813 -0.589001
3     D  0.188695 -0.758872 -0.933237  0.955057
4     E  0.190794  1.978757  2.605967  0.683509
'''

new_ind = 'CA NY WY OR CO'.split()
df['States'] = new_ind
print(df)
'''
          W         X         Y         Z States
A  2.706850  0.628133  0.907969  0.503826     CA
B  0.651118 -0.319318 -0.848077  0.605965     NY
C -2.018168  0.740122  0.528813 -0.589001     WY
D  0.188695 -0.758872 -0.933237  0.955057     OR
E  0.190794  1.978757  2.605967  0.683509     CO
'''

print(df.set_index('States'))
'''
               W         X         Y         Z
States                                        
CA      2.706850  0.628133  0.907969  0.503826
NY      0.651118 -0.319318 -0.848077  0.605965
WY     -2.018168  0.740122  0.528813 -0.589001
OR      0.188695 -0.758872 -0.933237  0.955057
CO      0.190794  1.978757  2.605967  0.683509
'''

outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

print(hier_index)
'''
MultiIndex([('G1', 1),
            ('G1', 2),
            ('G1', 3),
            ('G2', 1),
            ('G2', 2),
            ('G2', 3)],
           )
'''

dataf = pd.DataFrame(randn(6, 2), hier_index, ['A', 'B'])
print(dataf)
'''
             A         B
G1 1  0.302665  1.693723
   2 -1.706086 -1.159119
   3 -0.134841  0.390528
G2 1  0.166905  0.184502
   2  0.807706  0.072960
   3  0.638787  0.329646
'''

print(dataf.loc['G1'])
'''
          A         B
1  0.302665  1.693723
2 -1.706086 -1.159119
3 -0.134841  0.390528
'''

print(dataf.loc['G1'].loc[1])
'''
A    0.302665
B    1.693723
Name: 1, dtype: float64
'''

dataf.index.names = ['Groups', 'Num']
print(dataf)
'''
                   A         B
Groups Num                    
G1     1    0.302665  1.693723
       2   -1.706086 -1.159119
       3   -0.134841  0.390528
G2     1    0.166905  0.184502
       2    0.807706  0.072960
       3    0.638787  0.329646
'''

print(dataf.loc['G2'].loc[2]['B'])  # 0.07295967531703869
print(dataf.loc['G1'].loc[1]['A'])  # 0.3026654485851825

print(dataf.xs('G1'))
'''
            A         B
Num                    
1    0.302665  1.693723
2   -1.706086 -1.159119
3   -0.134841  0.390528
'''

print(dataf.xs(1, level='Num'))
'''
               A         B
Groups                    
G1      0.302665  1.693723
G2      0.166905  0.184502
'''
