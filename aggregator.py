import pandas as pd
import numpy as np
df = pd.read_csv('BoxOffice.csv')
df1 = df[df['domestic_gross'] != '-']
df1.drop_duplicates(subset = ['titleId'], keep = 'first', inplace = True) 
df2 = pd.read_csv('merged_data.csv')

df2.drop_duplicates(subset = ['titleId'], keep = 'first', inplace = True) 
print(len(df1))
print(df2.columns)
df3 = pd.concat([df1.set_index('titleId'),df2.set_index('titleId')], axis=1, join='inner')

# df3.to_csv('aggregated_data.csv')