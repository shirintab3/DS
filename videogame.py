import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("vgsales.csv")
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

#Which video game publisher sells the most number of units globally and how much?
max_Sales=data.groupby('Publisher')['Global_Sales'].sum().nlargest(1)
print(max_Sales)