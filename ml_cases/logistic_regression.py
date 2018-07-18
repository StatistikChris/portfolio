import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression


df = pd.read_csv('./creditcard_fraud_subsample.csv', sep = ';')

df = df.drop(['Time'], axis=1)

df['Amount_norm'] = (df.Amount-df.Amount.mean())/df.Amount.std()

msk = np.random.rand(len(df)) < 0.6

train = df[msk]

test = df[~msk]


X = train.drop(['Amount','Class'], axis=1)
y = train['Class']

X_test = test.drop(['Amount','Class'], axis=1)
y_test = test['Class']

logisticRegr = LogisticRegression(penalty = 'l2' ,solver = 'liblinear')
logistic_model = logisticRegr.fit(X, y) 
accuracy = np.mean(np.equal(logistic_model.predict(X_test),y_test))  

#accuracy = pd.DataFrame(eval(accuracy))

#accuracy.to_csv('./accuracy.csv')

f = open("accuracy.txt", "w")
f.write( str(accuracy)  )    
f.close()
