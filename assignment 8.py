import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456"
)

#print(mydb)

#Load Data: The Iris dataset was used in R.A. Fisher's classic 1936 paper, The Use of Multiple Measurements in Taxonomic Problems, and can also be found on the UCI Machine Learning Repository.


import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             db='iris')


cursor=connection.cursor()

cursor.execute('SELECT * FROM iris.iris')

#for row in cursor:
    #print(row)


#Data Exploration:
sql01 = cursor.execute('SELECT AVG(SepalLengthCm) FROM iris.iris')
for row in cursor:
    print(row)

sql02 = cursor.execute('SELECT Sum(SepalLengthCm) FROM iris.iris')
for row in cursor:
    print(row)

sql03 = cursor.execute('SELECT AVG(PetalLengthCm) FROM iris.iris')
for row in cursor:
    print(row)

sql04 = cursor.execute('SELECT Sum(PetalLengthCm) FROM iris.iris')
for row in cursor:
    print(row)


#Data Wrangling:
df = pd.read_csv('https://raw.githubusercontent.com/Zchen116/Data602/master/Iris.csv')

df = df.drop('Id', axis=1)

df.rename(columns = {'SepalWidthCm':'sepal_width', 'SepalLengthCm':'sepal_length', 'Species':'SPECIES'}, inplace = True)

print (df)

#Data Visualizations:

df.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)

plt.show()

#

df.hist()

plt.show()

#From the graph, we can see two of the input variables have a normal distribution


fig = px.scatter(df, x="PetalLengthCm", y="PetalWidthCm", color="SPECIES")

fig.show()

#Conclusion: we can see Blue points (Iris-setosa) can be easily separated from red (Irir-versicolor) and green (Iris-virginica) by using PetalLength and PetalWidth.

fig = px.scatter(df, x="sepal_width", y="sepal_length", color="SPECIES")

fig.show()

#Conclusion: the species: Iris-setosa is not really realted to the other two across all feature combinations.

#Prediction
array = df.values

X = array[:,0:4]

y = array[:,4]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.4, stratify = y)

knn = KNeighborsClassifier(n_neighbors = 6)

knn.fit(X_train, y_train)

print(knn.score(X_test, y_test))

#The accuracy is 0.96 or 96%.


