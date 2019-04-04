import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
    
    
    
def func1():
    data  = pd.read_csv('Social_Network_Ads.csv')
    x = data.iloc[: , [2 , 3]].values
    y= data.iloc[: , 4].values
    x_train , x_test ,y_train ,y_test = train_test_split(x, y ,test_size= 0.25 ,random_state = 0)
    classifier = RandomForestClassifier(n_estimators = 10 , criterion='entropy' , random_state = 0)
    classifier.fit(x , y)
    y_pred = classifier.predict(x_test)
    cm = confusion_matrix(y_test , y_pred)
    print(cm)
    print("\nlol")
    return cm
