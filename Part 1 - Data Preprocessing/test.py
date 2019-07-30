# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 03:14:00 2019

@author: deepak
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing dataset 
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values # matrix of features
y = dataset.iloc[:, 3].values # dependent variable vector

#taking care of missing learn
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values= 'NaN', strategy= 'mean', axis = 0)
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])

#Encoding catergorical data
from sklearn.preprocessing import LabelEncoder , OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
onehotencoder = OneHotEncoder(categorical_features= [0])
X = onehotencoder.fit_transform(X).toarray()
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

#Splitting  the dataset  into Trainig set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0) 

#Feature scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)