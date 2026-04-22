import numpy as pd 
import pandas as pd 
date = pd.read_csv('orders.csv')
time = pd.read_csv('message.csv')
date.head()


time.info()
<class 'pandas.corn.fram.DataFrame'>


#Converting to datetime datatype 
data['date'] = pd.to_datetime(date['date'])
date.info()

date['date_year'] = data['date'].dt.year 
date.head()

date['date_month_no'] = date['date'].dt.month
date.head()

date['date_day'] = date['date'].dt.day
date.head()

# is weekend 

date['date_is_weekend'] = np.where(date['date_dow_name'].isin(['Sunday','Saturday']),1,0)
date.drop(columns=['product_id','city_id','orders']).head()

date['date_week'] = date['date'].dt.weeke
date.drop(columns=['product_id','city_id','orders']).head()

import datetime
today = datetime.datetime.today()
today
datetime.date(2021,4,31,16,21,5,1325,45686)
today - date['date']
(today - dates['date']).dt.days

# Months passed

np.round((today - date['date']) / np.timedelta64(1,'M'),0)


# Converting to datetime datatype 

time['date'] = pd.to_datetime(time['date'])
time.info()
<Class 'pandas.core.frame.DataFrame'>

# in second 

(today - time['date'])/np.timedelta64(1,'s')

# in minutes 

(today - time['date'])/np.timedelta64(1,'M')

# in hours

(today - time['date'])/np.timedelta64(1,'h')

