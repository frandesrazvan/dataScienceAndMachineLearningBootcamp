import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

tips = sns.load_dataset('tips')
print(tips.head())

# sns.barplot(x='sex', y='total_bill', data=tips, estimator=np.std)  # default estimator is mean()

# sns.countplot(x='sex', data=tips)

# sns.boxplot(x='day', y='total_bill', data=tips)
# sns.boxplot(x='day', y='total_bill', data=tips, hue='smoker')

# sns.violinplot(x='day', y='total_bill', data=tips)
# sns.violinplot(x='day', y='total_bill', data=tips, hue='sex', split=True)

# sns.stripplot(x='day', y='total_bill', data=tips, jitter=True)

# sns.swarmplot(x='day', y='total_bill', data=tips)

plt.show()
