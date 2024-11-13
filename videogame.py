import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("C:\\Users\\shiri\\OneDrive\\Desktop\\Data Science\\extras\\vgsales.csv")
data.index = range(1,16599)
#.loc is index referece but iloc is index position of the row
print(data.loc[1])
print(data.shape)
print(data.info())
print(data.isnull().sum())
print("\n\n")
data.dropna(inplace=True)

print(data.shape)

data['Year'] = data['Year'].astype(int)

#Find the top 10 best publishers of video games sold in North America.

top_10=data.groupby('Publisher')['NA_Sales'].sum().nlargest(10)
print(top_10)



NorthAm=data["Publisher"].unique()
#print(NorthAm)
print(len(NorthAm))

# Group by publisher and sum sales across different regions

data['Total_Sales'] = data[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum(axis=1)

publisher_sales = data.groupby('Publisher')[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].sum()
top_10_publishers = publisher_sales.sum(axis=1).sort_values(ascending=False).head(10).index


publisher_sales_top10 = publisher_sales.loc[top_10_publishers]
plt.figure(figsize=(12, 8))
regions = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']

for region in regions:
    plt.plot(publisher_sales_top10.index, publisher_sales_top10[region], label=region)

# Add labels, title, and legend
plt.xlabel('Publisher')
plt.ylabel('Units Sold (millions)')
plt.title('Total Units Sold by Top 10 Publishers Across Different Regions')
plt.xticks(rotation=45, ha="right")
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()


#Which video game publisher sells the most number of units globally and how much?
max_Sales=data.groupby('Publisher')['Global_Sales'].sum().nlargest(1)
print(max_Sales)
