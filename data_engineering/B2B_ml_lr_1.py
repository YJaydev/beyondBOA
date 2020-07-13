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
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import metrics







test_pr_in=pd.read_csv('../B2B/fnl.csv')
test_pr= test_pr_in
md_file = '../B2B/labeldata2.csv'
md_df = pd.read_csv(md_file)
X = md_df.drop(['Test Case id','label'], axis=1)
y = md_df[['label']]
test_pr = X


scaler = StandardScaler(copy=True, with_mean=True, with_std=True)
scaler.fit_transform(X)
scaler.transform(test_pr)
# print(test_pr)

#=========== LogisticRegression====================
logreg = LogisticRegression(max_iter=12500)
logreg.fit(X,y.values.ravel())

y_pred=logreg.predict(test_pr)
print(y_pred)
print(y.values.ravel())
print(len(y_pred))


print("accuracy LogReg: {}".format(accuracy_score(y, y_pred)))
# Use score method to get accuracy of model
score = logreg.score(test_pr, y)
print(score)
cm = metrics.confusion_matrix(y, y_pred)
print(cm)

# plt.figure(figsize=(9,9))
# sns.heatmap(cm, annot=True, fmt=".3f", linewidths=.5, square = True, cmap = 'Blues_r');
# plt.ylabel('Actual label');
# plt.xlabel('Predicted label');
# all_sample_title = 'Accuracy Score: {0}'.format(score)
# plt.title(all_sample_title, size = 15);
# Precision = TP / (TP+FP) = 40 / (40+20) = 40/60 = 0.67
#
# Recall = TP / (TP+FN) = 40 / (40+10) = 40/50 = 0.80


X_train= md_df.drop(['Test Case id','label'], axis=1) #md_df.drop(['Label','Test Case ID','Functionality Module','Test Case Description','Severity','Priority'], axis=1)
y_train = md_df[['label']] #md_df[['Label']]
# print(X_train)
# print(y_train)

#=========== KNN====================
knn = KNeighborsClassifier(n_neighbors=5)

# fitting the model
knn.fit(X_train, y_train.values.ravel())
# predict the response
pred = knn.predict(test_pr)
print('======= knn =======================')
# evaluate accuracy
print("accuracy KNN: {}".format(accuracy_score(y_train, pred)))
cm = metrics.confusion_matrix(y_train, pred)
print(cm)

#=========== GaussianNB====================
modelGNB = GaussianNB()
modelGNB.fit(X_train, y_train.values.ravel());
ynew = modelGNB.predict(test_pr)
print('==========GaussianNB =======================')
print(ynew)
print("accuracy GaussianNB: {}".format(accuracy_score(y_train, ynew)))



#=========== XGBClassifier====================
modelXGB = XGBClassifier(learning_rate = 0.05,
 n_estimators=300,
 max_depth=5)
modelXGB.fit(X_train, y_train.values.ravel())

y_predXGB= modelXGB.predict(test_pr)
print('=======XGBClassifier =======================')
print(y_predXGB)
print("accuracy GaussianNB: {}".format(accuracy_score(y_train, y_predXGB)))

test_pr= test_pr_in
scaler.transform(test_pr)
y_predXGB= modelXGB.predict(test_pr)
print(y_predXGB)
pd.concat([pd.DataFrame({'Label':list(y_predXGB)}),test_pr_in], axis=1).to_csv('../B2B/F_predfile.csv', index = False)
#=========== Random Forest Classifier====================



#=========== LogisticRegression Model prediction====================
print('=======prediction after trainging =======================')
# test_pr_in=pd.read_csv('B2B/fnl.csv')
test_pr= test_pr_in

scaler.transform(test_pr)

logreg = LogisticRegression(max_iter=12500)
logreg.fit(X,y.values.ravel())

y_pred=logreg.predict(test_pr)
# print(y_pred)
# print(y.values.ravel())
print(len(y_pred))
print(len(test_pr.columns))
print(559*3036)


# pd.concat([pd.DataFrame({'Label':list(y_pred)}),test_pr_in], axis=1).to_csv('B2B/F_predfile.csv',index = False)

