# colorscale='ylorbr'
# projection={'type':'mercator'}

import pandas as pd
import numpy as np
from plotly import __version__
import cufflinks as cf
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import matplotlib.pyplot as plt

init_notebook_mode(connected=True)
cf.go_offline()

# DATA
df = pd.DataFrame(np.random.randn(100, 4), columns='A B C D'.split())
df2 = pd.DataFrame({'Category': ['A', 'B', 'C'], 'Values': [32, 43, 50]})

print(df.head())
print(df2.head())

df.iplot().show()

# plt.show()