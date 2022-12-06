import pandas as pd
from collections import defaultdict
df = pd.read_csv('boxoffice_v1.5.csv')

actorRevenue = defaultdict(lambda: 0)
directorRevenue = defaultdict(lambda: 0)
for i, row in df.iterrows():
    bo = row['domestic_gross']
    for a in ('actor1', 'actor2', 'actor3'):
        actor = row[a]
        if pd.isna(actor) or len(actor) == 0:
            df.at[i, f'{a}_cumu_bo'] = 0
            continue
        df.at[i, f'{a}_cumu_bo'] = actorRevenue[actor]
        actorRevenue[actor] += bo
    directors = row['directors']
    if pd.isna(directors) or len(directors) == 0:
        df.at[i, f'directors_cumu_bo'] = 0
        continue
    df.at[i, f'directors_cumu_bo'] = directorRevenue[directors]
    directorRevenue[directors] += bo
    dArr = directors.split('|')
    if len(dArr) > 1:
        for d in dArr:
            directorRevenue[d] += bo
print(df['directors_cumu_bo'])
df.to_csv('box_office_v2.0.csv')