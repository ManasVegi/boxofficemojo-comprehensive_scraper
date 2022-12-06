import pandas as pd
import numpy as np
df = pd.read_csv('boxoffice_with_synopsis.csv')
# uniqueEditors, uniqueDirectors, uniqueComposers, uniqueProducers = set(), set(), set(), set()
# numEditors, numDirectors, numComposers, numProducers = 0, 0, 0, 0
numBudget = 0
actors = set()
for i, row in df.iterrows():
    for a in ('actor1', 'actor2', 'actor3'):
        if row[a] != '-':
            actors.add(row[a].lower())
df_op = pd.DataFrame(sorted(list(actors)))
df_op.to_csv('actors.csv', header=['actor'])

#     if row["budget"] != '-':
#         numBudget += 1
#     editors = row['editors']
#     editorArray = editors.split(",")
#     if editorArray[0] != '-':
#         numEditors += len(editorArray)
#         for e in editorArray:
#             uniqueEditors.add(e.lower())
#     d = row['directors']
#     dArray = d.split("|")
#     if dArray[0] != '-':
#         numDirectors += len(dArray)
#         for e in dArray:
#             uniqueDirectors.add(e.lower())
#     c = row['composers']
#     cArray = c.split("|")
#     if cArray[0] != '-':
#         numComposers += len(cArray)
#         for e in cArray:
#             uniqueComposers.add(e.lower())
#     p = row['composers']
#     pArray = p.split("|")
#     if pArray[0] != '-':
#         numProducers += len(pArray)
#         for e in pArray:
#             uniqueProducers.add(e.lower())
# print("Total number of rows", len(df))
# print("Number of unique editors: ", len(uniqueEditors))
# print("Average number of editors:", numEditors / len(df[df["editors"] != '-']))
# print("Number of unique directors: ", len(uniqueDirectors))
# print("Average number of directors:", numDirectors / len(df[df["directors"] != '-']))
# print("Number of unique composers: ", len(uniqueComposers))
# print("Average number of composers:", numComposers / len(df[df["composers"] != '-']))
# print("Number of unique producers: ", len(uniqueProducers))
# print("Average number of producers:", numProducers / len(df[df["producers"] != '-']))
# print("Number of movies that reported budget: ", numBudget)