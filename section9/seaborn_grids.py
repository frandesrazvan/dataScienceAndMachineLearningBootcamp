import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')
print(iris.head())

# g = sns.PairGrid(iris)
# # g.map(plt.scatter)
# g.map_diag(sns.histplot)
# g.map_upper(plt.scatter)
# g.map_lower(sns.kdeplot)

tips = sns.load_dataset('tips')
print(tips.head())

g = sns.FacetGrid(data=tips, col='time', row='smoker')
g.map(sns.histplot, 'total_bill')
# g.map(sns.scatterplot, 'total_bill', 'tip')

plt.show()
