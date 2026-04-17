import numpy as np
import pandas as pd

df = pd.read_csv('cars.csv')
df.head
df['brand'].value_counts()
df['fule'].value_counts()
