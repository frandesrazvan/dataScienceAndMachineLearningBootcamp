# Import numpy and pandas
import numpy as np
import pandas as pd

# Import visualization libraries
import matplotlib.pyplot as plt

# Read in the csv file as a dataframe called df
df = pd.read_csv('911.csv')

# Check in the info() of the df
print(df.info())

# Check the head of df
print(df.head())

# What are the top 5 zipcodes for 911 calls?
print(df['zip'].value_counts().head(5))

# What are the top 5 townships (twp) for 911 calls?
print(df['twp'].value_counts().head(5))

# Take a look at the 'title' column, how many unique title codes are there?
print(df['title'].nunique())

# In the titles column there are 'Reasons/Departments' specified before the title code. There are EMS, Fire, and Traffic.
# Use .apply() with a custom lambda expression to create a new column called 'Reason' that contains this string value

# For example if the title column value is EMS: BACK PAINS/INJURY, the reason column value would be EMS
df['Reason'] = df['title'].apply(lambda title: title.split(':')[0])
print(df['Reason'])

# What is the most common Reason for a 911 call based off of this new column?
print(df['Reason'].value_counts())

# Now user seaborn to create a countplot of 911 calls by Reason
import seaborn as sns
import matplotlib.pyplot as plt

# sns.countplot(x='Reason', data=df)
# plt.show()

# Now let us begin to focus on time information. What is the data type of the objects in the timeStamp column?


# You should have seen that these timestamps are still strings. Use pd.to_datetime to convert the column from strings to DateTime objects.
df['timeStamp'] = pd.to_datetime(df['timeStamp'])
print(df['timeStamp'])

# You can now grab specific attributes from a Datetime object by calling them. For example:
time = df['timeStamp'].iloc[0]
print(time.hour)  # 17

# Now that he timestamp column are actually DateTime objects, use .apply() to create 3 new columns called Hour, Month and Day of Week.
# You will create these columns based off of the timeStamp column, reference the solutions if you ge stuck on this step
df[['Hour', 'Month', 'Day of Week']] = pd.DataFrame({
    'Hour': df['timeStamp'].dt.hour,
    'Month': df['timeStamp'].dt.month,
    'Day of Week': df['timeStamp'].dt.day_of_week
})

print(df[['Hour', 'Month', 'Day of Week']])

# Notice how the DAy of Week is an integer 0-6. Use the .map() with this dictionary to map the actual string names to the day of the week
dmap = {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'}

df['Day of Week'] = df['Day of Week'].map(dmap)
print(df[['Hour', 'Month', 'Day of Week']])

# Now use seaborn to create a countplot of the Day of Week column with the hue based off of the Reason column
# sns.countplot(x='Day of Week', data=df, hue=df['Reason'])
# plt.show()

# Now create a groupby object called byMonth, where you group the DataFrame by the month column and use the count()
# method for aggregation. Use th head() method on thi returned DataFrame
group_month = df.groupby('Month').count()
print(group_month.head())

# Now create a simple plot off of the dataframe indicating the count of calls per month
# group_month['lat'].plot()
# plt.show()

# Now see if you can use seaborn's Implot() to create a linear fit on the number of calls per month.
# Keep in mind you may need to reset the index to a column
# sns.lmplot(x='Month', y='twp', data=group_month.reset_index())
# plt.show()

# Create a new column called 'Date' that contains the date from the timeStamp column.
# You will need to use apply along with the .date() method
df['Date'] = df['timeStamp'].apply(lambda t: t.date())
print(df['Date'])

# Now groupby this Date column with the count() aggregate and create a plot of counts of 911 calls.
# group_date = df.groupby('Date').count()
# group_date['lat'].plot()
# plt.tight_layout()
# plt.show()

# Now recreate this plot but create 3 separate plots with each plot representing a Reason for the 911 call
# group_date = df[df['Reason'] == 'Fire'].groupby('Date').count()  # Reason = EMS | Fire | Traffic
# group_date['lat'].plot()
# plt.title('Fire')  # EMS | Fire | Traffic
# plt.tight_layout()
# plt.show()

# Restructure the dataframe so that the columns become the Hours and the Index becomes the Day of the Week.
# You can use unstack method
dayHour = df.groupby(by=['Day of Week', 'Hour']).count()['Reason'].unstack()
print(dayHour)

# Now create a HeatMap using this new DataFrame
# sns.heatmap(dayHour, cmap='viridis')
# plt.show()

# Now create a clustermap using this DataFrame
# sns.clustermap(dayHour)
# plt.show()

# Now repeat these same plots and operations, for a DataFrame that shows the Month as the column.
month = df.groupby(by=['Day of Week', 'Month']).count()['Reason'].unstack()
print(month)

# sns.heatmap(month)
sns.clustermap(month)
plt.show()
