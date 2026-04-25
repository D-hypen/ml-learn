import numpy as pd 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

df = pd.read_csv('placement.csv')
df.head

plt.figure(figsize=(16,5))
plt.subplot(1,2,1)
sns.distplot(df['cgpa'])

plt.subplot(1,2,2)
sns. distplot(df['placement_exam_marks'])
plt.show()

df['placement_exam_marks'].describe()
sns.bpxplot(df['placement_exam_marks'])

# Finding the IQR
percentile25 = df['placement_exam_marks'].quantile(0.25)
percentile75 = df['placement_exam_marks'].quantile(0.75)

percentile75 
iqr = percentile75 - percentile25
iqr

upper_limit = percentile75 + 1.5 * iqr
lower_limit = percentile25 + 1.5 * iqr

peint("Upper limit",upper_limit)
print("Lower limit",lower_limit)

df[df['placement_exam_marks'] > upper_limit]
df[df['placement_exam_marks'] > Lower_limit]

#  Trimming 

nwe_df = df[df['placement_exam_marks'] < upper_limit]
nwe_df.shape

# Comparing

plkt.figure(figsize=(16,8))
plt.subplot(2,2,1)
sns.distplot(df['placement_exam_marks'])

plt.subplot(2,2,2)
sns.boxplot(df['placement_exam_maeks'])

plt.subplot(2,2,3)
sns.boxplot(df['placement_exam_maeks'])

plt.subplot(2,2,4)
sns.boxplot(df['placement_exam_maeks'])

plt.show()

# Capping

nwe_df_cap = df.copy()

nwe_df_cap['placement_exam_marks'] = np.where(
    nwe_df_cap['placement_exam_marks'] > upper_limit,
    upper_limit,
    np.where(
        nwe_df_cap['placement_exam_marks'] < lower_limit,
        lower_limit,
        nwe_df_cap['placement_exam_marks']
    )

)
nwe_df_cap.shape

# Comparing

plt.figure(figsize=(16,8))
plt.subplot(2,2,1)
sns.distplot(df['placement_exam_marks'])

plt.subplot(2,2,2)
sns.distplot(df['placement_exam_marks'])

plt.subplot(2,2,3)
sns.distplot(df['placement_exam_marks'])

plt.subplot(2,2,4)
sns.distplot(df['placement_exam_marks'])
plt.show()







