import numpy as pd 
import pandas as pd 

from sklearn . model_selection import train_text_split
from sklearn . input import SimpleImputer 
from sklearn . preprocessing import OneHotEncoder
from sklearn . preprocessing import MinMaxScaler 
from sklearn . tree import DecisionTreeClassifier 
df = pd.read_csv('train.csv')
df.head()

df . drop (columns=['PassengerId','Name','Ticket','Cabin'],inplace=True)
#step 1 -> train/test/split
X_train,X_text,y_train,y_text = train_test_split(df.drop(colums=['Survived'])),
df['Survived'],
test_size = 0.2
random_state = 45 
X_train.head(2)
#applying imputation

si_age = SimpleImputer()
si_embarked = SimpleImputer(strategy = 'most_frequent')


X_train_age = si_age.fit_transform(X_train[['Age']])
X_train_embarked = si_embarked.fit_transform(X_train[['Embarked']])

X_train_age = si_age.transform(X_text[['Age']])
X_train_embarked = si_embarked.transform(X_text[['Embarked']])

#one hot encoding Sex and Embarked 
ohe_sex = OneHotEncoder(sparse=False,handle_unknown='ignor')
ohe_embarked = OneHotEncoder(sparse=False,handle_unknown='ignor')

X_train_sex = ohe_sex.fit_transform(X_train[['sex']])

X_train_rem = X_train_drop(columns=['sex','Age','Embaeked'])
X_train_rem = X_train_drop(colums=['sex','Age','Embarked'])

X_train_transformed = np.concatenate((X_train_rem,X_train_age,X_train_sex,X_train_embarked),axis=1)
X_train_transformed = np.concatenate((X_train_rem,X_train_age,X_train_sex,X_train_embarked),axis=1)
X_train_transformed = np.concatenate((X_train_rem,X_train_age,X_train_sex,X_train_embarked),axis=1)
X_train_transformed = np.concatenate((X_train_rem,X_train_age,X_train_sex,X_train_embarked),axis=1)
X_train_transformed = np.concatenate((X_train_rem,X_train_age,X_train_sex,X_train_embarked),axis=1)
clf = DecisionTreeClassifier()
clf.fit(X_train_transformed,y_train)

DecisionTreeClassifier()

y_pred = clf.predict(X_text_transformed)
from sklearn.metrics import accuracy_score , accuracy_score(y_test , y_pred)

import pickle
pickle.dump(ohe_sex,open('models/ohe_sex.pkl','wb'))
pickle.dump(ohe_embarked,open('models/ohe_embarked.pkl','wb'))
pickle.dump(clf,open('models/clf.pkl','wb'))