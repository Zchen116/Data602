import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Load Avocado Dataset
df = pd.read_csv('https://raw.githubusercontent.com/Zchen116/assignments/master/avocado.csv')

#Data Exploration:
df.head()

average = df['AveragePrice'].mean()

print(average)

median = df['AveragePrice'].median()

print(median)




#Data Wrangling

df.rename(columns = {'Date':'DATE', 'type':'TYPE'}, inplace = True)

df['Difference'] = df['Small Bags'] - df['Large Bags']

print (df)

df.drop(['4046', '4225', '4770'], axis=1)

print (df)




#Data Visualization

boston_df = df[ df['region'] == "Boston" ]

boston_df = boston_df.set_index("DATE")

boston_df.head()

print(boston_df.head)

boston_df['AveragePrice'].plot()




NewYork_df = df[ df['region'] == "NewYork" ]

NewYork_df = NewYork_df.set_index("DATE")

NewYork_df.head()

print(NewYork_df.head)

NewYork_df['AveragePrice'].plot()

plt.title ('Average Price of Boston and NewYork Avocados')

plt.show()




regions = ['Boston','NewYork']

plt.boxplot([df[df.region == "Boston"].AveragePrice,df[df.region == "NewYork"].AveragePrice])

plt.xticks([1,2],regions)

plt.title ('Average Price of Boston and NewYork Avocados')

plt.show()

#Conclusion: Average price of New York is higher than Boston.


datayear = []

datayearBoston = []

datayearNewYork = []

bar_width = 0.20

for i in df.year.unique():
    
    datayear.append(df[df.year == i].AveragePrice)
    datayearBoston.append(df[(df.year == i) & (df['region'] == 'Boston')].AveragePrice.mean())
    datayearNewYork.append(df[(df.year == i) & (df.region == 'NewYork')].AveragePrice.mean())

plt.bar(np.arange(df.year.nunique()),datayearBoston,bar_width, label = 'Boston')

plt.bar(np.arange(df.year.nunique())+bar_width,datayearNewYork,bar_width, label = 'NewYork')

plt.xticks(np.arange(df.year.nunique())+bar_width/2,df.year.unique())

plt.title ('Average price of Boston and New York avocado for different years')

plt.legend(loc = 'upper right')

plt.show()

#Conclusion: Both average price and volume increases from 2015 to 2017, but they reach same level on 2018. 







