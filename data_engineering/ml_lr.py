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






test_pr_in=pd.read_csv('datasource/test_label.csv')
test_pr= test_pr_in
md_file = 'datasource/test_label.csv'
md_df = pd.read_csv(md_file)  #, header=0, index_col=False, keep_default_na=True
print(md_df)
X = md_df.drop(['Label','Test Case ID','Functionality Module','Test Case Description','Severity','Priority'], axis=1)  #'Test Case ID','Functionality Module','Test Case Description','Severity	Priority'
test_pr= test_pr.drop(['Label','Test Case ID','Functionality Module','Test Case Description','Severity','Priority'], axis=1)
y = md_df[['Label']]
# print(X)
# print(y)
# X_train,X_test,y_train,y_test=md_df(X,y,test_size=0.10,random_state=0)



scaler = StandardScaler(copy=True, with_mean=True, with_std=True)
scaler.fit_transform(X)
scaler.transform(test_pr)
print(test_pr)

#=========== LogisticRegression====================
logreg = LogisticRegression(max_iter=12500)
logreg.fit(X,y.values.ravel())

y_pred=logreg.predict(test_pr)
print("accuracy LogReg: {}".format(accuracy_score(y, y_pred)))
# Use score method to get accuracy of model
score = logreg.score(test_pr, y)
print(score)
cm = metrics.confusion_matrix(y, y_pred)
print(cm)

plt.figure(figsize=(9,9))
sns.heatmap(cm, annot=True, fmt=".3f", linewidths=.5, square = True, cmap = 'Blues_r');
plt.ylabel('Actual label');
plt.xlabel('Predicted label');
all_sample_title = 'Accuracy Score: {0}'.format(score)
plt.title(all_sample_title, size = 15);
# Precision = TP / (TP+FP) = 40 / (40+20) = 40/60 = 0.67
#
# Recall = TP / (TP+FN) = 40 / (40+10) = 40/50 = 0.80



pd.concat([pd.DataFrame({'Label':list(y_pred)}),test_pr_in], axis=1).to_csv('datasource/predictedfile.csv',index = False)
#pd.DataFrame(list(y_pred)).to_csv('datasource/predictedfile.csv')


X_train= md_df.drop(['Label','Test Case ID','Functionality Module','Test Case Description','Severity','Priority'], axis=1)
y_train = md_df[['Label']]
print(X_train)
print(y_train)

#=========== KNN====================
knn = KNeighborsClassifier(n_neighbors=2)

# fitting the model
knn.fit(X_train, y_train)
# predict the response
pred = knn.predict(test_pr)
print('knn =======================')
# evaluate accuracy
print("accuracy KNN: {}".format(accuracy_score(y_train, pred)))
cm = metrics.confusion_matrix(y_train, pred)
print(cm)

#=========== GaussianNB====================
modelGNB = GaussianNB()
modelGNB.fit(X_train, y_train);
ynew = modelGNB.predict(test_pr)
print('GaussianNB =======================')
# print(ynew)
print("accuracy GaussianNB: {}".format(accuracy_score(y_train, ynew)))



#=========== XGBClassifier====================
modelXGB = XGBClassifier(learning_rate = 0.05,
 n_estimators=300,
 max_depth=5)
modelXGB.fit(X_train, y_train)

y_predXGB= modelXGB.predict(test_pr)
print('XGBClassifier =======================')
print("accuracy GaussianNB: {}".format(accuracy_score(y_train, ynew)))



#=========== Random Forest Classifier====================
