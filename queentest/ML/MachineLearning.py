import csv
import numpy as np
# Load libraries
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

filename = './SubData/data50and60and70.csv'


#url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
#names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
names0 = ['time4sub','time11sub','solution?','n','SAT']

#dataset = pandas.read_csv(url, names=names)
data = pandas.read_csv(filename,names=names0)
#print(data.shape)
#print(data.head(500))
# Split-out validation dataset
array = data.values
print(data.head(20))
#print(array)United Kingdom
X = array[:,0:4]
Y = array[:,4]
Y = Y.transpose()
#print("X :=",X)
#print("Y :=",Y)
validation_size = 0.2
seed = 3
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)
# Test options and evaluation metric
seed = 3
scoring = 'accuracy'
# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))
# evaluate each model in turn
results = []
names = []
for name, model in models:
	kfold = model_selection.KFold(n_splits=10, random_state=seed)
	cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
	results.append(cv_results)
	names.append(name)
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	print(msg)
#data.hist()
#plt.show()
#scatter_matrix(data)
#plt.show()
# Make predictions on validation dataset
# Compare Algorithms
#fig = plt.figure()
#fig.suptitle('Algorithm Comparison')
#ax = fig.add_subplot(111)
#plt.boxplot(results)
#ax.set_xticklabels(names)
#plt.show()
knn = KNeighborsClassifier()
lr = LogisticRegression()
knn.fit(X_train, Y_train)
#print(X_validation)
query_n =np.array([[0.0765219097,0.227670254,0.1,70]])
#predictions = knn.predict(X_validation)
predictions = knn.predict(X_validation)
print(predictions)
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))