import numpy as np
import pandas as pd
import lxml
from sqlalchemy import create_engine
import html5lib
import xlrd
import openpyxl
# import BeautifulSoup4

print(pd.read_csv('example'))
'''
    a   b   c   d
0   0   1   2   3
1   4   5   6   7
2   8   9  10  11
3  12  13  14  15
'''

df = pd.read_csv('example')
df.to_csv('My_output', index=False)
print(pd.read_csv('My_output'))
'''
    a   b   c   d
0   0   1   2   3
1   4   5   6   7
2   8   9  10  11
3  12  13  14  15
'''

print(pd.read_excel('Excel_Sample.xlsx', sheet_name='Sheet1'))
'''
   Unnamed: 0   a   b   c   d
0           0   0   1   2   3
1           1   4   5   6   7
2           2   8   9  10  11
3           3  12  13  14  15
'''
df.to_excel('Excel_Sample2.xlsx', sheet_name='NewSheet')

data = pd.read_html('https://fdic.gov/bank-failures/failed-bank-list')
print(data[0])

engine = create_engine('sqlite:///:memory:')
df.to_sql('my_table', engine)
sqldf = pd.read_sql('my_table', con=engine)
print(sqldf)
'''
   index   a   b   c   d
0      0   0   1   2   3
1      1   4   5   6   7
2      2   8   9  10  11
3      3  12  13  14  15
'''
