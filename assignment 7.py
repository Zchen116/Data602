#Core
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ml
from sklearn import datasets as ds
from sklearn import linear_model as lm
from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.model_selection import train_test_split as tts

# infra
import unittest

iris = ds.load_iris()
boston = ds.load_boston()


def exercise01():
    '''
        Data set: Iris
        Return the first 5 rows of the data including the feature names as column headings in a DataFrame and a
        separate Python list containing target names
    '''
    X = iris.data
    df = pd.DataFrame(X)
    df.columns = iris.feature_names
    df_first_five_rows=df[0:5]
    target_names = iris.target_names
    return df_first_five_rows,target_names



def exercise02(new_observations):
     '''
        Data set: Iris
        Fit the Iris dataset into a kNN model with neighbors=5 and predict the category of observations passed in 
        argument new_observations. Return back the target names of each prediction (and not their encoded values,
        i.e. return setosa instead of 0).
    '''
     X = iris.data
     df = pd.DataFrame(X)
     y = iris.target
     knn = KNN(n_neighbors=5)
     knn.fit(X,y)
     iris_predictions = knn.predict(X)
     return iris_predictions

    

def exercise03(neighbors,split):
    '''
        Data set: Iris
        Split the Iris dataset into a train / test model with the split ratio between the two established by 
        the function parameter split.
        Fit KNN with the training data with number of neighbors equal to the function parameter neighbors
        Generate and return back an accuracy score using the test data was split out
    '''
    random_state = 21
    X = iris.data
    df = pd.DataFrame(X)
    y = iris.target
    X_train, X_test, y_train, y_test = tts(X, y, test_size = 0.2, random_state = 21, stratify=y)
    knn = KNN(n_neighbors=5)
    knn.fit(X_train, y_train)
    knn_score = knn.score(X_test, y_test)
    return knn_score



def exercise04():
    '''
        Data set: Iris
        Generate an overfitting / underfitting curve of kNN each of the testing and training accuracy performance scores series
        for a range of neighbor (k) values from 1 to 30 and plot the curves (number of neighbors is x-axis, performance score 
        is y-axis on the chart).
    '''
    scores = []
    X_train, X_test, y_train, y_test = tts(iris.data, iris.target, test_size = .2, random_state=21, stratify = iris.target)
    for k in range(1,31):
        knn = KNN(n_neighbors = k)
        knn.fit(X_train, y_train)
        scores.append(knn.score(X_test, y_test))
    #plot using plotly
    fig = go.Figure([go.Scatter(x=range(1,31), y=scores)])
    fig.update_layout(title_text='Accuracy by Neighbors in Classifier', xaxis_title="Neighbors", yaxis_title="Accuracy")
    fig.show()
    py.plot(fig, sharing = 'public')
    plotly_overfit_underfit_curve_url = py.plot(fig, sharing = 'public')
    return plotly_overfit_underfit_curve_url
    



def exercise05():
    '''
        Data set: Boston
        Load sklearn's Boston data into a DataFrame (only the data and feature_name as column names)
        Load sklearn's Boston target values into a separate DataFrame
        Return back the average of AGE, average of the target (median value of homes or MEDV), and the target as NumPy values 
    '''
    bostondf = pd.DataFrame(data= np.c_[boston['data']],
                     columns= boston['feature_names'])
    bostont = pd.DataFrame(data= np.c_[boston['target']], columns = ['target'])
    average_age = np.mean(bostondf['AGE'])
    average_medv = np.mean(bostont['target'])
    medv_as_numpy_values = np.array(boston.target)
    return average_age, average_medv, medv_as_numpy_values


def exercise06():
    '''
        Data set: Boston
        In the Boston dataset, the feature PTRATIO refers to pupil teacher ratio.
        Using a matplotlib scatter plot, plot MEDV median value of homes as y-axis and PTRATIO as x-axis
        Return back PTRATIO as a NumPy array
    '''
    bostondf = pd.DataFrame(data= np.c_[boston['data']],
                     columns= boston['feature_names'])
    
    plot = plt.scatter(bostondf['PTRATIO'], boston.target)
    plt.title('MEDV Median Values by PT')
    plt.xlabel('PTRATIO')
    plt.ylabel('MEDV Median Value')
    plt.show()
    X_ptratio = np.array(bostondf['PTRATIO'])
    



def exercise07():
    '''
        Data set: Boston
        Create a regression model for MEDV / PTRATIO and display a chart showing the regression line using matplotlib
        with a backdrop of a scatter plot of MEDV and PTRATIO from exercise06
        Use np.linspace() to generate prediction X values from min to max PTRATIO
        Return back the regression prediction space and regression predicted values
        Make sure to labels axes appropriately
    '''
    bostondf = pd.DataFrame(data= np.c_[boston['data']],
                     columns= boston['feature_names'])
    reg = lm.LinearRegression()
    reg.fit(bostondf['PTRATIO'].values.reshape(-1,1), boston.target)
    prediction_space = np.linspace(min(bostondf['PTRATIO'].values), max(bostondf['PTRATIO'].values)).reshape(-1,1)
    reg_model = reg.predict(prediction_space)
    plt.scatter(bostondf['PTRATIO'], boston.target)
    plt.title('MEDV Median Values by PT')
    plt.xlabel('PTRATIO')
    plt.ylabel('MEDV Median Value')
    plt.plot(prediction_space, reg_model)
    plt.show()

    return reg_model, prediction_space

    



class TestAssignment7(unittest.TestCase):
    def test_exercise07(self):
        rm, ps = exercise07()
        self.assertEqual(len(rm),50)
        self.assertEqual(len(ps),50)

        
    def test_exercise06(self):
        ptr = exercise06()
        self.assertTrue(len(ptr),506)

        
    def test_exercise05(self):
        aa, am, mnpy = exercise05()
        self.assertAlmostEqual(aa,68.57,2)
        self.assertAlmostEqual(am,22.53,2)
        self.assertTrue(len(mnpy),506)

    def test_exercise04(self):
         print('Skipping EX4 tests')  

    
    def test_exercise03(self):
        score = exercise03(8,.25)
        self.assertAlmostEqual(exercise03(8,.3),.955,2)
        self.assertAlmostEqual(exercise03(8,.25),.947,2)
    
    def test_exercise02(self):
        pred = exercise02([[6.7,3.1,5.6,2.4],[6.4,1.8,5.6,.2],[5.1,3.8,1.5,.3]])
        self.assertTrue('setosa' in pred)
        self.assertTrue('virginica' in pred)
        self.assertTrue('versicolor' in pred)
        self.assertEqual(len(pred),3)

    
    def test_exercise01(self):
        df, tn = exercise01()
        self.assertEqual(df.shape,(5,4))
        self.assertEqual(df.iloc[0,1],3.5)
        self.assertEqual(df.iloc[2,3],.2)
        self.assertTrue('setosa' in tn)
        self.assertEqual(len(tn),3)

if __name__ == '__main__':
    unittest.main()
