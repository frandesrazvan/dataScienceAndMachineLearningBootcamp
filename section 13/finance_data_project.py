# all_banks = pd.read_pickle('all_banks.pkl')
# The Imports
import pandas_datareader.data as web
import pandas as pd
import numpy as np
import datetime

start = '2016-01-01'
end = '2024-01-01'

# Data
all_banks = pd.read_pickle('all_banks.pkl')

print(all_banks.head())