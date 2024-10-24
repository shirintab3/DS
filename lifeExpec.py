import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("LifeExpectancy.csv")
print(data.shape)

# Strip leading and trailing spaces from column names
data.columns = data.columns.str.strip()


# Find columns with missing values and their count
missing_values = data.isnull().sum()


# Filter columns with missing values
missingdata=(missing_values[missing_values > 0])
print(type(missingdata))

#Drop all the columns from the DataFrame containing more than 15% percent of the missing values.

data = data.loc[:, data.isnull().mean() <= 0.15]
print(data.shape)
print(data.head())
#Replace the missing values in the remaining columns with the median 
#data=data.fillna(data.median())
print(data.isnull().sum())

numeric_cols = data.select_dtypes(include=['number'])  # Select only numeric columns
data[numeric_cols.columns] = numeric_cols.fillna(numeric_cols.median())
print(data.isnull().sum())

#Create a bar plot to find out whether 
# the average age of death had increased globally in a period of 15 years i.e. between 2000 and 2015.
# Filter the data for the years 2000 and 2015
data_filtered = data[data['Year'].isin([2000, 2015])]

# Group by year and calculate the average life expectancy for each year
avg_life_expectancy = data_filtered.groupby('Year')['Life expectancy'].mean()

# Create a bar plot to compare the average life expectancy in 2000 and 2015
plt.figure(figsize=(8, 6))
avg_life_expectancy.plot(kind='line', color=['blue', 'green'])

# Add labels and title
plt.title('Average Life Expectancy Comparison (2000 vs 2015)')
plt.xlabel('Year')
plt.ylabel('Average Life Expectancy (Years)')

# Show the plot
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

#Line plot
# Filter the data for the years 2000 to 2015
data_new = data[(data['Year'] >= 2000) & (data['Year'] <= 2015)]

# Group by year and calculate the average life expectancy for each year
lifeExpect = data_new.groupby('Year')['Life expectancy'].mean()

# Create a line plot to show the changes in life expectancy over the years
plt.figure(figsize=(10, 6))
plt.plot(lifeExpect.index, lifeExpect.values, marker='o', linestyle='-', color='blue')

# Add labels and title
plt.title('Global Average Life Expectancy (2000 - 2015)')
plt.xlabel('Year')
plt.ylabel('Average Life Expectancy (Years)')

# Show the plot
#plt.grid(True)

#plt.show()



#In which year, the average life expectancy was maximum?
lifeMax = data.groupby('Year')['Life expectancy'].mean()
print(lifeMax.idxmax())
print(lifeMax.max())




#Create a barplot for yearly life expectancy of developing and developed countries 
#in a single bar chart.

yearly_life = data.groupby(['Year', 'Status'])['Life expectancy'].mean().unstack()

# Create a bar plot to show the life expectancy for Developing and Developed countries
#plt.figure(figsize=(12, 6))
yearly_life.plot(kind='bar', width=0.8, figsize=(12, 6))

# Add labels and title
plt.title('Average Life Expectancy for Developing vs Developed Countries (All Years)')
plt.xlabel('Year')
plt.ylabel('Average Life Expectancy (Years)')
plt.ylim(60, 90)

# Show the plot
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()