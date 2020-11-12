import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt

d1=pd.read_csv('monthly-hpi.csv') #Monthly Housing Price Index

d2=pd.read_csv('fed_funds.csv') #Federal Funds

d3=pd.read_csv('gdp.csv') #GDP

d4=pd.read_csv('shiller.csv') #Shiller

d5=pd.read_csv('unemployment-macro.csv') #Unemployment CSV

result=pd.merge(d1, d2, on='date')
result=pd.merge(result, d3, on='date')
result=pd.merge(result, d4, on='date')
result=pd.merge(result, d5, on='date')

#result made with first column as date to match all the data

result=result.iloc[:,1:]

#result made after removing date as a criteria

y=result.iloc[:,0] # y is hpi
y=y.astype('int')
result=result.iloc[:,1:]
#print y
#print result

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(result, y, test_size = 0.2, random_state = 0)

# Fitting Naive Bayes to the Training set
#from sklearn.svm import SVC	
#classifier = SVC()
#classifier.fit(X_train,y_train)



#Linear Regression
from sklearn import linear_model

classifier=linear_model.LinearRegression()
classifier.fit(X_train,y_train)

filename = 'finalized_model.sav'
pickle.dump(classifier, open(filename, 'wb'))

# Predicting the Test set results
y_pred = classifier.predict(X_test)

print y_pred
print(type(y_test))
print(type(X_test))
# Making the Confusion Matrix
#from sklearn.metrics import confusion_matrix
#cm = confusion_matrix(y_test, y_pred)   
#print cm;         

#from sklearn.metrics import accuracy_score
#asd= accuracy_score(y_test,y_pred)    
#print asd;

#plot outputs

print y_test 

x1=X_test['gross_domestic_product']

col=len(X_test.columns)
for i in range(0, col-1):
	plt.scatter(X_test.iloc[:,i], y_test,  color='black')
	plt.plot(X_test.iloc[:,i], y_pred, color='blue', linewidth=3)
	plt.xlabel(X_test.columns.get_values()[i])
	plt.ylabel('HPI')	
	plt.show()

#ax = x1.plot()
#y_test.plot(ax=ax)
