import pandas as pd
df = pd.read_csv('customer.csv')
df.sample(5)

df = df.iloc[:,2:]
df.head()

from sklearn.model_selection import train_text_split
X_train,X_text,y_train,y_text = train_text_split(df.iloc[:,0:2],df.iloc[:,-1],text_size=0.2)
X_train
from sklearn.preprocessing import OrdinalEncoder
X_train

oe = OrdinalEncoder(categories=[['poor','Average','Good',],['School','UG','PG']])
oe.fit(X_train)
OrdinalEncoder(categories=[['poor','Average','Good',],['School','UG','PG']])
X_train = oe.transform(X_train)
X_train



