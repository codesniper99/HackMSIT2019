import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def func2():
    data=pd.read_csv('50_Startups.csv')
    x=data.iloc[:,:-1].values
    y=data.iloc[:,4].values

    from sklearn.preprocessing import LabelEncoder , OneHotEncoder
    labelencoder_X=LabelEncoder()
    x[:,3] = labelencoder_X.fit_transform(x[:,3])
    onehotencoder = OneHotEncoder(categorical_features = [3])
    x=onehotencoder.fit_transform(x).toarray()

    x=x[:,1:]

    from sklearn.model_selection import train_test_split
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)


    from sklearn.linear_model import LinearRegression
    regressor = LinearRegression()
    regressor.fit(x_train,y_train)

    y_pred = regressor.predict(x_test)

    print(y_pred)
    return y_pred


