import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

print(tips.head())
'''
   total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
1       10.34  1.66    Male     No  Sun  Dinner     3
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4
'''

# sns.distplot(tips['total_bill'], kde=False, bins=30)
# sns.jointplot(x='total_bill', y='tip', data=tips, kind='kde')  # default kind = 'scatter' | kind='hex' | kind='reg'
# sns.pairplot(tips, hue='sex', palette='coolwarm')
# sns.rugplot(tips['total_bill'])


plt.show()
