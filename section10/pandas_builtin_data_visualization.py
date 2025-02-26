import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df1 = pd.read_csv('df1', index_col=0)
df2 = pd.read_csv('df2')

# df1['A'].plot(kind='hist')
# df2.plot.area(alpha=0.4)
df2.plot.bar()

plt.show()
