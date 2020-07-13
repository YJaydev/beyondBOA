import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
#from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
# from sklearn import metrics
from sklearn.metrics import classification_report, accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from xgboost import XGBClassifier




test_pr_in=pd.read_csv('datasource/All_Features.csv')
# test_pr_in=pd.read_csv('datasource/train_label.csv')
test_pr= test_pr_in
md_file = 'datasource/train_label.csv'
md_df = pd.read_csv(md_file)  #, header=0, index_col=False, keep_default_na=True
print(md_df)
X = md_df.drop(['Label','Test Case ID','Functionality Module','Test Case Description','Severity','Priority'], axis=1)  #'Test Case ID','Functionality Module','Test Case Description','Severity	Priority'
test_pr= test_pr.drop(['Test Case ID','Functionality Module','Test Case Description','Severity','Priority'], axis=1)
y = md_df[['Label']]
print(X)
print(y)
# X_train,X_test,y_train,y_test=md_df(X,y,test_size=0.10,random_state=0)

scaler = StandardScaler(copy=True, with_mean=True, with_std=True)
scaler.fit_transform(X)
scaler.transform(test_pr)
#
#
logreg = LogisticRegression(max_iter=12500)
logreg.fit(X,y.values.ravel())

y_pred=logreg.predict(test_pr)
# print(y.values.ravel())
# print(pd.DataFrame(list(y_pred)))
# print(list(y_pred))
# print(y_pred)
# print(classification_report(y_pred,test_pr))
# df = pd.DataFrame({'Label':list(y_pred)})
# label=pd.DataFrame(list(y_pred))
pd.concat([pd.DataFrame({'Label':list(y_pred)}),test_pr_in], axis=1).to_csv('datasource/predictedfile.csv',index = False)
#pd.DataFrame(list(y_pred)).to_csv('datasource/predictedfile.csv')


# print(logreg.score(y_pred, y.values.ravel()))

X_train= md_df.drop(['Label','Test Case ID','Functionality Module','Test Case Description','Severity','Priority'], axis=1)
y_train = md_df[['Label']]

knn = KNeighborsClassifier(n_neighbors=3)

# fitting the model
knn.fit(X_train, y_train)


# predict the response
pred = knn.predict(test_pr)
print('knn =======================')
print(pred)

# evaluate accuracy
#print("accuracy: {}".format(accuracy_score(y_test, pred)))





modelGNB = GaussianNB()
modelGNB.fit(X_train, y_train);
ynew = modelGNB.predict(test_pr)
print('GaussianNB =======================')
print(ynew)




# fit model no training data
modelXGB = XGBClassifier(learning_rate = 0.05,
 n_estimators=300,
 max_depth=5)
modelXGB.fit(X_train, y_train)

y_predXGB= modelXGB.predict(test_pr)
print('xgboost =======================')
print(y_predXGB)


predictions = [value for value in y_predXGB]
print(predictions)

# evaluate predictions
# from sklearn.metrics import accuracy_score
# accuracy = accuracy_score(y_train, ynew)
# print("Accuracy: %.2f%%" % (accuracy * 100.0))

