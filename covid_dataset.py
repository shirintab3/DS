import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("covid_data.csv")
#print(data.head())
data = data[['Country_Region', 'Confirmed', 'Recovered', 'Deaths', 'Active']]
data.columns = ('Country','Confirmed','Recovered','Deaths','Active')
'''print(data.head())
print(data.isnull().sum())

confirmed = pd.DataFrame(data.groupby('Country')['Confirmed'].sum().reset_index())
                               
print(confirmed)

top10_confirmed = confirmed.sort_values(by='Confirmed', ascending=False).head(10)

#top10_confirmed.plot(kind='bar', color='green')
plt.bar(top10_confirmed['Country'], top10_confirmed['Confirmed'], color='green')
plt.title('Top 10 Countries by Recovered COVID-19 Cases')
plt.ylabel('Number of Recovered Cases')
plt.xlabel('Country')
plt.legend()
# Show the plot
plt.show()'''





# Filter the data for a specific country (e.g., India)
india_data = data[data['Country'] == 'India'][['Confirmed', 'Recovered', 'Deaths']].sum()

# Plot the global data
plt.figure(figsize=(5, 5))

plt.bar(india_data.index, india_data.values, color=['blue', 'green', 'red'])
plt.title('COVID-19 Data for India')
plt.ylabel('Total Numbers')
plt.xlabel('Categories')
plt.show()
