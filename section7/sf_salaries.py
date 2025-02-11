import pandas as pd

# Read Salaries.csv as a dataframe called sal
sal = pd.read_csv('Salaries.csv')
print(sal)

# Check the head of the DataFrame
print(sal.head())

# Use the .info() method to find out how many entries there are
print(sal.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 148654 entries, 0 to 148653
'''

# What is the average BasePay?
print(sal['BasePay'].mean())  # 66325.4488404877

# What is the highest amount of OvertimePay in the dataset?
print(sal['OvertimePay'].max())  # 245131.88

# What is the job title of JOSEPH DRISCOLL?
print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle'])
'''
24    CAPTAIN, FIRE SUPPRESSION
Name: JobTitle, dtype: object
'''

# How much does JOSEPH DRISCOLL make (including benefits)?
print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits'])
'''
24    270324.91
Name: TotalPayBenefits, dtype: float64
'''

# What is the name of highest paid person (including benefits)?
print(sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]['EmployeeName'])
'''
0    NATHANIEL FORD
Name: EmployeeName, dtype: object
'''

# What is the name of the lowest paid person (including benefits)?
# Do you notice something strange about how much he or she is paid?
print(sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()]['EmployeeName'])
'''
148653    Joe Lopez
Name: EmployeeName, dtype: object
'''

# What was the average(mean) BasePay of all employees per year? (2011-2014)?
print(sal.groupby('Year')['BasePay'].mean())  # 66325.4488404877
'''
Year
2011    63595.956517
2012    65436.406857
2013    69630.030216
2014    66564.421924
Name: BasePay, dtype: float64
'''

# How many unique job titles are there?
print(sal['JobTitle'].nunique())  # 2159

# What are the top 5 most common jobs?
print(sal['JobTitle'].value_counts().head(5))
'''
JobTitle
Transit Operator                7036
Special Nurse                   4389
Registered Nurse                3736
Public Svc Aide-Public Works    2518
Police Officer 3                2421
Name: count, dtype: int64
'''

# How many Job Title were represented by only one person in 2013? (e.g. Job Title with only one occurence in 2013?)
sal_2013 = sal[sal['Year'] == 2013]
job_counts = sal_2013['JobTitle'].value_counts()
unique_job_titles = (job_counts == 1).sum()
print(unique_job_titles)  # 202

# How many people have the word Chief in their job title?
print(sal[sal['JobTitle'].str.contains('Chief', case=False, na=False)].value_counts())  # 202


# def chief_string(title):
#     if 'chief' in title.lower().split():
#         return True
#     return False
#
#
# print(sum(sal['JobTitle'].apply(lambda x: chief_string(x))))

# BONUS: Is there a correlation between length of the Job Title string and Salary?
sal['title_len'] = sal['JobTitle'].apply(len)
print(sal[['TotalPayBenefits', 'title_len']].corr())
'''
                  TotalPayBenefits  title_len
TotalPayBenefits          1.000000  -0.036878
title_len                -0.036878   1.000000
'''
