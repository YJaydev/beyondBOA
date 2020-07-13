import numpy as np
from sklearn import preprocessing, neighbors
from sklearn.model_selection import cross_val_predict, cross_val_score, cross_validate
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_breast_cancer

X= load_breast_cancer().data
y= load_breast_cancer().target

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,y,test_size=0.2)

clf = LinearRegression(normalize=True)
clf.fit(X_train, y_train)

accuracy= clf.score(X_test, y_test)
print(accuracy)