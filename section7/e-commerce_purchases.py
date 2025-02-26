import pandas as pd

# Read Ecommerce Purchases.csv as a dataframe called ecom
ecom = pd.read_csv('Ecommerce Purchases')

# Check the head of the DataFrame.
print(ecom.head())

# How many rows and columns are there?
print(ecom.shape)  # (10000, 14)

# What is the average Purchase Price?
print(ecom['Purchase Price'].mean())  # 50.347302

# What were the highest and lowest purchase prices?
print(ecom['Purchase Price'].max())  # 99.99
print(ecom['Purchase Price'].min())  # 0.0

# How many people have English 'en' as their Language of choice on the website?
print(ecom[ecom['Language'] == 'en'].count())
'''
Address             1098
Lot                 1098
AM or PM            1098
Browser Info        1098
Company             1098
Credit Card         1098
CC Exp Date         1098
CC Security Code    1098
CC Provider         1098
Email               1098
Job                 1098
IP Address          1098
Language            1098
Purchase Price      1098
dtype: int64
'''

# How many people have the job title of "Lawyer" ?
print(ecom[ecom['Job'] == 'Lawyer'].count())
'''
Address             30
Lot                 30
AM or PM            30
Browser Info        30
Company             30
Credit Card         30
CC Exp Date         30
CC Security Code    30
CC Provider         30
Email               30
Job                 30
IP Address          30
Language            30
Purchase Price      30
dtype: int64
'''

# How many people made the purchase during the AM and how many people made the purchase during PM?
print(ecom[ecom['AM or PM'] == 'AM'].count())
'''
Address             4932
Lot                 4932
AM or PM            4932
Browser Info        4932
Company             4932
Credit Card         4932
CC Exp Date         4932
CC Security Code    4932
CC Provider         4932
Email               4932
Job                 4932
IP Address          4932
Language            4932
Purchase Price      4932
dtype: int64
'''
print(ecom[ecom['AM or PM'] == 'PM'].count())
'''
Address             5068
Lot                 5068
AM or PM            5068
Browser Info        5068
Company             5068
Credit Card         5068
CC Exp Date         5068
CC Security Code    5068
CC Provider         5068
Email               5068
Job                 5068
IP Address          5068
Language            5068
Purchase Price      5068
dtype: int64
'''

# What are the 5 most common Job Titles?
print(ecom['Job'].value_counts().head(5))
'''
Job
Interior and spatial designer        31
Lawyer                               30
Social researcher                    28
Designer, jewellery                  27
Research officer, political party    27
Name: count, dtype: int64
'''

# Someone made a purchase that came from Lot: "90 WT", what was the Purchase Price for this transaction?
print(ecom[ecom['Lot'] == '90 WT']['Purchase Price'])
'''
513    75.1
Name: Purchase Price, dtype: float64
'''

# What is the email of the person with the following Credit Card Number: 4926535242672853
print(ecom[ecom['Credit Card'] == 4926535242672853]['Email'])
'''
1234    bondellen@williams-garza.com
Name: Email, dtype: object
'''

# How many people have American Express as their Credit Card Provider and made a purchase above $95 ?
print(ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price'] > 95)].count())
'''
Address             39
Lot                 39
AM or PM            39
Browser Info        39
Company             39
Credit Card         39
CC Exp Date         39
CC Security Code    39
CC Provider         39
Email               39
Job                 39
IP Address          39
Language            39
Purchase Price      39
dtype: int64
'''

# Hard: How many people have a credit card that expires in 2025 ?
print(ecom[ecom['CC Exp Date'].str.contains('25', case=False, na=False)].count())
'''
Address             1033
Lot                 1033
AM or PM            1033
Browser Info        1033
Company             1033
Credit Card         1033
CC Exp Date         1033
CC Security Code    1033
CC Provider         1033
Email               1033
Job                 1033
IP Address          1033
Language            1033
Purchase Price      1033
dtype: int64
'''

# Hard What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com etc)
print(ecom['Email'].apply(lambda email: email.split('@')[1]).value_counts().head(5))
'''
Email
hotmail.com     1638
yahoo.com       1616
gmail.com       1605
smith.com         42
williams.com      37
Name: count, dtype: int64
'''
