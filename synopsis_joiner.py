import pandas as pd
import numpy as np
df1 = pd.read_csv('synopsis_initial.csv')
# df1.drop_duplicates(subset = ['titleId'], keep = 'first', inplace = True) 
df2 = pd.read_csv('synopsis_missed.csv')

# df2.drop_duplicates(subset = ['titleId'], keep = 'first', inplace = True) 
df3 = pd.concat([df1, df2])
df = pd.read_csv('master_dataset.csv')
# print(df2.columns)
total = pd.concat([df.set_index('titleId'),df3.set_index('titleId')], axis=1, join='inner')

total.to_csv('boxoffice_with_synopsis.csv')