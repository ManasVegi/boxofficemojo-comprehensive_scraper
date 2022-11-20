import pandas as pd
import numpy as np
df1 = pd.read_csv('clean_aggregated_data.csv')
# df1.drop_duplicates(subset = ['titleId'], keep = 'first', inplace = True) 
df2 = pd.read_csv('cast_crew_opening.csv')

# df2.drop_duplicates(subset = ['titleId'], keep = 'first', inplace = True) 

print(df2.columns)
df3 = pd.concat([df1.set_index('titleId'),df2.set_index('titleId')], axis=1, join='inner')

df3.to_csv('master_dataset.csv')