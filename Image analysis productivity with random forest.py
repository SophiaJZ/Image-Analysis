# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 05:50:41 2023

@author: sophi
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('D:/Python/python_for_microscopists-master/python_for_microscopists-master/other_files/images_analyzed_productivity1.csv')
print (df.head())
#sizes = df['Productivity'].value_counts(sort = 1)
#print(sizes)

#Drop missing values

#df = df.dropna()
# Drop irrelevant columns

df.drop(['Images_Analyzed'], axis=1, inplace=True)
df.drop(['User'], axis=1, inplace=True)
#print(df.head())

#converting non-numeric to numeric

df.Productivity[df.Productivity=='Good'] = 1
df.Productivity[df.Productivity=='Bad'] = 2
#print(df.head())

#define dependent variable should be an integer
 
Y = df['Productivity'].values
Y = Y.astype(int)

#define independent variable = all variable except Y , just drop Y

X = df.drop(labels=['Productivity'], axis=1)

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.4, random_state=20)

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=10, random_state=20)
model.fit (X_train, Y_train)
predict_test = model.predict(X_test)
#print(predict_test)

from sklearn import metrics

print('Accuracy score =', metrics.accuracy_score(Y_test,predict_test))

feature_list = list(X.columns)
#print(feature_list)
feature_imp = pd.Series(model.feature_importances_, index = feature_list).sort_values(ascending=False)
print(feature_imp)


